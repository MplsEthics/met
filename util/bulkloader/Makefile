  PYTHON25 ?= python2.5
 APPENGINE := /usr/local/lib/google_appengine

usage:
	@echo "usage: [clean|csv|load]"

clean:
	rm -f *.csv

csv answers.csv scenario.csv:
	$(PYTHON25) bin/yaml2csv.py src/*.yaml

load: load-scenario load-answer

load-scenario: scenario.csv
	$(PYTHON25) $(APPENGINE)/bulkloader.py \
		--app_id="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api

load-answer: answers.csv
	$(PYTHON25) $(APPENGINE)/bulkloader.py \
		--app_id="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api
