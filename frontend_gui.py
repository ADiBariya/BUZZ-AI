import os
import sys
import threading
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QLineEdit, QMessageBox, QFileDialog, QHBoxLayout, QProgressBar
)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt, QTimer

from model.pipeline import generate, load_pipeline

MODEL_PATH = r"C:\Users\ahira\BUZZ-AI\models\AnythingXL_xl.safetensors" #change this according to your path!!

class BuzzImageGenApp(QWidget):
    def __init__(self):
        super().__init__()

        self.model_loaded = False

        # GUI setup
        self.setWindowTitle("🚀 BUZZ AI - Image Generator")
        self.setFixedSize(512, 640)
        self.setStyleSheet("""QWidget { background-color: #1e1e1e; color: #ffffff; font-family: 'Segoe UI'; }
        QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 6px; }
        QPushButton:hover { background-color: #45a049; }
        QLineEdit { padding: 10px; font-size: 14px; border-radius: 4px; border: 1px solid #555; background-color: #2d2d2d; color: #fff; }
        QLabel { font-size: 13px; }""")

        layout = QVBoxLayout()

        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("💡 Enter your prompt here...")
        layout.addWidget(self.prompt_input)

        self.generate_button = QPushButton("🎨 Generate Image")
        self.generate_button.clicked.connect(self.generate_image)
        layout.addWidget(self.generate_button)

        self.progress = QProgressBar()
        self.progress.setMaximum(0)
        self.progress.setMinimum(0)
        self.progress.setVisible(False)
        layout.addWidget(self.progress)

        self.image_label = QLabel("🔍 Generated image will appear here")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.download_button = QPushButton("⬇️ Open in Folder")
        self.download_button.setVisible(False)
        self.download_button.clicked.connect(self.open_in_folder)
        layout.addWidget(self.download_button)

        self.setLayout(layout)
        self.last_image_path = None

        # Load model in background
        QTimer.singleShot(500, self.load_model_async)

    def load_model_async(self):
        def _load():
            load_pipeline(MODEL_PATH)
            self.model_loaded = True
            QTimer.singleShot(0, lambda: QMessageBox.information(self, "BUZZ AI", "✅ Model Loaded Successfully!"))
        threading.Thread(target=_load, daemon=True).start()

    def generate_image(self):
        if not self.model_loaded:
            QMessageBox.warning(self, "Model Loading", "🚧 Model is still loading. Please wait.")
            return

        prompt = self.prompt_input.text().strip()
        if not prompt:
            QMessageBox.warning(self, "No Prompt", "Please enter a prompt to generate an image.")
            return

        self.progress.setVisible(True)
        self.image_label.setText("⏳ Generating... Please wait...")
        self.download_button.setVisible(False)

        threading.Thread(target=self._generate_image_thread, args=(prompt,), daemon=True).start()

    def _generate_image_thread(self, prompt):
        try:
            path = generate(prompt)
            self.last_image_path = path
            self.show_generated_image(path)
        except Exception as e:
            self.image_label.setText("❌ Failed to generate image.")
            QTimer.singleShot(0, lambda: QMessageBox.critical(self, "Error", f"An error occurred:\n{e}"))
        finally:
            QTimer.singleShot(0, lambda: self.progress.setVisible(False))

    def show_generated_image(self, path):
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToWidth(460, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.download_button.setVisible(True)

    def open_in_folder(self):
        if self.last_image_path:
            folder = os.path.dirname(self.last_image_path)
            os.startfile(folder)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BuzzImageGenApp()
    window.show()
    sys.exit(app.exec())
