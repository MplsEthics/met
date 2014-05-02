
    PYTHON2X ?= python2.7
  BULKLOADER ?= $(HOME)/local/google_appengine/bulkloader.py
       SHELL := /bin/bash

usage:
	@echo "usage: [clean|csv|localload|upload]"

clean:
	rm -f *.csv bulkloader-{log,progress}-*

csv:
	make scenario.csv
	make answers.csv
	make boards.csv
	make views.csv

scenario.csv:
	$(PYTHON2X) bin/yaml2csv.py src/*.yaml

answers.csv:
	$(PYTHON2X) bin/yaml2csv.py src/*.yaml

boards boards.csv: src/boards.txt
	echo "id,board" > boards.csv
	perl -nle 'print qq{"$$_"}' src/boards.txt | nl -w1 -nln -s , >> boards.csv

views views.csv: src/views.txt
	echo "id,view" > views.csv
	grep -v '^#' src/views.txt | grep '[[:print:]]' | \
		perl -nle 'print qq{"$$_"}' | nl -w1 -nln -s , >> views.csv

localload:
	make localload-boards localload-views
	make localload-scenario localload-answer

localload-boards: boards.csv
	echo XX | $(PYTHON2X) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=boards.csv \
		--kind=Board \
		--passin \
		--email=johntrammell@gmail.com \
		--url http://localhost:8765/remote_api

localload-views: views.csv
	echo XX | $(PYTHON2X) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=views.csv \
		--kind=View \
		--email=johntrammell@gmail.com \
		--passin \
		--url http://localhost:8765/remote_api

localload-scenario: scenario.csv
	echo XX | $(PYTHON2X) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=scenario.csv \
		--kind=Scenario \
		--email=johntrammell@gmail.com \
		--passin \
		--url http://localhost:8765/remote_api

localload-answer: answers.csv
	echo XX | $(PYTHON2X) $(BULKLOADER) \
		--application="dev~mpls-ethics" \
		--config_file=etc/bulkloader.yaml \
		--filename=answers.csv \
		--kind=Answer \
		--email=johntrammell@gmail.com \
		--passin \
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
