import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt

class PixelViewerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pixel Viewer")

        # Image label to display your image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Labels to show coordinates
        self.x_label = QLabel("X: ")
        self.y_label = QLabel("Y: ")

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.image_label, 0, 0, 1, 2)  # Image takes up the top
        layout.addWidget(self.x_label, 1, 0)
        layout.addWidget(self.y_label, 1, 1)
        self.setLayout(layout)

        # Connect the mouse move event
        self.image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.update_coordinates

    def load_image(self, image_path):
        self.pixmap = QPixmap(image_path)
        self.image_label.setPixmap(self.pixmap)

    def update_coordinates(self, event):
        x = event.x()
        y = event.y()
        self.x_label.setText("X: {}".format(x))
        self.y_label.setText("Y: {}".format(y))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixelViewerWindow()

    # Example usage:
    window.load_image("Your image path here")  # Replace with your image path

    window.show()
    sys.exit(app.exec_())
