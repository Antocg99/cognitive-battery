from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CognitiveBattery(object):
    def setupUi(self, CognitiveBattery):
        # Set the object name and resize the main window
        CognitiveBattery.setObjectName("CognitiveBattery")
        CognitiveBattery.resize(451, 546)
        
        # Create the central widget
        self.centralwidget = QtWidgets.QWidget(CognitiveBattery)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create the main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Create the main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        
        # Create the session info layout
        self.sessionInfoLayout = QtWidgets.QVBoxLayout()
        self.sessionInfoLayout.setObjectName("sessionInfoLayout")
        
        # Add session info text label
        self.sessionInfoText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sessionInfoText.sizePolicy().hasHeightForWidth())
        self.sessionInfoText.setSizePolicy(sizePolicy)
        self.sessionInfoText.setTextFormat(QtCore.Qt.AutoText)
        self.sessionInfoText.setObjectName("sessionInfoText")
        self.sessionInfoLayout.addWidget(self.sessionInfoText)
        
        # Create the session info column layout
        self.sessionInfoColumnLayout = QtWidgets.QHBoxLayout()
        self.sessionInfoColumnLayout.setObjectName("sessionInfoColumnLayout")
        
        # Create the session info label layout
        self.sessionInfoLabelLayout = QtWidgets.QVBoxLayout()
        self.sessionInfoLabelLayout.setObjectName("sessionInfoLabelLayout")
        
        # Add labels for session info
        self.raText = QtWidgets.QLabel(self.centralwidget)
        self.raText.setObjectName("raText")
        self.sessionInfoLabelLayout.addWidget(self.raText)
        
        self.subNumText = QtWidgets.QLabel(self.centralwidget)
        self.subNumText.setObjectName("subNumText")
        self.sessionInfoLabelLayout.addWidget(self.subNumText)
        
        self.conditionText = QtWidgets.QLabel(self.centralwidget)
        self.conditionText.setObjectName("conditionText")
        self.sessionInfoLabelLayout.addWidget(self.conditionText)
        
        self.ageText = QtWidgets.QLabel(self.centralwidget)
        self.ageText.setObjectName("ageText")
        self.sessionInfoLabelLayout.addWidget(self.ageText)
        
        self.sexText = QtWidgets.QLabel(self.centralwidget)
        self.sexText.setObjectName("sexText")
        self.sessionInfoLabelLayout.addWidget(self.sexText)
        
        self.sessionInfoColumnLayout.addLayout(self.sessionInfoLabelLayout)
        
        # Create the session info input layout
        self.sessionInfoInputLayout = QtWidgets.QVBoxLayout()
        self.sessionInfoInputLayout.setObjectName("sessionInfoInputLayout")
        
        # Add input fields for session info
        self.raBox = QtWidgets.QLineEdit(self.centralwidget)
        self.raBox.setObjectName("raBox")
        self.sessionInfoInputLayout.addWidget(self.raBox)
        
        self.subNumBox = QtWidgets.QLineEdit(self.centralwidget)
        self.subNumBox.setObjectName("subNumBox")
        self.sessionInfoInputLayout.addWidget(self.subNumBox)
        
        self.conditionBox = QtWidgets.QLineEdit(self.centralwidget)
        self.conditionBox.setObjectName("conditionBox")
        self.sessionInfoInputLayout.addWidget(self.conditionBox)
        
        self.ageBox = QtWidgets.QLineEdit(self.centralwidget)
        self.ageBox.setObjectName("ageBox")
        self.sessionInfoInputLayout.addWidget(self.ageBox)
        
        # Create the sex layout with radio buttons
        self.sexLayout = QtWidgets.QHBoxLayout()
        self.sexLayout.setContentsMargins(-1, -1, -1, 0)
        self.sexLayout.setObjectName("sexLayout")
        
        self.maleRadio = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maleRadio.sizePolicy().hasHeightForWidth())
        self.maleRadio.setSizePolicy(sizePolicy)
        self.maleRadio.setObjectName("maleRadio")
        self.sexLayout.addWidget(self.maleRadio)
        
        self.femaleRadio = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.femaleRadio.sizePolicy().hasHeightForWidth())
        self.femaleRadio.setSizePolicy(sizePolicy)
        self.femaleRadio.setObjectName("femaleRadio")
        self.sexLayout.addWidget(self.femaleRadio)
        
        self.sessionInfoInputLayout.addLayout(self.sexLayout)
        self.sessionInfoColumnLayout.addLayout(self.sessionInfoInputLayout)
        self.sessionInfoLayout.addLayout(self.sessionInfoColumnLayout)
        self.mainLayout.addLayout(self.sessionInfoLayout)
        
        # Add a horizontal line separator
        self.sessionLine = QtWidgets.QFrame(self.centralwidget)
        self.sessionLine.setLineWidth(1)
        self.sessionLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.sessionLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sessionLine.setObjectName("sessionLine")
        self.mainLayout.addWidget(self.sessionLine)
        
        # Create the battery layout
        self.batteryLayout = QtWidgets.QVBoxLayout()
        self.batteryLayout.setObjectName("batteryLayout")
        
        # Add battery select text label
        self.batterySelectText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batterySelectText.sizePolicy().hasHeightForWidth())
        self.batterySelectText.setSizePolicy(sizePolicy)
        self.batterySelectText.setScaledContents(True)
        self.batterySelectText.setObjectName("batterySelectText")
        self.batteryLayout.addWidget(self.batterySelectText)
        
        # Create the task order layout
        self.taskOrderLayout = QtWidgets.QHBoxLayout()
        self.taskOrderLayout.setContentsMargins(-1, -1, -1, 10)
        self.taskOrderLayout.setObjectName("taskOrderLayout")
        
        # Add reorder text label
        self.reorderText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.reorderText.setFont(font)
        self.reorderText.setObjectName("reorderText")
        self.taskOrderLayout.addWidget(self.reorderText)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.taskOrderLayout.addItem(spacerItem)
        
        # Add random order checkbox
        self.randomOrderCheck = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.randomOrderCheck.sizePolicy().hasHeightForWidth())
        self.randomOrderCheck.setSizePolicy(sizePolicy)
        self.randomOrderCheck.setChecked(False)
        self.randomOrderCheck.setObjectName("randomOrderCheck")
        self.taskOrderLayout.addWidget(self.randomOrderCheck)
        self.batteryLayout.addLayout(self.taskOrderLayout)
        
        # Create the selection layout
        self.selectionLayout = QtWidgets.QHBoxLayout()
        self.selectionLayout.setContentsMargins(-1, -1, -1, 10)
        self.selectionLayout.setObjectName("selectionLayout")
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.selectionLayout.addItem(spacerItem1)
        
        # Add select all and deselect all buttons
        self.selectAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectAllButton.setObjectName("selectAllButton")
        self.selectionLayout.addWidget(self.selectAllButton)
        
        self.deselectAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.deselectAllButton.setObjectName("deselectAllButton")
        self.selectionLayout.addWidget(self.deselectAllButton)
        self.batteryLayout.addLayout(self.selectionLayout)
        
        # Create the task list layout
        self.taskListLayout = QtWidgets.QHBoxLayout()
        self.taskListLayout.setContentsMargins(-1, -1, -1, 0)
        self.taskListLayout.setObjectName("taskListLayout")
        
        # Add the task list widget
        self.taskList = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taskList.setFont(font)
        self.taskList.setProperty("showDropIndicator", False)
        self.taskList.setDragEnabled(True)
        self.taskList.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.taskList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.taskList.setAlternatingRowColors(True)
        self.taskList.setMovement(QtWidgets.QListView.Snap)
        self.taskList.setObjectName("taskList")
        
        # Add items to the task list
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)

        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        
        """
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        """
        self.taskList.addItem(item)
        self.taskListLayout.addWidget(self.taskList)
        
        # Create the reorder button layout
        self.reorderButtonLayout = QtWidgets.QVBoxLayout()
        self.reorderButtonLayout.setContentsMargins(0, -1, -1, -1)
        self.reorderButtonLayout.setSpacing(6)
        self.reorderButtonLayout.setObjectName("reorderButtonLayout")
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.reorderButtonLayout.addItem(spacerItem2)
        
        # Add up and down buttons for reordering tasks
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.upButton.setObjectName("upButton")
        self.reorderButtonLayout.addWidget(self.upButton)
        
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.downButton.setObjectName("downButton")
        self.reorderButtonLayout.addWidget(self.downButton)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.reorderButtonLayout.addItem(spacerItem3)
        self.taskListLayout.addLayout(self.reorderButtonLayout)
        self.batteryLayout.addLayout(self.taskListLayout)
        self.mainLayout.addLayout(self.batteryLayout)
        
        # Create the save/load layout
        self.saveLoadLayout = QtWidgets.QHBoxLayout()
        self.saveLoadLayout.setObjectName("saveLoadLayout")
        
        # Add start and cancel buttons
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.saveLoadLayout.addWidget(self.startButton)
        
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.saveLoadLayout.addWidget(self.cancelButton)
        self.mainLayout.addLayout(self.saveLoadLayout)
        self.verticalLayout.addLayout(self.mainLayout)
        
        # Set the central widget
        CognitiveBattery.setCentralWidget(self.centralwidget)
        
        # Create the menu bar
        self.menubar = QtWidgets.QMenuBar(CognitiveBattery)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        
        # Create the file menu
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        # Create the help menu
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        
        # Create the options menu
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        CognitiveBattery.setMenuBar(self.menubar)
        
        # Create the status bar
        self.statusbar = QtWidgets.QStatusBar(CognitiveBattery)
        self.statusbar.setObjectName("statusbar")
        CognitiveBattery.setStatusBar(self.statusbar)
        
        # Create actions for the menu items
        self.actionSettings = QtWidgets.QAction(CognitiveBattery)
        self.actionSettings.setObjectName("actionSettings")
        
        self.actionExit = QtWidgets.QAction(CognitiveBattery)
        self.actionExit.setObjectName("actionExit")
        
        self.actionDocumentation = QtWidgets.QAction(CognitiveBattery)
        self.actionDocumentation.setObjectName("actionDocumentation")
        
        self.actionLicense = QtWidgets.QAction(CognitiveBattery)
        self.actionLicense.setObjectName("actionLicense")
        
        self.actionContribute = QtWidgets.QAction(CognitiveBattery)
        self.actionContribute.setObjectName("actionContribute")
        
        self.actionBrowse_Issues = QtWidgets.QAction(CognitiveBattery)
        self.actionBrowse_Issues.setObjectName("actionBrowse_Issues")
        
        self.actionReport_Bug = QtWidgets.QAction(CognitiveBattery)
        self.actionReport_Bug.setObjectName("actionReport_Bug")
        
        self.actionRequest_Feature = QtWidgets.QAction(CognitiveBattery)
        self.actionRequest_Feature.setObjectName("actionRequest_Feature")
        
        self.actionAbout = QtWidgets.QAction(CognitiveBattery)
        self.actionAbout.setObjectName("actionAbout")
        
        self.actionAnalysis = QtWidgets.QAction(CognitiveBattery)
        self.actionAnalysis.setEnabled(False)
        self.actionAnalysis.setObjectName("actionAnalysis")
        
        self.actionCheck_for_updates = QtWidgets.QAction(CognitiveBattery)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        
        # Add actions to the file menu
        self.menuFile.addAction(self.actionExit)
        
        # Add actions to the help menu
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContribute)
        self.menuHelp.addAction(self.actionBrowse_Issues)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addAction(self.actionRequest_Feature)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addAction(self.actionAbout)
        
        # Add actions to the options menu
        self.menuOptions.addAction(self.actionSettings)
        
        # Add menus to the menu bar
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # Retranslate the UI
        self.retranslateUi(CognitiveBattery)
        
        # Connect slots by name
        QtCore.QMetaObject.connectSlotsByName(CognitiveBattery)

    def retranslateUi(self, CognitiveBattery):
        _translate = QtCore.QCoreApplication.translate
        CognitiveBattery.setWindowTitle(_translate("CognitiveBattery", "Cognitive Battery"))

        # Set text for session information labels and input fields
        self.sessionInfoText.setText(_translate("CognitiveBattery", "<html><head/><body><p><span style=\" font-weight:600;\">Session information:</span></p></body></html>"))
        self.raText.setText(_translate("CognitiveBattery", "Research Assistant:"))
        self.subNumText.setText(_translate("CognitiveBattery", "Subject #:"))
        self.conditionText.setText(_translate("CognitiveBattery", "Condition:"))
        self.ageText.setText(_translate("CognitiveBattery", "Age:"))
        self.sexText.setText(_translate("CognitiveBattery", "Sex:"))
        
        # Set status tips for input fields
        self.raBox.setStatusTip(_translate("CognitiveBattery", "Enter name of the research assistant"))
        self.subNumBox.setStatusTip(_translate("CognitiveBattery", "Enter the subject number or ID"))
        self.conditionBox.setStatusTip(_translate("CognitiveBattery", "Enter the current condition"))
        self.ageBox.setStatusTip(_translate("CognitiveBattery", "Enter the participant's age"))
        
        # Set text for sex radio buttons
        self.maleRadio.setText(_translate("CognitiveBattery", "Male"))
        self.femaleRadio.setText(_translate("CognitiveBattery", "Female"))
        
        # Set text for task selection labels and buttons
        self.batterySelectText.setText(_translate("CognitiveBattery", "<html><head/><body><p><span style=\" font-weight:600;\">Task selection:</span></p></body></html>"))
        self.reorderText.setText(_translate("CognitiveBattery", "(use the Up/Down buttons to set the task order)"))
        self.randomOrderCheck.setStatusTip(_translate("CognitiveBattery", "Run tasks in a random order"))
        self.randomOrderCheck.setText(_translate("CognitiveBattery", "Random order"))
        self.selectAllButton.setStatusTip(_translate("CognitiveBattery", "Select all tasks"))
        self.selectAllButton.setText(_translate("CognitiveBattery", "Select All"))
        self.deselectAllButton.setStatusTip(_translate("CognitiveBattery", "Deselect all tasks"))
        self.deselectAllButton.setText(_translate("CognitiveBattery", "Deselect All"))
        
        # Disable sorting while setting text for task list items
        __sortingEnabled = self.taskList.isSortingEnabled()
        self.taskList.setSortingEnabled(False)
        
        # Set text for each task in the task list
        item = self.taskList.item(0)
        item.setText(_translate("CognitiveBattery", "Bouncing Ball"))

        item = self.taskList.item(1)
        item.setText(_translate("CognitiveBattery", "Attention Network Test (ANT)"))
        
        item = self.taskList.item(2)
        item.setText(_translate("CognitiveBattery", "Digit Span (backwards)"))
        
        item = self.taskList.item(3)
        item.setText(_translate("CognitiveBattery", "Sternberg Task"))
        
        # Re-enable sorting
        self.taskList.setSortingEnabled(__sortingEnabled)
        
        # Set status tips and text for reorder buttons
        self.upButton.setStatusTip(_translate("CognitiveBattery", "Move selected task up in order of administration"))
        self.upButton.setText(_translate("CognitiveBattery", "Up"))
        self.downButton.setStatusTip(_translate("CognitiveBattery", "Move selected task down in order of administration"))
        self.downButton.setText(_translate("CognitiveBattery", "Down"))
        
        # Set status tips and text for start and cancel buttons
        self.startButton.setStatusTip(_translate("CognitiveBattery", "Start the testing session"))
        self.startButton.setText(_translate("CognitiveBattery", "Start"))
        self.cancelButton.setStatusTip(_translate("CognitiveBattery", "Quit the battery"))
        self.cancelButton.setText(_translate("CognitiveBattery", "Cancel"))
        
        # Set titles for menu items
        self.menuFile.setTitle(_translate("CognitiveBattery", "File"))
        self.menuHelp.setTitle(_translate("CognitiveBattery", "Help"))
        self.menuOptions.setTitle(_translate("CognitiveBattery", "Options"))
        
        # Set text and status tips for menu actions
        self.actionSettings.setText(_translate("CognitiveBattery", "Settings"))
        self.actionSettings.setStatusTip(_translate("CognitiveBattery", "Change battery settings"))
        self.actionExit.setText(_translate("CognitiveBattery", "Exit"))
        self.actionExit.setStatusTip(_translate("CognitiveBattery", "Exit the battery"))
        self.actionDocumentation.setText(_translate("CognitiveBattery", "Documentation"))
        self.actionDocumentation.setStatusTip(_translate("CognitiveBattery", "Visit the GitHub support page"))
        self.actionLicense.setText(_translate("CognitiveBattery", "License"))
        self.actionLicense.setStatusTip(_translate("CognitiveBattery", "View application license"))
        self.actionContribute.setText(_translate("CognitiveBattery", "Contribute"))
        self.actionContribute.setStatusTip(_translate("CognitiveBattery", "Contribute code on GitHub"))
        self.actionBrowse_Issues.setText(_translate("CognitiveBattery", "Browse Issues"))
        self.actionBrowse_Issues.setStatusTip(_translate("CognitiveBattery", "Browse known bugs and issues"))
        self.actionReport_Bug.setText(_translate("CognitiveBattery", "Report Bug"))
        self.actionReport_Bug.setStatusTip(_translate("CognitiveBattery", "Report a bug"))
        self.actionRequest_Feature.setText(_translate("CognitiveBattery", "Request Feature"))
        self.actionRequest_Feature.setStatusTip(_translate("CognitiveBattery", "Request a feature"))
        self.actionAbout.setText(_translate("CognitiveBattery", "About"))
        self.actionAbout.setStatusTip(_translate("CognitiveBattery", "About the battery"))
        self.actionAnalysis.setText(_translate("CognitiveBattery", "Analysis"))
        self.actionAnalysis.setStatusTip(_translate("CognitiveBattery", "Calculate aggregate data for all tasks"))
        self.actionCheck_for_updates.setText(_translate("CognitiveBattery", "Check for updates"))
        self.actionCheck_for_updates.setStatusTip(_translate("CognitiveBattery", "Check for new releases of the battery"))