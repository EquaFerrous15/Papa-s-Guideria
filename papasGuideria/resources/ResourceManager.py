import os
import tomllib

from PyQt5.QtGui import QFontDatabase


class ResourceManager:
    """Class to manage and access resources easily."""

    _setup_completed = False
    _font_dict: dict[str, str] = {}

    @classmethod
    def resources_setup(cls):
        """Set up all resources."""
        cls._font_setup()
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



