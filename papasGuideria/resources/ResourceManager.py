import os
import tomllib

from PyQt5.QtGui import QFontDatabase


class ResourceManager:
    """Class to manage and access resources easily."""

    _setup_completed = False
    _font_dict: dict[str, str] = {}
    _image_dict: dict[str, any] = {}
    _colour_dict: dict[str, str] = {}

    @classmethod
    def resources_setup(cls):
        """Set up all resources."""
        cls._font_setup()
        cls._image_setup()
        cls._colour_setup()
        cls._setup_completed = True

    @classmethod
    def get_font(cls, font_name: str):
        """Get a font from the font dictionary."""
        if not cls._setup_completed:
            cls.resources_setup()

        # If the font name doesn't exist, return arial to avoid errors.
        if font_name not in cls._font_dict.keys():
            return "arial"

        return cls._font_dict[font_name]

    @classmethod
    def _font_setup(cls):
        """Set up the font dictionary using the font config file."""
        cls._font_dict = {}

        with open("papasGuideria/resources/fonts/fontconfig.toml", "rb") as file:
            config_data = tomllib.load(file)

            for font_config in config_data.items():
                # Handle if the toml config has the wrong layout.
                if not isinstance(font_config[1], dict):
                    print(f"Font config error: Unexpected item '{font_config[0]}'.")
                    continue

                name = font_config[0]
                data = font_config[1]

                # Handle if the toml config is missing data.
                if "name" not in data.keys():
                    print(f"Font config error: Font '{name}' missing font name. (name = ?)")
                    continue
                elif "file" not in data.keys():
                    print(f"Font config error: Font '{name}' missing font file. (file = ?)")
                    continue
                # Handle if the toml config has extra unnecessary data.
                elif len(data.keys()) > 2:
                    print(f"Font config error: Unexpected items in font '{name}'. Font creation unaffected.")

                font_name = data["name"]
                font_path = f"papasGuideria/resources/fonts/{data['file']}"

                if not os.path.exists(font_path):
                    print(f"Font config error: Font file '{data['file']}' not  for.")
                    continue

                QFontDatabase.addApplicationFont(font_path)
                cls._font_dict[name] = font_name

    @classmethod
    def get_image(cls, image_name: str):
        """Gets an image from the image dictionary."""
        if not cls._setup_completed:
            cls.resources_setup()

        if image_name not in cls._image_dict.keys():
            return "null"

        return cls._image_dict[image_name]

    @classmethod
    def image_exists(cls, image_name: str):
        """Returns if the given image exists in the image dictionary."""
        if image_name in cls._image_dict.keys():
            return True
        else:
            return False

    @classmethod
    def _image_setup(cls):
        """Set up the image dictionary by finding the images."""
        cls._image_dict = {}

        path = "papasGuideria/resources/images"
        for root, dirs, files in os.walk(path):
            root = root.replace("\\", "/")
            folder = root.replace(path, "").lstrip("/")

            for file in files:
                file_name = f"{folder}/{file}"
                file_name = file_name.replace(".png", "")
                file_path = f"{root}/{file}"
                cls._image_dict[file_name] = file_path

    @classmethod
    def get_colour(cls, colour_name: str) -> str:
        """Returns a colour hex-code string."""
        if not cls._setup_completed:
            cls.resources_setup()

        if colour_name not in cls._colour_dict.keys():
            return "#000000"

        return cls._colour_dict[colour_name]

    @classmethod
    def _colour_setup(cls):
        """Set up the colour dictionary."""
        cls._colour_dict = {
            "text_light_grey": "#a19f9f",
            "text_dark_grey": "#505050",
            "closer_red": "#CD0101",
            "jojo_blue": "#0167CD",
            "pizzeria": "#3e5a27",
            "burgeria": "#08359a",
            "taco_mia": "#c44000",
            "freezeria": "#7c0c9e",
            "pancakeria": "#dbb304",
            "wingeria": "#8e0404",
            "hot_doggeria": "#089374",
            "cupcakeria": "#bf317d",
            "pastaria": "#8a9709",
            "donuteria": "#3da0b5",
            "cheeseria": "#d17b02",
            "bakeria": "#6c0e28",
            "sushiria": "#002919",
            "scooperia": "#ae96e0",
            "mocharia": "#4c3120",
            "cluckeria": "#d55b44"
        }
