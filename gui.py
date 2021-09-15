
import datetime
import sys

from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
	QApplication, QMainWindow,
	QGridLayout, QWidget, QLabel,
	QLineEdit, QMenu, QAction,
	QToolBar, QGroupBox, QVBoxLayout,
	QHBoxLayout
)
from PyQt5.QtGui import QIcon

#=======================================================================
#=======================================================================
#=======================================================================
__author__  = 'LawlietJH'				# Desarrollador
__title__   = 'SendFile'				# Nombre
__version__ = 'v1.0.0'					# Versión
#=======================================================================
#=======================================================================
#=======================================================================

class Window(QMainWindow):
	
	def __init__(self, parent=None):
		super().__init__(parent)
		self._createWindow()
		self._createGrid()
		self._createActions()
		self._createMenuBar()
		self._createToolBars()
		self._connectActions()
		self._createStatusBar()
	
	#===================================================================
	# GUI
	
	def _createWindow(self):
		self.setWindowTitle(__title__+' '+__version__ + ' - By: ' + __author__)
		self.setWindowIcon(QIcon('icons/icon.png'))
		self.widthSize, self.heightSize = 480, 480
		self.setFixedSize(self.widthSize, self.heightSize)
		self.wordlist = None
	
	def _createGrid(self):
		
		vbl_main = QVBoxLayout()
		
		w = QWidget()
		w.setLayout(vbl_main)
		self.setCentralWidget(w)
		
		gb_data = QGroupBox('Data')
		gb_info = QGroupBox('Info')
		
		gl_info = QGridLayout()
		gl_data = QGridLayout()
		
		gb_info.setLayout(gl_info)
		gb_data.setLayout(gl_data)
		
		vbl_main.addWidget(gb_info)
		vbl_main.addWidget(gb_data)
		
		#---------------------------------------------------------------
		
		# Pos: 0, 0
		l_localHostName = QLabel('Name:')
		
		# Pos: 0, 1
		le_localHostName = QLineEdit('Eny')
		le_localHostName.setReadOnly(True)
		
		# Pos: 0, 2
		l_localHost = QLabel('Host:')
		
		# Pos: 0, 3
		le_localHost = QLineEdit('0.0.0.0')
		le_localHost.setReadOnly(True)
		
		#---------------------------------------------------------------
		
		# Pos: 1, 0
		l_localHostName2 = QLabel('Name:')
		
		# Pos: 1, 1
		le_localHostName2 = QLineEdit('Eny')
		le_localHostName2.setReadOnly(True)
		
		# Pos: 1, 2
		l_localHost2 = QLabel('Host:')
		
		# Pos: 1, 3
		le_localHost2 = QLineEdit('0.0.0.0')
		le_localHost2.setReadOnly(True)
		
		#---------------------------------------------------------------
		
		# Add Widgets
		
		# ~ gl_info.setRowStretch(0, 0)
		gl_info.setColumnStretch(0, 0)
		gl_info.setColumnStretch(1, 1)
		gl_info.setColumnStretch(2, 0)
		gl_info.setColumnStretch(3, 1)
		
		gl_info.addWidget(l_localHostName,  0, 0)#, alignment=Qt.AlignRight)
		gl_info.addWidget(le_localHostName, 0, 1, alignment=Qt.AlignLeft)
		gl_info.addWidget(l_localHost,      0, 2)#, alignment=Qt.AlignRight)
		gl_info.addWidget(le_localHost,     0, 3, alignment=Qt.AlignLeft)
		gl_info.addWidget(l_localHostName2,  1, 0)#, alignment=Qt.AlignRight)
		gl_info.addWidget(le_localHostName2, 1, 1, alignment=Qt.AlignLeft)
		gl_info.addWidget(l_localHost2,      1, 2)#, alignment=Qt.AlignRight)
		gl_info.addWidget(le_localHost2,     1, 3, alignment=Qt.AlignLeft)
		
		#---------------------------------------------------------------
		
		# Pos: 0, 0
		# ~ l_localHostName = QLabel('Name:')
		
		# Pos: 0, 1
		# ~ le_localHostName = QLineEdit('Eny')
		# ~ le_localHostName.setReadOnly(True)
		
		# Pos: 0, 2
		# ~ l_localHost = QLabel('Host:')
		
		# Pos: 0, 3
		# ~ le_localHost = QLineEdit('0.0.0.0')
		# ~ le_localHost.setReadOnly(True)
		
		#---------------------------------------------------------------
		
		# Add Widgets
		
		# ~ gl_info.setRowStretch(0, 0)
		# ~ gl_data.setColumnStretch(0, 0)
		# ~ gl_data.setColumnStretch(1, 1)
		# ~ gl_data.setColumnStretch(2, 0)
		# ~ gl_data.setColumnStretch(3, 1)
		
		# ~ gl_data.addWidget(l_localHostName,  0, 0)#, alignment=Qt.AlignRight)
		# ~ gl_data.addWidget(le_localHostName, 0, 1, alignment=Qt.AlignLeft)
		# ~ gl_data.addWidget(l_localHost,      0, 2)#, alignment=Qt.AlignRight)
		# ~ gl_data.addWidget(le_localHost,     0, 3, alignment=Qt.AlignLeft)
		
		#---------------------------------------------------------------
		
		
	def _createActions(self):
		# 'File' Actions
		self.openAction = QAction(QIcon('icons/open.png'), '&Open...', self)
		self.exitAction = QAction(QIcon('icons/exit.png'), '&Exit', self)
		#---------------------------------------------------------------
		# Using Keys
		self.openAction.setShortcut('Ctrl+O')
		self.exitAction.setShortcut('Esc')
		#---------------------------------------------------------------
		# Adding 'File' Tips
		openTip = 'Abre el explorador para cargar archivos.'
		self.openAction.setStatusTip(openTip)							# Agrega un mensaje a la barra de estatus
		self.openAction.setToolTip(openTip)								# Modifica el mensaje de ayuda que aparece encima
	
	def _createMenuBar(self):
		menuBar = self.menuBar()
		# File menu
		fileMenu = QMenu('&File', self)
		menuBar.addMenu(fileMenu)
		fileMenu.addAction(self.openAction)
		fileMenu.addSeparator()
		fileMenu.addAction(self.exitAction)
	
	def _createToolBars(self):
		
		self.fileToolBar = QToolBar('File', self)
		self.addToolBar(Qt.BottomToolBarArea, self.fileToolBar)
		self.fileToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		self.fileToolBar.addAction(self.exitAction)
		self.fileToolBar.addSeparator()
		# ~ self.fileToolBar.addAction(self.openAction)
		self.fileToolBar.setMovable(False)
	
	def _createStatusBar(self):
		self.statusbar = self.statusBar()
		# Adding a temporary message
		self.statusbar.showMessage('Ready', 3000)
		# Adding a permanent message
		t = QTime.currentTime().toPyTime()
		t = '{}:{}'.format(str(t.hour).zfill(2),
						   str(t.minute).zfill(2))
		self.wcLabel = QLabel(t)
		self.statusbar.addPermanentWidget(self.wcLabel)
	
	def contextMenuEvent(self, event):
		# Creating a menu object with the central widget as parent
		menu = QMenu(self)
		# Populating the menu with actions
		menu.addAction(self.openAction)
		menu.addSeparator()
		# Launching the menu
		menu.exec(event.globalPos())
	
	def _connectActions(self):
		
		# Connect File actions
		# ~ self.openAction.triggered.connect(self.openWordList)
		self.exitAction.triggered.connect(self.close)
		
		# Buttons:
		# ~ self.btnOpenFile.clicked.connect(self.openWordList)
		
		# Listwidget:
		# ~ self.tablewidgetUsers.clicked.connect(self.userSelected)
		# ~ self.tablewidgetUsers.doubleClicked.connect(self.bruteForce)
		# ~ self.btnBruteForce.clicked.connect(self.bruteForce)
		# ~ self.btnBruteForceCancel.clicked.connect(self.bruteForceCancel)
		
		# Clock
		self.timer = QTimer()
		self.timer.timeout.connect(self.updateClock)
		self.timer.start(1000)
	
	#===================================================================
	# Functions
	
	def updateClock(self):
		t = datetime.datetime.now().strftime('%H:%M')
		self.wcLabel.setText(t)
	



if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())







