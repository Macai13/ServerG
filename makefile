all:
	python -m PyQt6.uic.pyuic design\MainWindow_UI.ui -o package\ui\mainwindow_ui.py
	maturin develop --release
	pyinstaller main.spec
dv:
	maturin develop --release

env:
	.\.env\Scripts\activate.ps1