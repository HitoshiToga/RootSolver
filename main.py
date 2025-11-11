import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTranslator
from ui.main_window import MainWindow


class RootSolver(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.translator = QTranslator()
        self.main_window = MainWindow(self)
        self.main_window.show()
        # Язык по умолчанию
        self.load_language("ru_RU")

    def resource_path(self, relative_path: str) -> str:
        """
        Возвращает корректный путь к файлу, как при запуске из IDE, так и из PyInstaller.
        """
        if hasattr(sys, "_MEIPASS"):
            # при запуске из собранного exe
            base_path = sys._MEIPASS
        else:
            # при обычном запуске из исходников
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def load_language(self, lang_code):
        """Загрузка .qm файла и обновление интерфейса"""
        if not self.translator.isEmpty():
            self.removeTranslator(self.translator)

        qm_path = self.resource_path(f"translations/{lang_code}.qm")
        if self.translator.load(qm_path):
            self.installTranslator(self.translator)
        else:
            print(f"Translation not found: {qm_path}")

        if self.main_window:
            self.main_window.retranslate_ui()


if __name__ == "__main__":
    app = RootSolver(sys.argv)
    sys.exit(app.exec())
