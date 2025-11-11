from PyQt6.QtWidgets import QMessageBox

def show_error(message: str):
    msg = QMessageBox()
    msg.setWindowTitle("Ошибка")
    msg.setText(message)
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.exec()
