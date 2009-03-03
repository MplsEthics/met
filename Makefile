
   PACKAGE := mpls-ethics
     STAMP := $(shell date '+%Y%m%d.%H%M%S')
   DISTDIR := $(PACKAGE)-$(STAMP)
     PWD   := $(shell pwd)

usage:
	@echo "usage: [clean]"

clean:
	rm -rf $(PACKAGE)-20[0-9][0-9][01][1-9][0-3][0-9].*
	rm -f *.zip *.tar.gz
	find . -name '*.pyc' | xargs rm -f

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

test:
	pyflakes met/

exe:
	python setup.py py2exe --bundle 1

