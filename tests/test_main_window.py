import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from main import RootSolver
from ui.main_window import MainWindow

# Фикстура для единственного QApplication на всю сессию
@pytest.fixture(scope="session")
def qapp():
    """Создаёт QApplication один раз на сессию"""
    app = RootSolver([])
    return app

# Фикстура для окна
@pytest.fixture
def app_with_window(qapp, qtbot):
    """Возвращает RootlyApp, MainWindow и qtbot для тестов"""
    window: MainWindow = qapp.main_window
    qtbot.addWidget(window)
    window.show()
    return qapp, window, qtbot

class TestRootSolver:

    def test_initial_state(self, app_with_window):
        app, w, qtbot = app_with_window
        assert w.input_value.text() == ""
        assert w.input_degree.text() == ""
        assert w.result.text() == "Результат появится здесь"

    def test_calculate_root_integer(self, app_with_window):
        app, w, qtbot = app_with_window
        w.input_value.setText("9")
        w.input_degree.setText("2")
        qtbot.mouseClick(w.btn_calc, Qt.MouseButton.LeftButton)

        # Разбираем текст результата
        text = w.result.text()
        assert text.startswith("2-й корень из 9") or text.startswith("2-й корень из 9.0")
        # Проверяем, что результат содержит число 3
        assert "3" in text

    def test_calculate_root_float(self, app_with_window):
        app, w, qtbot = app_with_window
        w.input_value.setText("10")
        w.input_degree.setText("2")
        qtbot.mouseClick(w.btn_calc, Qt.MouseButton.LeftButton)
        # SymPy вернёт Float, проверяем что текст содержит число
        assert "корень из 10" in w.result.text()

    def test_negative_even_degree_complex(self, app_with_window):
        app, w, qtbot = app_with_window
        w.input_value.setText("-8")
        w.input_degree.setText("2")
        qtbot.mouseClick(w.btn_calc, Qt.MouseButton.LeftButton)
        assert "I" in w.result.text()  # SymPy комплексное число
