print("Can I haz QtCore")
from PyQt6.QtCore import QUrl
print("Can I haz QtWidgets")
from PyQt6.QtWidgets import QApplication
print("Can I haz QtWebEngineWidgets")
from PyQt6.QtWebEngineWidgets import QWebEngineView


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
