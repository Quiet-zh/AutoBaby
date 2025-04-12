from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoBaby")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("点击我", self)
        self.button.clicked.connect(self.on_click)  # type: ignore

    def on_click(self, checked: bool):
        print("按钮被点击！")

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()