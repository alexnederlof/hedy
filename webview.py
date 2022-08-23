from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication


def run_viewer():
    app = QApplication([])
    web = QWebEngineView()

    # Initialize web engine
    # Set window title
    web.setWindowTitle("Hedy code")
    web.setZoomFactor(1)
    # set window size
    web.resize(web.maximumSize())
    # set window zoom

    # load the url
    web.load(QUrl("http://localhost:8080"))
    # Show the results
    web.show()
    # web.setZoomFactor(1.5)
    app.exec()
