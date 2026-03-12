from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QFrame
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import numpy as np

class PreviewTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        
        # Left Panel: Image Viewer
        self.preview_area = QScrollArea()
        self.preview_area.setWidgetResizable(True)
        self.preview_area.setFrameShape(QFrame.Shape.NoFrame)
        
        self.preview_label = QLabel("Select an image to preview")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_area.setWidget(self.preview_label)
        
        # Right Panel: Info & Histogram
        self.info_panel = QWidget()
        self.info_panel.setFixedWidth(250)
        self.info_layout = QVBoxLayout(self.info_panel)
        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.metadata_label = QLabel("Metadata:\nNone")
        self.info_layout.addWidget(self.metadata_label)
        
        self.histogram_label = QLabel("Histogram Placeholder")
        self.histogram_label.setFixedHeight(150)
        self.histogram_label.setStyleSheet("border: 1px solid #2d2d2d; background: #000000;")
        self.info_layout.addWidget(self.histogram_label)
        
        self.layout.addWidget(self.preview_area, 3)
        self.layout.addWidget(self.info_panel, 1)

    def update_preview(self, image_np):
        """Displays a numpy image array (RGB) in the preview label."""
        if image_np is None:
            return
            
        height, width, channel = image_np.shape
        bytes_per_line = 3 * width
        q_img = QImage(image_np.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        
        # Scale pixmap to fit area
        scaled_pixmap = pixmap.scaled(self.preview_area.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.preview_label.setPixmap(scaled_pixmap)

    def update_metadata(self, metadata):
        text = "Metadata:\n\n"
        for k, v in metadata.items():
            text += f" {k}: {v}\n"
        self.metadata_label.setText(text)
