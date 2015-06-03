# Copyright 2012 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics is free
# software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

     PACKAGE := mpls-ethics
        PATH := /usr/bin:/bin:/usr/local/bin
      PYTHON ?= python2.7
        NOSE := nosetests-2.7

   APPENGINE := ./sdk/google_appengine
     ZIPFILE := google_appengine_1.9.21.zip
      ZIPURL := https://storage.googleapis.com/appengine-sdks/featured/$(ZIPFILE)

.PHONY: start

usage:
	@echo "usage: [clean|realclean|sdk|start]"

clean:
	rm -f MANIFEST bulkloader-* *.csv *.tar.gz
	rm -rf build/ dist/ *.egg-info/
	find . -name '*.pyc' -exec rm {} \;

realclean:
	git clean -df

sdk: sdk/google_appengine

sdk/google_appengine/dev_appserver.py:
	make sdk/google_appengine

sdk/google_appengine: sdk/$(ZIPFILE)
	mkdir -p sdk
	cd sdk; unzip -q $(ZIPFILE)

sdk/$(ZIPFILE):
	mkdir -p sdk ~/Downloads
	if [ ! -e ~/Downloads/$(ZIPFILE) ]; then (cd ~/Downloads; wget $(ZIPURL)); fi
	cp ~/Downloads/$(ZIPFILE) sdk/ \

start: sdk/google_appengine/dev_appserver.py
	$(PYTHON) sdk/google_appengine/dev_appserver.py --skip_sdk_update_check 1 mpls-ethics/

update:
	$(PYTHON) $(APPENGINE)/appcfg.py --email=johntrammell@gmail.com update mpls-ethics/

nose nosetest:
	$(NOSE) -v -s --with-gae

test: bin/check_yaml.py
	@-ack $$(echo "abcde" | tr 'edcba' 'emxif')
	@-find . -name *.py | grep -v '__' | xargs pyflakes
	@-find util/bulkloader/src -name '*.yaml' | xargs -n 1 $(PYTHON) bin/check_yaml.py
	cd mpls-ethics; $(NOSE) -v --with-gae --gae-lib-root=$(APPENGINE) --without-sandbox

