check: sync snapshot after

sync:
	python3 tools/sync-check.py

snapshot:
	python3 tools/snapshot.py

after:
	python3 tools/check-after.py

mirror:
	python3 tools/sync-check.py --fix-mirror

baseline:
	python3 tools/snapshot.py --update

.PHONY: check sync snapshot after mirror baseline
