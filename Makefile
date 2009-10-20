# Copyright 2009 John J. Trammell
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

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
	git archive --verbose --format=tar --prefix="met-0.2/" HEAD | gzip > met-0.2.tar.gz

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

