PYTHON := $(shell python3)

run:
	ifndef PYTHON
		pip install -r requirements.txt --break-system-packages
		python main.py
	else
		pip install -r requirements.txt --break-system-packages
		python3 main.py