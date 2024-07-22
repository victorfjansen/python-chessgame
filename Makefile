PYTHON3 := $(shell python3 --version)

run:
ifdef PYTHON3
	pip install -r requirements.txt --break-system-packages
	python3 main.py
else
	pip install -r requirements.txt --break-system-packages
	python main.py
endif