import sys
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

    def load_language(self, lang_code):
        """Загрузка .qm файла и обновление интерфейса"""
        if not self.translator.isEmpty():
            self.removeTranslator(self.translator)

        if self.translator.load(f"translations/{lang_code}.qm"):
            self.installTranslator(self.translator)

        if self.main_window:
            self.main_window.retranslate_ui()

if __name__ == "__main__":
    app = RootSolver(sys.argv)
    sys.exit(app.exec())
