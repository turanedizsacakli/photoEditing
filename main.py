import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication , QFileDialog
# from PyQt5.uic import loadUi
from photoEditing import Ui_MainWindow
from PIL import Image
import datetime

class myApp(QtWidgets.QMainWindow,QDialog):
    def __init__(self):
        super(myApp, self).__init__()
        # loadUi("D:\000_PROGRAMLAMA\deneme\untitled.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newPhotoName=""
        self.imagePathOldtoNew=""
        self.ui.browse.clicked.connect(self.browsefiles)
        self.ui.radioButton_thumbnail.toggled.connect(self.thumbnailFunction)
        self.ui.radioButton_compress.toggled.connect(self.compress)
        self.ui.radioButton_resize.toggled.connect(self.sizeChange)
        self.ui.radioButton_watermark.toggled.connect(self.watermark)
        self.ui.radioButton_rotation.toggled.connect(self.rotation)
        self.ui.radioButton_CFormat.toggled.connect(self.CFormat)
        
        # , ,"D:\\","Images(*.png, *.JPG, *.jpg, *.jpeg)"
    def browsefiles (self):
        fname=QFileDialog.getOpenFileName(self,"Open file" )
        self.imagePathOldtoNew=fname[0]
        self.ui.filename.setText(self.imagePathOldtoNew)
        self.pathOfImage()

    def nameImage(self):
        an = datetime.datetime.now()
        self.newPhotoName=str(an.hour)+str(an.minute)+str(an.microsecond)
        return self.newPhotoName
    
    def pathOfImage (self):
        imgPath=self.imagePathOldtoNew
        imgPath=imgPath.split("/")
        imgPath.pop()
        self.imagePathOldtoNew="/".join(imgPath)
        print(self.imagePathOldtoNew)

    def thumbnailFunction (self):
        tn = self.sender()
        with Image.open(self.browsefiles()) as img:
            extension=img.format.lower()
            img.thumbnail(size=(400,400))
            img.save( f"{self.imagePathOldtoNew}/{self.newPhotoName}.{extension}",format=(self.imagePathOldtoNew,self.newPhotoName,extension) )
        # if tn.isChecked():
            #print('seçilen ülke: '+ tn.text())
            
    
    def compress (self):
        c== self.sender()
        with Image.open(self.browsefiles()) as img:
            extension=img.format.lower()
            img.save(f"./dist/compressed.{extension}", format=extension, quality=self.ui.textBrowser_compress.toPlainText())
        pass

    def sizeChange (self):
        rs = self.sender()
        path=self.ui.filename.toPlainText.text
        with Image.open(path) as img:
            extension=img.format.lower()
            resized=img.resize(size=(500, 300))
            path.split("/")

            resized.save(f"./resized.{extension}",format=extension)
        pass

    def watermark (self):
        # wm== self.sender()
        # with Image open(" ./halo.jpg ") as img:
        # with Image open( /assets/hicoders png > as logo:
        #     image=img.convert("RGBA ")
        #     logo_ size = int(img.size[0]*.1)
        #     rbga_logo=logo.convert("RGBA")
        #     rbga_logo.thumbnail(size=(logo.size, logo.size))
        #     padding=10
        #     img_w, img_h=img.size
        #     dest=(img_ _W (10go. size + padding) img h(10go. size padding))
        #     image alpha, composite(im=rbga logo dest=dest)
        #     image save(" /dist/composite png format="PNG")
        pass

    def rotation (self):
        r== self.sender()
        pass

    def CFormat (self):
        cf== self.sender()
        pass

    def visibility (self):
        pass


 

def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton {border-radius:10px; background-color: black; color:white; border:10px;}")
    
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(myApp())
    
    win = myApp()
    win.show()
    sys.exit(app.exec_())
    
app()

