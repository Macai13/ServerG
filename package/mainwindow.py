from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtMultimedia import QSoundEffect
from package.ui.mainwindow_ui import Ui_MainWindow
import time
import rust_modules

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        cato_gif = QMovie("assets/cato.gif")

        self.ui.cato.setMovie(cato_gif)
        cato_gif.start()

        self.ui.startServerBtn.clicked.connect(self.start_server)

        self.show()

    
    def start_server(self):
        rust_modules.start_server()


    def download_server(self):
        pass 


    def upload_server(self):
        pass
    
    # TODO
    def check_status(self):
        pass