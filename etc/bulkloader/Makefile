
       SHELL := /bin/bash
      PYTHON ?= python2.7
  BULKLOADER ?= ../../sdk/google_appengine/bulkloader.py

usage:
	@echo "usage: [clean|csv|localload]"

clean:
	rm -f *.csv bulkloader-{log,progress}-*

csv:
	make scenario.csv
	make answers.csv
	make boards.csv

scenario.csv:
	$(PYTHON) bin/yaml2csv.py src/*.yaml

answers.csv:
	$(PYTHON) bin/yaml2csv.py src/*.yaml

boards.csv: src/boards.txt
	echo "priority,name" > boards.csv
	sed -e 's/\(.*\)/"\1"/' src/boards.txt | nl --number-width=1 \
		--number-format=ln --number-separator="," >> boards.csv

localload: localload-scenarios localload-answers localload-boards

localload-scenarios: scenario.csv
	echo 'XX' | $(PYTHON) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://localhost:8080/remote_api \
		--passin

localload-answers: answers.csv
	echo 'XX' | $(PYTHON) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://localhost:8080/remote_api \
		--passin

localload-boards: boards.csv
	echo 'XX' | $(PYTHON) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=boards.csv \
		--kind=Board \
		--email=johntrammell@gmail.com \
		--url http://localhost:8080/remote_api \
		--passin

upload: upload-scenarios upload-answers upload-boards

upload-scenarios: scenario.csv
	$(PYTHON) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--url http://mpls-ethics.appspot.com/remote_api

upload-answers: answers.csv
	$(PYTHON) $(BULKLOADER) \
		--application="mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--url http://mpls-ethics.appspot.com/remote_api

upload-boards: boards.csv
	$(PYTHON) $(BULKLOADER) \
		--application="s~mpls-ethics-hrd" \
		--config_file=etc/bulkloader.yaml \
		--filename=boards.csv \
		--kind=Board \
		--url http://mpls-ethics.appspot.com/remote_api
