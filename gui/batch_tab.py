from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QCheckBox, QLineEdit, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

class BatchTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Batch Operations
        self.ops_group = QGroupBox("Batch Operations")
        self.ops_layout = QVBoxLayout(self.ops_group)
        
        self.cb_resize = QCheckBox("Resize images")
        self.cb_contrast = QCheckBox("Auto contrast")
        self.cb_noise = QCheckBox("Remove noise")
        self.cb_grayscale = QCheckBox("Convert to grayscale")
        
        self.ops_layout.addWidget(self.cb_resize)
        self.ops_layout.addWidget(self.cb_contrast)
        self.ops_layout.addWidget(self.cb_noise)
        self.ops_layout.addWidget(self.cb_grayscale)
        
        self.layout.addWidget(self.ops_group)
        
        # Renaming
        self.rename_group = QGroupBox("Renaming Pattern")
        self.rename_layout = QVBoxLayout(self.rename_group)
        
        self.rename_layout.addWidget(QLabel("Pattern (e.g., IMG_{number}.jpg):"))
        self.pattern_input = QLineEdit("IMG_{number}.jpg")
        self.rename_layout.addWidget(self.pattern_input)
        
        self.layout.addWidget(self.rename_group)
        
        # Apply button
        self.btn_apply = QPushButton("APPLY TO QUEUE")
        self.btn_apply.setFixedHeight(40)
        self.layout.addWidget(self.btn_apply)
        
        self.layout.addStretch()
