# Name

mpls-ethics - online ethics training for the city of Minneapolis


## Copyright

Copyright 2022 John J. Trammell.

This file is part of the Mpls-ethics software package.  Mpls-ethics is free
software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, either
version 3 of the License, or (at your option) any later version.

Mpls-ethics is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License
along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.


## Description

This package contains a complete Google App Engine application suitable for
basic municipal ethics training, including the following topics:

* Conflict of Interest
* Disclosure of Information
* Gifts

Each topic contains one or more sample 'scenarios', each having a question
that must be answered correctly before proceeding to the next scenario.  At
the end of the training, a user may enter contact information and submit
proof of completion to a central location.

This training is modeled after the 2007 US DOD Annual Ethics Training
module.


## Resources

* <http://code.google.com/intl/en/appengine/>
* <http://code.google.com/appengine/docs/python/overview.html>
* <http://www.dod.mil/dodgc/defense_ethics/ethics_training/2007_AET/>
* <https://appengine.google.com/>
* <http://stackoverflow.com/questions/20956429/google-app-engine-jinja2-template-extends-base-template-from-parent-folder>


## Python Dependencies

```
% pip install pyyaml nose nosegae
```

## Author

John Trammell <mailto:john.trammell@gmail.com>


## Development notes

* http://localhost:8000/
* http://localhost:8080/

Dates in templates:

* https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#std:templatefilter-date

