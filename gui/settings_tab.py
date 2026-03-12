from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QComboBox, QLineEdit, QLabel, QPushButton, QSpinBox
from PyQt6.QtCore import Qt

class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # General Settings
        self.gen_group = QGroupBox("General Settings")
        self.gen_layout = QVBoxLayout(self.gen_group)
        
        self.gen_layout.addWidget(QLabel("Theme:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Dark (Pro)", "Light"])
        self.gen_layout.addWidget(self.theme_combo)
        
        self.gen_layout.addWidget(QLabel("Default Output Folder:"))
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Select folder...")
        self.gen_layout.addWidget(self.path_input)
        
        self.layout.addWidget(self.gen_group)
        
        # Performance
        self.perf_group = QGroupBox("Performance")
        self.perf_layout = QVBoxLayout(self.perf_group)
        
        self.perf_layout.addWidget(QLabel("CPU Threads:"))
        self.threads_spin = QSpinBox()
        self.threads_spin.setRange(1, 32)
        self.threads_spin.setValue(4)
        self.perf_layout.addWidget(self.threads_spin)
        
        self.layout.addWidget(self.perf_group)
        
        # Save Button
        self.btn_save = QPushButton("SAVE SETTINGS")
        self.btn_save.setObjectName("PrimaryButton")
        self.btn_save.setFixedHeight(40)
        self.layout.addWidget(self.btn_save)
        
        self.layout.addStretch()
