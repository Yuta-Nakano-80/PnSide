import sys
from PySide6 import QtWidgets
from PySide6 import QtGui


class MainWindow(QtWidgets.QMainWindow):
    """
    QMainWindow を継承したカスタムウィンドウクラス。

    self.root_widget / self.root_layout をセットしてある。

    Methods:
        __init__: ウィンドウの初期化。
        set_window: ウィンドウの設定
        set_center: ウィンドウを画面中央に配置

    Examples:
        import sys
        from PySide6 import QtWidgets
        from window import normal_window

        if __name__ == '__main__':

            app = QtWidgets.QApplication(sys.argv)

            # メインウィンドウの作成
            window = normal_window.MainWindow()
            window.show()

            sys.exit(app.exec())
    """

    def __init__(self, window_title='Test Window', width=600, height=300):
        """
        メインウィンドウを初期化します。
        """
        super().__init__()

        self.window_title = window_title
        self.width = width
        self.height = height

        # ルートウィジェット
        self.root_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.root_widget)

        # ルートレイアウト
        self.root_layout = QtWidgets.QVBoxLayout()
        self.root_widget.setLayout(self.root_layout)

        self.set_window()

    def set_window(self):
        """
        ウィンドウ設定
        """
        # ウィンドウの基本設定
        self.setWindowTitle(self.window_title)
        self.resize(self.width, self.height)
        self.set_center()

        self.setStyleSheet(
            'background-color: #363636'
        )

    def set_center(self):
        """
        ウィンドウを画面中央に配置
        """
        # 画面の中央位置を取得
        screen_geometry = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()

        # ウィンドウを画面中央に移動
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    # メインウィンドウの作成
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
