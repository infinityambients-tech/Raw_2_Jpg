import sys
import os
import time
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from gui.main_window import MainWindow
from gui.splash_screen import ProfessionalSplashScreen

def main():
    app = QApplication(sys.argv)
    
    # Apply global theme
    try:
        qss_path = os.path.join(os.path.dirname(__file__), 'styles', 'dark_theme.qss')
        with open(qss_path, 'r') as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        print(f"Could not load stylesheet: {e}")
    
    # Show Splash Screen
    splash = ProfessionalSplashScreen()
    splash.show()
    
    # Simulate loading process
    steps = [
        (20, "Loading UI components..."),
        (40, "Initializing RAW engine..."),
        (60, "Scanning extensions..."),
        (80, "Ready to launch..."),
        (100, "Finished.")
    ]
    
    def run_loading(index=0):
        if index < len(steps):
            progress, message = steps[index]
            splash.set_progress(progress, message)
            QTimer.singleShot(500, lambda: run_loading(index + 1))
        else:
            # Launch Main Window
            window = MainWindow()
            window.show()
            splash.finish(window)
            # Keep a reference to the window
            app._window = window

    QTimer.singleShot(500, lambda: run_loading(0))
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
