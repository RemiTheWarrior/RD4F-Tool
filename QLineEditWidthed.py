from PyQt5.QtWidgets import QLineEdit

class QLineEditWidthed(QLineEdit):
    def __init__(self, text, editable=False):
        super().__init__()
        self.setText(text)
        self.setReadOnly(not editable)
        textSize = self.fontMetrics().size(0, text)
        self.setFixedWidth(textSize.width() + 16)