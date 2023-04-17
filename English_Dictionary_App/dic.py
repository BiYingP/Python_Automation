from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout

from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox

from PyQt6.QtCore import Qt

import json

data = json.load(open("data.json"))

def translate():
	word = text.text()
	word = word.lower()

	if word in data:
		res = data[word]
		output_label.setText("\n".join(res))
	else:
		output_label.setText("The word does not exit.")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Word Definition")

layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout.addLayout(layout1)

layout2 = QVBoxLayout()
layout.addLayout(layout2)

text = QLineEdit()
layout1.addWidget(text)

btn = QPushButton("Convert")
layout1.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(translate)

output = QWidget()

output_label = QLabel("")
output_label.setFixedSize(600,50)
layout2.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
