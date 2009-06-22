
   PACKAGE := mpls-ethics
     STAMP := $(shell date '+%Y%m%d.%H%M%S')
   DISTDIR := $(PACKAGE)-$(STAMP)
       PWD := $(shell pwd)
 APPENGINE := /usr/local/lib/google_appengine
      PATH := /usr/bin:/bin

usage:
	@echo "usage: [clean]"

start gae app:
	$(APPENGINE)/dev_appserver.py --port=9001 appengine/

clean:
	rm -f *.zip *.tar.gz
	rm -rf build/ dist/ *.egg-info/
	find . -name '*.pyc' | xargs rm -f
	python setup.py clean

dist:
	python setup.py dist



dist distdir $(DISTDIR):
	mkdir -p $(DISTDIR)
	cp -a Makefile README $(DISTDIR)
	cp -a doc/ src/ $(DISTDIR)

zip: $(DISTDIR)
	zip -r $(DISTDIR).zip $(DISTDIR)

tgz: $(DISTDIR)
	tar czf $(DISTDIR).tar.gz $(DISTDIR)

run:
	PYTHONPATH=$(PWD) /usr/bin/python met/main.py

   FIX = FIX
   f_i_x_m_e := $(FIX)ME

test: bin/check-yaml.py
	@-ack $(f_i_x_m_e)
	@-find . -name '*.py' | xargs -n 1 pyflakes
	@-find app/content -name '*.yaml' | xargs -n 1 python bin/check-yaml.py
	@-python setup.py test
	

