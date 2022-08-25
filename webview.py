
import random
from PyQt6.QtCore import QUrl, QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Viewer:
    """
    Should actually be called WebWindow or something.
    It's the class that holds the logic to show a chrome
    based browser, that loads Hedy
    """

    def __init__(self, url) -> None:
        # QT Applications need a running QApplication
        # This works with some shady python singleton stuff
        # So everything created after this knows of 
        # QApplication
        self.app = QApplication([])
        self.url = url

    def run_viewer(self):
        self.web = QWebEngineView()
        web = self.web
        # Initialize web engine
        # Set window title
        web.setWindowTitle("Hedy code")
        web.setZoomFactor(1)
        # set window size
        max = web.maximumSize()
        ideal = QSize(min(max.width(), 1280), max.height())
        web.resize(ideal)
        web.move(web.geometry().center())
        # set window zoom

        # load the url
        web.load(QUrl(self.url))
        # Show the results
        web.show()
        # web.setZoomFactor(1.5)
        self.app.exec()

    def show_error(self, message):
        """
        This shows a window with just a text message. Handy
        in case you've packaged your app on a Mac, and you
        can no longer get console output.
        """
        w = ErrorWidget(message)
        w.resize(800, 600)
        w.show()
        self.app.exec()


class ErrorWidget(QWidget):
    def __init__(self, message):
        QWidget.__init__(self)

        self.text = QLabel(message)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)