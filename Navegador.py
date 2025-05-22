import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Navegador Simples")
        self.setGeometry(300, 100, 800, 600)

        self.browser = QWebEngineView()

        self.url_bar = QLineEdit(self)
        self.url_bar.setPlaceholderText("Digite a URL ou uma pesquisa no Google")
        self.url_bar.returnPressed.connect(self.load_url_or_search)

        back_button = QPushButton("←", self)
        back_button.setFixedWidth(30)  
        back_button.clicked.connect(self.browser.back)

        top_layout = QHBoxLayout()
        top_layout.addWidget(back_button)
        top_layout.addWidget(self.url_bar)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.browser)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def load_url_or_search(self):
        url_text = self.url_bar.text()
        if "." in url_text:
            url = QUrl(url_text) if url_text.startswith("http") else QUrl("http://" + url_text)
        else:
            url = QUrl(f"https://www.google.com/search?q={url_text}")
        self.browser.setUrl(url)


app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
