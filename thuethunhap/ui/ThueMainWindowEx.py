from thuethunhap.ui.ThueMainWindow import Ui_MainWindow


class ThueMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow (self):
        self.MainWindow.show()

