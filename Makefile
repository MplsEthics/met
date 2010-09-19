# Copyright 2010 John J. Trammell.
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
 APPENGINE := /usr/local/google_appengine
      PATH := /usr/bin:/bin:/usr/local/bin
  PYTHON25 ?= python2.5

usage:
	@echo "usage: [clean]"

start gae app:
	PYTHON25=$(PYTHON25) APPENGINE=$(APPENGINE) /bin/bash bin/start-appengine.sh

clean:
	rm -f MANIFEST bulkloader-* *.csv *.zip *.tar.gz
	rm -rf build/ dist/ *.egg-info/
	find . -name '*.pyc' | xargs rm -f

update:
	$(PYTHON25) $(APPENGINE)/appcfg.py --email=johntrammell@gmail.com update mpls-ethics/

nose nosetest:
	nosetests-2.5 -v -s --with-gae

   FIX = FIX
   ME = ME

nose nosetest:
	(cd mpls-ethics; nosetests-2.5 --with-gae \
		--gae-datastore=/tmp/dev_appserver.datastore \
		--without-sandbox)

test: bin/check_yaml.py
	@-ack $(FIX)$(ME)
	@-find . -name *.py | grep -v '__' | xargs pyflakes
	@-find util/bulkloader/src -name '*.yaml' | xargs -n 1 $(PYTHON25) bin/check_yaml.py
