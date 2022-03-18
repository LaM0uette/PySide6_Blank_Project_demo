from PySide6.QtWidgets import QLineEdit


class EchoMode:

    NORMAL = QLineEdit.Normal
    NO = QLineEdit.NoEcho
    PASSWORD = QLineEdit.Password
    PASSWORD_ON_EDIT = QLineEdit.PasswordEchoOnEdit
