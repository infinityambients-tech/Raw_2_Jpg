from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QProgressBar, QLabel, QGroupBox, QSpinBox, QCheckBox
from PyQt6.QtCore import Qt

class ConvertTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        
        # Left: Queue List
        self.queue_group = QGroupBox("Conversion Queue")
        self.queue_layout = QVBoxLayout(self.queue_group)
        
        self.file_list = QListWidget()
        self.queue_layout.addWidget(self.file_list)
        
        self.btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Add Folder")
        self.btn_clear = QPushButton("Clear Queue")
        self.btn_layout.addWidget(self.btn_add)
        self.btn_layout.addWidget(self.btn_clear)
        self.queue_layout.addLayout(self.btn_layout)
        
        # Right: Settings & Status
        self.settings_group = QGroupBox("Export Settings")
        self.settings_layout = QVBoxLayout(self.settings_group)
        self.settings_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.settings_layout.addWidget(QLabel("Output Quality:"))
        self.quality_spin = QSpinBox()
        self.quality_spin.setRange(1, 100)
        self.quality_spin.setValue(95)
        self.settings_layout.addWidget(self.quality_spin)
        
        self.resize_check = QCheckBox("Resize Images")
        self.settings_layout.addWidget(self.resize_check)
        
        self.settings_layout.addStretch()
        
        self.btn_start = QPushButton("START CONVERSION")
        self.btn_start.setObjectName("PrimaryButton")
        self.btn_start.setFixedHeight(50)
        self.settings_layout.addWidget(self.btn_start)
        
        self.progress_bar = QProgressBar()
        self.settings_layout.addWidget(self.progress_bar)
        
        self.layout.addWidget(self.queue_group, 2)
        self.layout.addWidget(self.settings_group, 1)
