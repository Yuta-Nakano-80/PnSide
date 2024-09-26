import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # タブウィジェットを作成
        self.tab_widget = QTabWidget()

        # タブの位置を左側に設定（縦に並ぶようにする）
        self.tab_widget.setTabPosition(QTabWidget.West)

        # 各タブの内容を作成
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("タブ 1 の内容"))
        tab1.setLayout(tab1_layout)

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("タブ 2 の内容"))
        tab2.setLayout(tab2_layout)

        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("タブ 3 の内容"))
        tab3.setLayout(tab3_layout)

        # タブウィジェットにタブを追加
        self.tab_widget.addTab(tab1, "タブ 1")
        self.tab_widget.addTab(tab2, "タブ 2")
        self.tab_widget.addTab(tab3, "タブ 3")

        # メインレイアウトにタブウィジェットを追加
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

        self.setWindowTitle("縦に並ぶタブウィジェット")
        self.resize(400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
