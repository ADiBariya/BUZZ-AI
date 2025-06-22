# frontend_gui.py
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QMessageBox, QHBoxLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from model.pipeline import generate, load_pipeline

MODEL_PATH = r"C:\Users\ahira\BUZZ-AI\models\AnythingXL_xl.safetensors"
#upload it according to you and also change model path according to your wish!

class BuzzAIGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BUZZ-AI ImageGen")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")

        self.image_path = None
        self.init_ui()

        # Load model pipeline
        load_pipeline(MODEL_PATH)

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("BUZZ-AI: Anime Image Generator")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(self.title)

        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Enter prompt (e.g., anime girl in rain)...")
        self.prompt_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.prompt_input)

        btn_layout = QHBoxLayout()

        self.generate_btn = QPushButton("🎨 Generate")
        self.generate_btn.clicked.connect(self.generate_image)
        self.generate_btn.setStyleSheet("background-color: #03DAC6; padding: 10px;")
        btn_layout.addWidget(self.generate_btn)

        self.save_btn = QPushButton("💾 Save")
        self.save_btn.clicked.connect(self.save_image)
        self.save_btn.setEnabled(False)
        self.save_btn.setStyleSheet("background-color: #BB86FC; padding: 10px;")
        btn_layout.addWidget(self.save_btn)

        layout.addLayout(btn_layout)

        self.image_label = QLabel("Image will appear here")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 1px dashed gray; padding: 20px;")
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def generate_image(self):
        prompt = self.prompt_input.text().strip()
        if not prompt:
            QMessageBox.warning(self, "Missing Prompt", "Please enter a prompt!")
            return

        self.image_label.setText("Generating image...")
        QApplication.processEvents()

        try:
            path = generate(prompt)
            self.image_path = path
            pixmap = QPixmap(path).scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.save_btn.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Generation Error", str(e))

    def save_image(self):
        if self.image_path:
            save_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "buzz_output.png", "PNG Files (*.png)")
            if save_path:
                try:
                    os.replace(self.image_path, save_path)
                    QMessageBox.information(self, "Saved", f"Image saved to:\n{save_path}")
                except Exception as e:
                    QMessageBox.critical(self, "Save Error", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BuzzAIGui()
    window.show()
    sys.exit(app.exec())
