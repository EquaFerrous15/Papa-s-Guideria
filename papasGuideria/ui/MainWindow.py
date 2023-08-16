from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QToolBar, QAction, QWidget, QStyle
from .generic.AbstractScreen import AbstractScreen


class MainWindow(QMainWindow):
    """The main ui window."""

    def __init__(self):
        super().__init__()

        self.main_widget = QStackedWidget()
        self.back_button_action = QAction()

        self.setWindowTitle("Papa's Guideria")
        self.create_ui()

    def create_ui(self) -> None:
        """Set up the ui of the widget."""
        # Overall style
        self.setStyleSheet(
            "background: white;")

        # Widgets
        self.main_widget = QStackedWidget()
        self.setCentralWidget(self.main_widget)

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Back button
        back_button_icon = self.style().standardIcon(QStyle.SP_ArrowBack)
        self.back_button_action: QAction = toolbar.addAction(back_button_icon, "Back")
        self.back_button_action.triggered.connect(lambda: self.return_to_previous_screen())

    def show_new_screen(self, new_screen: AbstractScreen) -> None:
        """Shows the new screen over any previous screens."""
        self.main_widget.insertWidget(0, new_screen)
        self.update_window()

    def update_window(self) -> None:
        """Updates the window based on current screen."""
        self.main_widget.setCurrentIndex(0)
        size_hint = self.main_widget.currentWidget().sizeHint()
        if size_hint.isValid():
            self.setFixedSize(size_hint)

        # If on main screen, do not allow to go back, as it will crash the program.
        if self.main_widget.count() == 1:
            self.back_button_action.setEnabled(False)
        else:
            self.back_button_action.setEnabled(True)

    def return_to_previous_screen(self):
        """Returns to the previous screen, destroying the current one."""
        old_screen: QWidget = self.main_widget.widget(0)
        self.main_widget.removeWidget(old_screen)
        old_screen.setParent(None)
        self.update_window()


