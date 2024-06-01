from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QUrl, QTimer, QThread, pyqtSignal, QObject
from PyQt6.QtMultimedia import QSoundEffect
from package.ui.mainwindow_ui import Ui_MainWindow
import time
import os
import rust_modules

class Downloader(QThread):
    def run(self):
        if rust_modules.is_dir_empty(".\\server"):
            rust_modules.download_create_server()
        else:
            rust_modules.download_update_server()
        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        cato_gif = QMovie("assets/cato.gif")

        self.ui.cato.setMovie(cato_gif)
        cato_gif.start()

        self.ui.startServerBtn.clicked.connect(self.start_server)
        self.ui.downloadServerBtn.clicked.connect(self.download_server)

        if rust_modules.is_dir_empty(".\\config"):
            self.config_dialog()

        self.show()

    
    def start_server(self):
        rust_modules.start_server()


    def download_server(self):
        if rust_modules.check_server_status() == "Offline":
            self.downloader = Downloader()
            
            self.downloader.start()
        else:
            self.error_dialog("Server tá online, dê 'stop' antes de fazer download")

            return
        

    # TODO
    def upload_server(self):
        pass
    

    # TODO
    def check_status(self):
        pass


    # TODO
    def error_dialog(self, error: str):
        pass

    
    # TODO
    def config_dialog(self):
        pass