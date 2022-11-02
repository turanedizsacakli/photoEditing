dlg = QFileDialog(self, "Open", "", "Yaml(*.yaml)")
        filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            FILE_NAME = str(QFileInfo(filenames[0]).baseName())




I found a solution.

QFileDialog has a method called setAcceptMode(QFileDialog.AcceptMode) which allows you to change between Open and Save. http://pyqt.sourceforge.net/Docs/PyQt4/qfiledialog.html#setAcceptMode

Usage for open:

QFileDialog.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
Usage for Save:

QFileDialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)