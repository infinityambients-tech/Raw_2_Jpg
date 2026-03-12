from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QLabel, QStatusBar
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from gui.library_tab import LibraryTab
from gui.preview_tab import PreviewTab
from gui.convert_tab import ConvertTab
from gui.batch_tab import BatchTab
from gui.settings_tab import SettingsTab
from core.raw_converter import get_raw_preview, convert_raw_to_jpg
from core.metadata_reader import get_metadata
import os

class ConversionWorker(QThread):
    progress = pyqtSignal(int, str)
    finished = pyqtSignal()

    def __init__(self, files, output_dir, quality, resize):
        super().__init__()
        self.files = files
        self.output_dir = output_dir
        self.quality = quality
        self.resize = resize

    def run(self):
        total = len(self.files)
        for i, file_path in enumerate(self.files):
            filename = os.path.basename(file_path)
            output_name = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(self.output_dir, output_name)
            
            self.progress.emit(int((i / total) * 100), f"Converting {filename}...")
            
            success, error = convert_raw_to_jpg(file_path, output_path, self.quality, self.resize)
            if not success:
                print(f"Error converting {filename}: {error}")
        
        self.progress.emit(100, "Done.")
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAW2JPG Studio v2")
        self.resize(1200, 800)
        
        # Central Widget and Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # Header / Navigation
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)
        
        # Instantiate Tabs
        self.library_tab = LibraryTab(self)
        self.convert_tab = ConvertTab()
        self.preview_tab = PreviewTab()
        self.batch_tab = BatchTab()
        self.settings_tab = SettingsTab()
        
        self.tabs.addTab(self.library_tab, "Library")
        self.tabs.addTab(self.convert_tab, "Convert")
        self.tabs.addTab(self.preview_tab, "Preview")
        self.tabs.addTab(self.batch_tab, "Batch Tools")
        self.tabs.addTab(self.settings_tab, "Settings")
        
        # Connect Signals
        self.library_tab.file_list.clicked.connect(self.handle_file_selected)
        self.convert_tab.btn_start.clicked.connect(self.start_conversion)
        self.convert_tab.btn_add.clicked.connect(self.add_folder_to_queue)
        self.convert_tab.btn_clear.clicked.connect(self.clear_queue)
        
        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        self.status_label_files = QLabel("Files: 0")
        self.status_label_cpu = QLabel("CPU: Auto")
        self.status_bar.addPermanentWidget(self.status_label_files)
        self.status_bar.addPermanentWidget(self.status_label_cpu)

    def handle_file_selected(self, index):
        path = self.library_tab.file_model.filePath(index)
        if os.path.isfile(path):
            # Update Preview
            preview_img = get_raw_preview(path)
            if preview_img is not None:
                self.preview_tab.update_preview(preview_img)
                
            # Update Metadata
            metadata = get_metadata(path)
            self.preview_tab.update_metadata(metadata)

    def add_folder_to_queue(self):
        from PyQt6.QtWidgets import QFileDialog
        folder = QFileDialog.getExistingDirectory(self, "Select Folder with RAW files")
        if folder:
            from core.raw_scanner import scan_directory
            files = scan_directory(folder)
            for file in files:
                self.convert_tab.file_list.addItem(file)
            self.status_label_files.setText(f"Files: {self.convert_tab.file_list.count()}")
            self.status_bar.showMessage(f"Added {len(files)} files to queue.")

    def clear_queue(self):
        self.convert_tab.file_list.clear()
        self.status_label_files.setText("Files: 0")
        self.status_bar.showMessage("Queue cleared.")

    def start_conversion(self):
        # Gather info from UI
        quality = self.convert_tab.quality_spin.value()
        resize = (1920, 1080) if self.convert_tab.resize_check.isChecked() else None
        
        # Get files from Queue List
        files = []
        for i in range(self.convert_tab.file_list.count()):
            files.append(self.convert_tab.file_list.item(i).text())
        
        if not files:
            self.status_bar.showMessage("No files in queue! Use 'Add Folder' or select from Library.")
            return
            
        output_dir = self.settings_tab.path_input.text() or os.path.join(os.path.dirname(files[0]), "Export")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        # Start Worker
        self.worker = ConversionWorker(files, output_dir, quality, resize)
        self.worker.progress.connect(self.update_conversion_progress)
        self.worker.finished.connect(lambda: self.status_bar.showMessage("Conversion Finished!"))
        self.worker.start()

    def update_conversion_progress(self, val, msg):
        self.convert_tab.progress_bar.setValue(val)
        self.status_bar.showMessage(msg)
