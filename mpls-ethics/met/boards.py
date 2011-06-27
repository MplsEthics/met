# Copyright 2010 John J. Trammell.
#
# This file is part of the Mpls-ethics software package.  Mpls-ethics
# is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Mpls-ethics is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mpls-ethics.  If not, see <http://www.gnu.org/licenses/>.

"""
A list of the City of Minneapolis boards & commissions, taken mostly from
URL http://www.ci.minneapolis.mn.us/boards-and-commissions/.
"""

_boards = """
Guest
Above the Falls Citizen Advisory Committee
Airports Commission, Metropolitan (MAC)
Animal Care and Control Advisory Board
Arts Commission, Minneapolis
Audit Committee
Bassett Creek Watershed Management Commission
Bloomington-Lake Special Service District Board
Capital Long Range Improvements Committee (CLIC)
Central Avenue Special Service District Advisory Board
Charter Commission
Chicago Avenue Advisory Board (Also known as 48th St E and Chicago Ave S)
Chicago-Lake Special Service District Advisory Board
Citizen Environmental Advisory Committee (CEAC)
Civil Rights Commission, Minneapolis
Civil Service Commission
Civilian Police Review Authority
Complete Count Committee (2010 Census)
Dinkytown Special Service District Advisory Board
Disabilities, Minneapolis Advisory Committee on People With
Downtown Skyway Advisory Committee
East Lake Street Special Service District
Economic Development Company, Minneapolis (MEDC)
Estimate and Taxation, Board of
Ethical Practices Board
Family Housing Fund (McKnight), Minneapolis/St. Paul
Fire Code Board of Appeals
Forty Third Street West and Upton Avenue South Special Service District
Franklin Avenue East Special Service District Advisory Board
Heritage Preservation Commission
Hennepin Theatre District Special Service District Advisory Board
Housing Board of Appeals
Latino Community Advisory Committee to the Mayor and the City Council
Linden Hills Advisory Board (Also known as 43rd St W and Upton Ave S)
Lyndale-Lake Special Service District
Metropolitan Airports Commission
Minneapolis Bicycle Advisory Committee
Minneapolis Tree Advisory Commission
Minneapolis Workforce Council
Minnehaha Creek Watershed District Board
Mississippi Watershed Management Organization
Municipal Building Commission
Neighborhood Revitalization Program (NRP) Policy Board
Neighborhood and Community Engagement Commission
Nicollet Avenue South Special Service District
Nicollet Mall South Special Service District
Park and Recreation Board of Commissioners, Minneapolis
Pedestrian Advisory Committee
Planning Commission
Public Health Advisory Committee
Public Housing Authority, Minneapolis
Riverview Advisory Board
School Board, Minneapolis
Senior Citizen Advisory Committee to the Mayor and City Council
Shingle Creek Watershed Management Commission
South Hennepin Avenue Special Service District Advisory Board
Sports Facilities Commission, Metropolitan
Stadium Village Special Service District Advisory Board
Telecommunications Network (MTN), Minneapolis
Thinc.GreenMSP Steering Committee
Truth in Sale of Housing Board of Appeals
Uptown Special Service District Advisory Committee
Workforce Council, Minneapolis
Youth Coordinating Board
Youth Violence Executive Committee
Zoning Board of Adjustment
"""

# build a list of boards (filter out empty strings)
boards = filter(lambda s: len(s) > 0, _boards.split("\n"))
