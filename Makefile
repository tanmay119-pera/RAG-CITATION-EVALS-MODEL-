.PHONY: help install ingest build-index test eval ablations app clean

help:
	@echo "Available commands:"
	@echo "  make install      - Install python dependencies"
	@echo "  make ingest       - Ingest and chunk raw documents"
	@echo "  make build-index  - Build BM25 and VectorStore indexes"
	@echo "  make test         - Run full unit test suite"
	@echo "  make eval         - Run golden dataset evaluation benchmark"
	@echo "  make ablations    - Run ablation experiments"
	@echo "  make app          - Launch interactive Streamlit demo"

install:
	pip install -r requirements.txt

ingest:
	python3 scripts/ingest.py

build-index:
	python3 scripts/build_index.py

test:
	PYTHONPATH=src python3 -m unittest discover -s tests -v

eval:
	PYTHONPATH=src python3 scripts/run_eval.py

ablations:
	PYTHONPATH=src python3 scripts/run_ablations.py

app:
	python3 scripts/run_app.py

clean:
	rm -rf __pycache__ src/**/__pycache__ tests/__pycache__ .pytest_cache
