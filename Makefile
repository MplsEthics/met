   PACKAGE := mpls-ethics
 APPENGINE := /usr/local/lib/google_appengine
      PATH := /usr/bin:/bin:/usr/local/bin
  PYTHON25 ?= python2.5

usage:
	@echo "usage: [clean]"

start gae app:
	PYTHON25=$(PYTHON25) APPENGINE=$(APPENGINE) /bin/bash bin/start-appengine.sh

clean:
	rm -f MANIFEST *.csv *.zip *.tar.gz
	rm -rf build/ dist/ *.egg-info/
	find . -name '*.pyc' | xargs rm -f

archive:
	git archive --verbose --format=tar --prefix="met-0.2/" HEAD | gzip > met-0.2.tar.gz

update:
	$(PYTHON25) $(APPENGINE)/appcfg.py --email=johntrammell@gmail.com update mpls-ethics/

load:
	$(PYTHON25) bin/yaml2csv.py lib/content/*.yaml

#$(PYTHON25) $(APPENGINE)/appcfg.py ???? --filename=bulkloader.yaml

dist sdist:
	$(PYTHON25) setup.py sdist --formats=zip

   FIX = FIX
   ME = ME

test: bin/check_yaml.py
	@-ack $(FIX)$(ME)
	@-find . -name *.py | grep -v '__' | xargs pyflakes
	@-find mpls-ethics/content -name '*.yaml' | xargs -n 1 $(PYTHON25) bin/check_yaml.py

