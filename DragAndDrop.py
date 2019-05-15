# !/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, QLineEdit
import json

class FileEdit(QLineEdit):
    """
        Petit hack ici:
        la fonction dropEvent ne peut pas renvoyer des résultats
        (on a un TypeError: invalid result from FileEdit.dropEvent())
        alors on lui passe en paramètre une fonction, qu'il va executer lors de la reception de données
    """
    def __init__(self, title, trigger):  # , theReturnList):
        super(FileEdit, self).__init__()
        self.setText(title)
        self.setReadOnly(True)
        self.setDragEnabled(True)
        self.trigger = trigger
        # self.theReturnList = theReturnList

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        print(urls)
        for url in urls:
            print(url.scheme())       
            filepath = str(url.path())
            sucessfully_loaded = []
            failed = []
            try:
                with open(filepath, "r") as fichier: 
                    liste = json.loads(fichier.read())
                print(liste, "was just sucessfully loaded")
                sucessfully_loaded.append((filepath, liste))
            except Exception as e:
                failed.append(filepath)
                print(e)
        if failed:
            dialog = QMessageBox()
            if len(failed) > 1:
                dialog.setWindowTitle("Error: Invalid Files")
            else:
                dialog.setWindowTitle("Error: Invalid File")
            error_text = "An error occured when loading :"
            for failure in failed:
                error_text += "\n" + failure
            dialog.setText(error_text)

            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()
        for success in sucessfully_loaded:
            get_name_from_path = lambda path : path.split("/")[-1].split('.', 1)[0]
            filepath, liste = success
            self.trigger(get_name_from_path(filepath), liste)
        #return sucessfully_loaded

        #self.theReturnList = self.theReturnList + sucessfully_loaded
        #print(self.theReturnList)