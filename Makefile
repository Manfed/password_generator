VENV:=$(CURDIR)/.venv

VBIN:=$(VENV)/bin

ACTIVATE:=$(VBIN)/activate
PIP:=$(VBIN)/pip

REQUIREMENTS:=$(CURDIR)/requirements.txt

$(VENV):
	@virtualenv -p python3.5 $(VENV)

$(ACTIVATE): $(VENV) $(REQUIREMENTS)
	@$(PIP) install -Ur $(REQUIREMENTS)
	@touch $(ACTIVATE)

.PHONY: venv
venv: $(ACTIVATE)