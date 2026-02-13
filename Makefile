
build-venv:
	python3 -m venv .venv

activate:
	@echo "source .venv/bin/activate"

deactivate:
	@echo "deactivate"

install:
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python app.py

curl:
	curl -s http://localhost:8080/
	@echo ""
	curl -s http://localhost:8080/health
	@echo ""

