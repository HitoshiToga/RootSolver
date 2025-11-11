from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from core.math_engine import compute_root
from core.utils import show_error

class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app  # RootSolver QApplication

        # Хранение последнего вычисления
        self.last_value = None
        self.last_degree = None
        self.last_result = None

        self.setWindowTitle(self.tr("RootSolver — Калькулятор корней"))
        self.resize(400, 250)

        # Поля ввода
        self.input_value = QLineEdit()
        self.input_value.setPlaceholderText(self.tr("Введите число"))

        self.input_degree = QLineEdit()
        self.input_degree.setPlaceholderText(self.tr("Введите степень (по умолчанию 2)"))

        # Кнопка вычислить
        self.btn_calc = QPushButton(self.tr("Вычислить"))

        # Метка для результата
        self.result = QLabel(self.tr("Результат появится здесь"))

        # Селектор языка
        self.lang_selector = QComboBox()
        self.lang_selector.addItems(["Русский", "English", "Español", "中文"])
        self.lang_selector.currentIndexChanged.connect(self.change_language)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_value)
        layout.addWidget(self.input_degree)
        layout.addWidget(self.btn_calc)
        layout.addWidget(self.result)
        layout.addWidget(self.lang_selector)
        self.setLayout(layout)

        # Сигналы
        self.btn_calc.clicked.connect(self.calculate_root)

    def calculate_root(self):
        try:
            value = float(self.input_value.text())
            degree_text = self.input_degree.text()
            degree = int(degree_text) if degree_text else 2
            result = compute_root(value, degree)

            # Сохраняем данные для перевода
            self.last_value = value
            self.last_degree = degree
            self.last_result = result

            self.update_result_text()
        except Exception as e:
            show_error(str(e))

    def update_result_text(self):
        """Обновляем текст результата с учётом текущего языка"""
        if self.last_value is not None:
            self.result.setText(self.tr("{degree}-й корень из {value} = {result}").format(
                degree=self.last_degree,
                value=self.last_value,
                result=self.last_result
            ))
        else:
            self.result.setText(self.tr("Результат появится здесь"))

    def change_language(self):
        lang_map = {
            0: "ru_RU",
            1: "en_US",
            2: "es_ES",
            3: "zh_CN"
        }
        lang_code = lang_map[self.lang_selector.currentIndex()]
        self.app.load_language(lang_code)

    def retranslate_ui(self):
        """Обновляем все тексты при смене языка"""
        self.setWindowTitle(self.tr("RootSolver — Калькулятор корней"))
        self.input_value.setPlaceholderText(self.tr("Введите число"))
        self.input_degree.setPlaceholderText(self.tr("Введите степень (по умолчанию 2)"))
        self.btn_calc.setText(self.tr("Вычислить"))
        self.update_result_text()
