from PyQt6.QtWidgets import QMainWindow, QDialog
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QThread
from package.ui.mainwindow_ui import Ui_MainWindow
from package.ui import configdialog_ui
import subprocess
import datetime
import rust_modules

class Log(QThread):
    def run(self):
        subprocess.call("mkdir logs", creationflags=0x08000000, shell=True)
        subprocess.call("mkdir logs/minecraft-logs", creationflags=0x08000000, shell=True)
        subprocess.call("git clone https://github.com/vctorfarias/minecraft-log-1 ./logs/minecraft-logs", creationflags=0x08000000, shell=True)
        open("logs/git_log.txt", "w")


class Uploader(QThread):
    def run(self):
        if rust_modules.is_dir_empty(".\\server"):
            return 
        else:
            rust_modules.upload_server()


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
        self.ui.saveServerBtn.clicked.connect(self.upload_server)
        self.ui.configButton.clicked.connect(self.config_dialog)

        rust_modules.pull_log_from_gith()

        self.show()

        if rust_modules.is_dir_empty(".\\logs"):
            self._log = Log()
            
            self._log.start()

        if rust_modules.is_dir_empty(".\\userconfig"):
            subprocess.call("mkdir userconfig", creationflags=0x08000000, shell=True)

            self.config_dialog()

    
    def start_server(self):
        rust_modules.start_server()


    def download_server(self):
        if rust_modules.check_server_status() == "Offline":
            self._downloader = Downloader()
            
            self._downloader.start()
            self.update_log("download")
            rust_modules.update_log()
        else:
            self.error_dialog("Server tá online, dê 'stop' antes de fazer download")

            return


    def upload_server(self):
        if rust_modules.check_server_status() == "Offline":
            self._uploader = Uploader()
            
            self._uploader.start()
            self.update_log("upload")
            rust_modules.update_log()
        else:
            self.error_dialog("Server tá online, dê 'stop' antes de fazer download")

            return
    

    def get_time(self):
        date = datetime.datetime.now()

        return f"{date.day:02}/{date.month:02}/{date.year} {date.hour:02}:{date.minute:02}:{date.second:02}"


    # TODO
    def check_status(self):
        pass


    # TODO
    def error_dialog(self, error: str):
        pass

    
    def config_dialog(self):
        dialog = QDialog()
        ui = configdialog_ui.Ui_Dialog()
        ui.setupUi(dialog)
        
        ui.counter.setText(str(ui.horizontalSlider.value()))

        ui.horizontalSlider.valueChanged.connect(lambda: self.update_slider_value(ui.horizontalSlider, ui.counter))

        ui.cancelBtn.clicked.connect(dialog.close)
        ui.saveBtn.clicked.connect(lambda: self.update_user_properties(ui.plainTextEdit.toPlainText(), ui.horizontalSlider.value()))

        dialog.exec()

    
    def update_slider_value(self, slider, counter):
        counter.setText(str(slider.value()))

    
    def update_user_properties(self, name, ram):
        f = open("./userconfig/user.properties", "w+")
        f.write(f"NOME: \n{name}\n\nRAM: \n{ram}G")

        f.close()

    
    def update_log(self, action: str):
        user_file = open("./userconfig/user.properties", "r")
        user_file.readline()
        user = user_file.readline().replace('\n', '')
        log_file = open("./logs/minecraft-logs/latest.txt", "a")
        log_file.write(f"\n{user} - {self.get_time()} - {action}")

        log_file.close()
        user_file.close()