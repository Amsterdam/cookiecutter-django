.PHONY: clean virtualenv project
DEPS:=requirements.txt
PIP=`. venv/bin/activate; which pip`
PYTHON=`. venv/bin/activate; which python`

clean:
	@rm -rf venv
	@echo "Removed virtual environment"

virtualenv: clean
	@virtualenv -q -p python3 venv
	@$(PIP) install -U "pip"
	@$(PIP) install -r $(DEPS)
	@echo "Created virtual environment"

cookiecutter:
	@$(PYTHON) run_cookiecutter.py

project: | cookiecutter clean
