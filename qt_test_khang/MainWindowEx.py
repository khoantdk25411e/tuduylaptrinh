from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()

    def setupSignalAndSlots(self):
        self.pushButton.cliked.connect(self.nut_1)



    def showWindow(self):
        self.MainWindow.show()

    def nut_1(self):
