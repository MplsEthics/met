

    PYTHON2X ?= python2.5
  BULKLOADER ?= /usr/local/google_appengine/bulkloader.py

usage:
	@echo "usage: [clean|csv|load]"

clean:
	rm -f *.csv bulkloader-{log,progress}-*

csv:
	make scenario.csv
	make answers.csv
	make boards.csv

scenario.csv:
	$(PYTHON2X) bin/yaml2csv.py src/*.yaml

answers.csv:
	$(PYTHON2X) bin/yaml2csv.py src/*.yaml

boards boards.csv: src/boards.txt
	nl -w1 -nln -s , src/boards.txt > boards.csv

localload: localload-scenario localload-answer

localload-scenario: scenario.csv
	$(PYTHON2X) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api

localload-answer: answers.csv
	$(PYTHON2X) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api

upload: upload-scenario upload-answer

upload-scenario: scenario.csv
	$(PYTHON2X) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://mpls-ethics.appspot.com/remote_api

upload-answer: answers.csv
	$(PYTHON2X) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://mpls-ethics.appspot.com/remote_api
