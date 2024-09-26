import os
import importlib
import inspect


def load_classes_from_test_directory():
    """
    'test' ディレクトリ内のすべての Python ファイルからクラスを動的に読み込み、クラス名で
    グローバルにアクセス可能にします。

    この関数は 'test' ディレクトリ内のすべての `.py` ファイル（`__init__.py` を除く）を検索し、
    各モジュールをインポートして、定義されているクラスを取得します。インポートされたクラスは
    グローバル名前空間に追加され、クラス名で直接アクセスできるようになります。

    Raises:
        ImportError: モジュールのインポートに問題がある場合に発生します。
        FileNotFoundError: 'test' ディレクトリが存在しない場合に発生します。

    例:
        例えば、'test' ディレクトリに `example.py` というファイルがあり、そこに `MyClass`
        というクラスが定義されている場合:

        ```
        test/
        ├── example.py
        ```

        `load_classes_from_test_directory()` を呼び出した後、`MyClass` を次のようにインスタンス化できます:

        ```python
        my_instance = MyClass()
        ```
    """
    # 'test' ディレクトリのパスを指定
    test_directory = os.path.join(os.path.dirname(__file__), 'test')

    # test ディレクトリ内のすべての .py ファイルをリスト化
    for filename in os.listdir(test_directory):
        if filename.endswith(".py") and filename != "__init__.py":
            # ファイル名から拡張子を除去してモジュール名に変換
            module_name = filename[:-3]

            # モジュールを動的にインポート
            module = importlib.import_module(f"test.{module_name}")

            # モジュール内のクラスを取得し、グローバルに登録
            for name, obj in inspect.getmembers(module, inspect.isclass):
                globals()[name] = obj