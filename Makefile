
   PACKAGE := mpls-ethics
 APPENGINE := /usr/local/lib/google_appengine
      PATH := /usr/bin:/bin

usage:
	@echo "usage: [clean]"

start gae app:
	$(APPENGINE)/dev_appserver.py --port=9001 app/

clean:
	rm -f MANIFEST *.zip *.tar.gz
	rm -rf build/ dist/ *.egg-info/
	find . -name '*.pyc' | xargs rm -f
	python setup.py clean

dist sdist:
	python setup.py sdist --formats=zip

   FIX = FIX
   ME = ME

test: bin/check-yaml.py
	@-ack $(FIX)$(ME)
	@-find . -name '*.py' | xargs -n 1 pyflakes
	@-find app/content -name '*.yaml' | xargs -n 1 python bin/check-yaml.py
	@-python setup.py test


