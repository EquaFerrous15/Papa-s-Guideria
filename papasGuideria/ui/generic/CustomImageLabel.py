from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class CustomImageLabel(QLabel):
    """A custom image label to be displayed."""

    def __init__(self, image_path: str, parent=None):
        super().__init__(parent)

        self.original_pixmap = QPixmap()
        if not self.original_pixmap.load(image_path):
            print(f"Image not found. ({image_path})")
        self.setPixmap(self.original_pixmap)

    def resize_image(self, width: int, height: int):
        """Resizes the image to the given pixel lengths."""
        resized_pixmap = self.original_pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(resized_pixmap)

    def resize_image_keep_aspect(self, width: int, height: int):
        """Resizes the image to the given pixel lengths, keeping the aspect ratio."""
        resized_pixmap = self.original_pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(resized_pixmap)

