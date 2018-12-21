.PHONY: clean virtualenv project
DEPS:=requirements.txt
PIP=`. venv/bin/activate; which pip`
PYTHON=`. venv/bin/activate; which python`

clean:
	@rm -rf venv

virtualenv: clean
	@virtualenv -p python3 venv
	@$(PIP) install -U "pip"
	@$(PIP) install -r $(DEPS)

cookiecutter:
	@$(PYTHON) run_cookiecutter.py

project: | cookiecutter clean
