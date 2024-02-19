from tkinter import messagebox
from PyQt6 import QtWidgets, QtCore, QtGui
from sys import path
path.append('program')
from engine import File, Stack, check_accountig_folders, is_internet_connected
from toolBar import setup_toolbar
from connections import Ui_windowLauncher


class Launcher(object):
    
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.param = File("settings/param.json")
        self.log_in = File("ressources/log_in.json")
        self.lang_file = File("ressources/lang/"+str(self.param.get_dict()["lang"])+".json")
        if not is_internet_connected():
            messagebox.showwarning(self.lang_file.get_page_text("connections_page", "no_internet_title"), self.lang_file.get_page_text("connections_page", "no_internet_msg"))

    def set_lang(self, lang):
        """Sets the language of the application"""
        self.param.set_pref("lang", lang)
        self.lang_file = File("ressources/lang/"+str(self.param.get_dict()["lang"])+".json")
        # update the folders for accounting
        check_accountig_folders()
        if not self.undo_stack.is_empty():
            self.set_page(self.undo_stack.pages_stack[-1])
        
    def set_page(self, page):
        """Displays the page and stack it
        
        Args:
            - {Qt template} page: template
        """
        # check if the user double clicked on a button
        if self.undo_stack.is_empty():
            # add the page to the undo stack
            self.undo_stack.stack(page)

        elif self.undo_stack.pages_stack[-1] != page:
            # add the page to the undo stack
            self.undo_stack.stack(page)
        return page.setupUi(self)

    def undo(self):
        """Comes back to the previous visited page"""
        # case when we can not undo
        if self.undo_stack.is_empty():
            return
        # --- Remove the actual page from the undo stack --- #
        page = self.undo_stack.unstack()
        # store it into the redo stack
        self.redo_stack.stack(page)

        # --- Display the previous page --- #
        # case when there was only one page in the stack
        if self.undo_stack.is_empty():
            page.setupUi(self)
            return
        page = self.undo_stack.unstack()
        self.redo_stack.stack(page)
        page.setupUi(self)

    def redo(self):
        """Redo the action that has been undone"""
        # case when we can not redo
        if self.redo_stack.is_empty():
            return
        # --- Remove the actual page from the redo stack --- #
        page = self.redo_stack.unstack()
        # store it into the undo stack
        self.undo_stack.stack(page)

        # --- Display the page before going back --- #
        # case when there was only one page in the stack
        if self.redo_stack.is_empty():
            page.setupUi(self)
            return
        page = self.redo_stack.unstack()
        self.undo_stack.stack(page)
        page.setupUi(self)

    def show(self):
        # preparation of the window
        self.MainWindow.setMinimumSize(QtCore.QSize(1000, 562))
        if self.param.get_dict()["fullscreen"] == "True":
            self.MainWindow.showMaximized()
        # title of the application
        self.MainWindow.setWindowTitle("APPLICATION")
        self.set_page(Ui_windowLauncher())
        setup_toolbar(self, self)
        self.MainWindow.show()

    def log_account(self, account):
        """Creates a attribute to store the connected account
        
        Args:
            - account: Vinted object or Email object
        """
        self.google_account = account

    def is_connected(self, account:str = "V") -> bool:
        """Returns False if the user is not connected to their account"""
        if account == "V":
            return hasattr(self, 'vinted_api')
        return hasattr(self, 'google_account')
    
    def not_co_vinted(self):
        """Returns a message to tell the user that he is not connected to its Vinted account"""
        if not self.is_connected():            
            messagebox.showwarning(
                self.lang_file.get_pop_up_text("vinted_connection_error_title"),
                self.lang_file.get_pop_up_text("vinted_connection_error_desc")
            )
            return True

if __name__ == "__main__":
    import sys

    # initialize the application
    app = QtWidgets.QApplication(sys.argv)
    windowLauncher = Launcher()
    windowLauncher.show()
    # Set the app icon
    app.setWindowIcon(QtGui.QIcon("gui/icons/labrotique_logo.png"))    
    # loop to keep the app running
    sys.exit(app.exec())