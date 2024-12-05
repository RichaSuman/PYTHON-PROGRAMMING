VENV = pytest_venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: 
	test -d venv || python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirement.txt

run: $(VENV)/bin/activate
	./$(VENV)/bin/python3 wallet.py

python:

pytest:

clean:
    rm -rf __pycache__
	 rm -rf $(VENV)

