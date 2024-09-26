import sys
from PySide6 import QtWidgets
from window import normal_window


class BasePushButton(QtWidgets.QPushButton):
    """
    ベースになるプッシュボタン
    """

    def __init__(self, text='', width=200, height=40, *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        self.text = text
        self.width = width
        self.height = height

        self.background_color = '#595959'
        self.hover_background_color = '#696969'
        self.pressed_background_color = '#4F4F4F'
        self.disabled_background_color = '#595959'

        self.border_color = '#999999'
        self.hover_border_color = '#A6A6A6'
        self.disabled_border_color = '#5E5E5E'

        self.font_color = 'white'
        self.disabled_font_color = '#999999'
        self.padding = '10px'
        self.border_radius = int
        self.border_width = '2px'

        self.set_style()

    def set_style(self):
        """

        スタイルのセット

        """
        self.border_radius = str(self.height / 2)

        self.set_qss()
        self.setFixedSize(self.width, self.height)

    def set_qss(self):
        """

        QSS の設定

        """
        qss = f"""
        QPushButton {{
            background-color: {self.background_color};
            color: {self.font_color};
            border: {self.border_width} solid {self.border_color};
            padding: {self.padding};
            border-radius: {self.border_radius};
        }}

        QPushButton:hover {{
            background-color: {self.hover_background_color};
            border: {self.border_width} solid {self.hover_border_color};
        }}

        QPushButton:pressed {{
            background-color: {self.pressed_background_color};
        }}

        QPushButton:disabled {{
            background-color: {self.disabled_background_color};
            color: {self.disabled_font_color};
            border-color: {self.disabled_border_color};
        }}
        """

        self.setStyleSheet(qss)


def test():
    """

    テストの実行関数

    """
    app = QtWidgets.QApplication(sys.argv)

    # メインウィンドウの作成
    window = normal_window.MainWindow()

    root_layout = window.root_layout
    push_button = BasePushButton('テスト')
    root_layout.addWidget(push_button)

    disabled_push_button = BasePushButton('テスト')
    disabled_push_button.setEnabled(False)
    root_layout.addWidget(disabled_push_button)

    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    test()
