from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTreeView, QListView, QFileSystemModel, QSplitter
from PyQt6.QtCore import Qt, QDir

class LibraryTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QHBoxLayout(self)
        
        # Splitter for adjustable panels
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left: Folder Tree
        self.tree_model = QFileSystemModel()
        self.tree_model.setRootPath(QDir.rootPath())
        self.tree_model.setFilter(QDir.Filter.AllDirs | QDir.Filter.NoDotAndDotDot)
        
        self.folder_tree = QTreeView()
        self.folder_tree.setModel(self.tree_model)
        self.folder_tree.setHeaderHidden(True)
        # Hide columns except first one
        for i in range(1, 4):
            self.folder_tree.setColumnHidden(i, True)
        
        self.folder_tree.clicked.connect(self.on_folder_selected)
        
        # Right: File List
        self.file_model = QFileSystemModel()
        self.file_list = QListView()
        self.file_list.setModel(self.file_model)
        # Only show supported RAW files (we'll set filtering in on_folder_selected)
        
        self.file_list.clicked.connect(self.on_file_selected)
        
        self.splitter.addWidget(self.folder_tree)
        self.splitter.addWidget(self.file_list)
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 2)
        
        self.layout.addWidget(self.splitter)

    def on_folder_selected(self, index):
        path = self.tree_model.filePath(index)
        self.file_model.setRootPath(path)
        self.file_list.setRootIndex(self.file_model.index(path))
        # Filter for RAW files (hardcoded extensions for simple demo)
        self.file_model.setNameFilters(["*.CR2", "*.CR3", "*.NEF", "*.ARW", "*.RAF", "*.DNG"])
        self.file_model.setNameFilterDisables(False)

    def on_file_selected(self, index):
        path = self.file_model.filePath(index)
        if hasattr(self.main_window, 'preview_tab'):
            # Emit signal or call method to update preview
            pass
