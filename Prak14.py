# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:25:13 2024

@author: ocanh
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Masukkan detail Anda:")
        self.label.setFont(QFont('Arial'))

        self.input_nama = QLineEdit()
        self.input_nama.setFont(QFont('Arial'))
        self.input_nama.setPlaceholderText("Nama")

        self.input_nim = QLineEdit()
        self.input_nim.setFont(QFont('Arial'))
        self.input_nim.setPlaceholderText("NIM")

        self.input_hobi = QLineEdit()
        self.input_hobi.setFont(QFont('Arial'))
        self.input_hobi.setPlaceholderText("Hobi")

        self.button_kirim = QPushButton("Kirim")
        self.button_kirim.setFont(QFont('Arial'))
        self.button_kirim.setStyleSheet("background-color: #82E0AA ;")

        self.button_reset = QPushButton("Reset")
        self.button_reset.setFont(QFont('Arial'))
        self.button_reset.setStyleSheet("background-color: #E9F5AA ;")
        self.button_reset.clicked.connect(self.reset_data)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_nama)
        self.layout.addWidget(self.input_nim)
        self.layout.addWidget(self.input_hobi)
        self.layout.addWidget(self.button_kirim)
        self.layout.addWidget(self.button_reset)

        self.button_kirim.clicked.connect(self.display_data)

    def display_data(self):
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        hobi = self.input_hobi.text()

        if not nama or not nim or not hobi:
            QMessageBox.critical(self, "Error", "Harap lengkapi semua bidang.")
            return
        
        if not nim.isdigit():
            QMessageBox.critical(self, "Error", "NIM harus berupa angka.")
            return

        self.label.setText(f"Halo, {nama}!\nNIM Anda adalah {nim}\ndan hobi Anda adalah {hobi}.")

    def reset_data(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_hobi.clear()
        self.label.setText("Masukkan detail Anda:")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        
        self.widget = CustomWidget()
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
