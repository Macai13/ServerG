from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QUrl, QTimer, QThread, pyqtSignal, QObject
from PyQt6.QtMultimedia import QSoundEffect
from package.ui.mainwindow_ui import Ui_MainWindow
import time
import os
import rust_modules

class Downloader(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def download(self):
        if rust_modules.is_server_dir_empty():
            try:
                os.system("git clone https://github.com/vctorfarias/minecraft-server-01 ./server")
            except:
                os.system("mkdir server")
                os.system("git clone https://github.com/vctorfarias/minecraft-server-01 ./server")
        else:
            try:
                os.system("cd ./server")
                os.system("git reset --hard origin/main")
                os.system("cd ..")
            except:
                os.system("git clone https://github.com/vctorfarias/minecraft-server-01 ./server")


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

        self.show()

    
    def start_server(self):
        rust_modules.start_server()


    def download_server(self):
        if rust_modules.check_server_status() == "Online":
            self.error_dialog("Server tá online, dê 'stop' antes de fazer download")

            return
        
        self.thread = QThread()

        self.downloader = Downloader()

        self.downloader.moveToThread(self.thread)

        self.thread.started.connect(self.downloader.download)

        self.downloader.finished.connect(self.thread.quit)
        self.downloader.finished.connect(self.downloader.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        self.ui.downloadServerBtn.setEnabled(False)

        self.thread.finished.connect(
            lambda: self.ui.downloadServerBtn.setEnabled(True)
        )


    def upload_server(self):
        pass
    

    # TODO
    def check_status(self):
        pass


    # TODO
    def error_dialog(error: str):
        pass