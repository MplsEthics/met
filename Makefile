
   PACKAGE := mpls-ethics
 APPENGINE := /usr/local/lib/google_appengine
      PATH := /usr/bin:/bin:/usr/local/bin
  PYTHON25 ?= python2.5

usage:
	@echo "usage: [clean]"

start gae app:
	PYTHON25=$(PYTHON25) APPENGINE=$(APPENGINE) /bin/bash bin/start-appengine.sh

clean:
	rm -f MANIFEST *.zip *.tar.gz
	rm -rf build/ dist/ *.egg-info/
	find . -name '*.pyc' | xargs rm -f
	$(PYTHON25) setup.py clean

archive:
	git archive --verbose --format=tar --prefix="met-0.1/" HEAD | gzip > met-0.1.tgz

update:
	$(PYTHON25) $(APPENGINE)/appcfg.py --email=johntrammell@gmail.com update app/

dist sdist:
	$(PYTHON25) setup.py sdist --formats=zip

   FIX = FIX
   ME = ME

test: bin/check_yaml.py
	@-ack $(FIX)$(ME)
	@-find . -name '*.py' | xargs -n 1 pylint -e
	@-find app/content -name '*.yaml' | xargs -n 1 $(PYTHON25) bin/check_yaml.py

