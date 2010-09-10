    PYTHON25 ?= python2.5
  BULKLOADER ?= /usr/local/bin/bulkloader.py

usage:
	@echo "usage: [clean|csv|load]"

clean:
	rm -f *.csv bulkloader-{log,progress}-*

csv answers.csv scenario.csv:
	$(PYTHON25) bin/yaml2csv.py src/*.yaml

load: load-scenario load-answer

load-scenario: scenario.csv
	$(PYTHON25) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api

load-answer: answers.csv
	$(PYTHON25) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api

upload: upload-scenario upload-answer

upload-scenario: scenario.csv
	$(PYTHON25) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://mpls-ethics.appspot.com/remote_api

upload-answer: answers.csv
	$(PYTHON25) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://mpls-ethics.appspot.com/remote_api
