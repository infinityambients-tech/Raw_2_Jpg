from PyQt6.QtWidgets import QSplashScreen, QProgressBar, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QFont

class ProfessionalSplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        
        # Set window flags
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        
        # Create a widget for the layout
        self.container = QWidget(self)
        self.layout = QVBoxLayout(self.container)
        
        # Logo (placeholder if not found)
        self.logo_label = QLabel("RAW2JPG Studio v2")
        self.logo_label.setStyleSheet("color: #00c8ff; font-size: 32px; font-weight: bold;")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logo_label)
        
        # Status Label
        self.status_label = QLabel("Initializing engine...")
        self.status_label.setStyleSheet("color: #ffffff; font-size: 14px;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.status_label)
        
        # Progress Bar
        self.progress = QProgressBar()
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #1b1b22;
                border-radius: 5px;
                text-align: center;
                background-color: #0f0f12;
                color: #ffffff;
            }
            QProgressBar::chunk {
                background-color: #00c8ff;
                width: 10px;
            }
        """)
        self.progress.setFixedSize(400, 20)
        self.layout.addWidget(self.progress)
        
        # Style the container
        self.container.setStyleSheet("background-color: #0f0f12; border: 1px solid #2d2d2d; border-radius: 10px;")
        self.container.setFixedSize(500, 300)
        self.setFixedSize(500, 300)

    def set_progress(self, value, message):
        self.progress.setValue(value)
        self.status_label.setText(message)
        self.repaint()
