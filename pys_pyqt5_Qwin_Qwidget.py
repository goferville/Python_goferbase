import  sys
from PyQt5.QtWidgets import (QMainWindow,QWidget, QAction, qApp, QApplication, QMenu,
                             QLabel, QLineEdit, QTextEdit, QGridLayout,
                             QVBoxLayout, QHBoxLayout,
                             QPushButton)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        # add Widget (button, tetxbox etx)
        # I use a layout to add two instances of Widget
        #self.layout = QHBoxLayout()

        self.formWidget=centralWidget()

        self.setCentralWidget(self.formWidget) # if I only add formWidget1 to mainwindow


    def initUI(self):
        # Here we initi everything in a 'Window' likw: menu, toolbar, etc
        #templ_: define actions-items inmenus & submenus
        exitAct=QAction(QIcon('./Icons/Shutdown.ico'), '&EXIT', self) # '/.' = under current project directory
        exitAct.setShortcut('Ctrl-Q')
        exitAct.setStatusTip('Exit Application!')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('./win98_icons/directory_open_file_mydocs.ico'), '&open', self)  # '/.' = under current project directory
        openAct.setShortcut('Ctrl-O')
        openAct.setStatusTip('open Application!')
        openAct.triggered.connect(qApp.quit)

        #templ_: init status bar
        self.statusBar()

        #region templ_: define menu bar

        menubar=self.menuBar()

        #add main menu title
        filemenu1 = menubar.addMenu('&FIle') # add main menu item 1
        filemenu2 = menubar.addMenu('&Edit')  # add main menu item 2
        # add 1st level sub menu items - add actions
        filemenu1.addAction(openAct)
        filemenu1.addAction(exitAct)

        # sub menu
        submenu1=QMenu('&Import', self) #sub menu is QMenu()
        subact11=QAction('&Import from FIle',self) #subActions - submenu items
        subact11.setIcon(QIcon('./win98_icons/directory_open_file_mydocs_2k.ico'))

        subact12 = QAction('&Import from Web', self)#subActions - submenu items
        subact12.setIcon(QIcon('./win98_icons/directory_open_net_web_documents.ico'))

        submenu1.addAction(subact11)
        submenu1.addAction(subact12)
        filemenu1.addMenu(submenu1)
        #endregion templ_: define menu bar
        #region toolBar
        #Add actions to toolbar
        self.toolbar=self.addToolBar('Actions')
        self.toolbar.addAction(subact11)
        self.toolbar.addAction(subact12)
        self.toolbar.addAction(openAct)
        self.toolbar.addAction(exitAct)
        #endregion: toolBar

        #region label & text box
        commType=QLabel('Communication')
        commMsg=QLabel('Message')
        txLbl=QLabel('Tx')
        rxLbl = QLabel('Rx')
        txMsg=QLineEdit()
        rxMsa=QTextEdit()

        grid=QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(commType, 2, 0)
        grid.addWidget(commMsg, 2, 1)
        self.setLayout(grid)
        #endregion label & text box

        #region templ_: set main window
        self.setGeometry(500,300,600,300) # x and y positions, width and of the window.
        self.setWindowTitle('PyQt5 Example')
        #self.windowIcon(QIcon('web.ico'))
        self.show()
        #endregion templ_:

class formWedgit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.layout=QVBoxLayout()
        self.bt1=QPushButton('Button 1')
        self.bt2 = QPushButton('Button 2')
        self.bt3 = QPushButton('Button 3')
        self.layout.addWidget(self.bt1)
        self.layout.addWidget(self.bt2)
        self.layout.addWidget(self.bt3)
        self.setLayout(self.layout)
class centralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.layout=QHBoxLayout()
        self.fWidget1 = formWedgit()
        self.fWidget2 = formWedgit()
        self.fWidget3= formWedgit()
        self.layout.addWidget(self.fWidget1)
        self.layout.addWidget(self.fWidget2)
        self.layout.addWidget(self.fWidget3)
        self.setLayout(self.layout)

print(__name__)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
