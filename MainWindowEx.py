from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonchangetext.clicked.connect(self.processChangeText)
        self.pushButtonfontsize.clicked.connect(self.processChangeFontSize)
        self.pushButtonalignleft.clicked.connect(self.processAlignLeft)
        self.pushButtonaligncenter.clicked.connect(self.processAlignCenter)
        self.pushButtonalignright.clicked.connect(self.processAlignRight)
        self.pushButtonshowpng.clicked.connect(self.processChangePNG)
        self.pushButtonshowgif.clicked.connect(self.processChangeGIF)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.labelname.setText("https://tranduythanh.com")
    def processChangeFontSize(self):
        font = self.labelname.font()
        font.setPointSize(20)
        font.setItalic(True)
        font.setBold(True)
        font.setFamily("Cambria")
        self.labelname.setFont(font)
    def processAlignLeft(self):
        self.labelname.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.labelname.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.labelname.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangePNG(self):
        pixmap = QPixmap("images/hehe.png")
        self.imagelabel.setPixmap(pixmap)
    def processChangeGIF(self):
        movie = QMovie("images/download.gif")
        self.imagelabel.setMovie(movie)
        movie.start()
