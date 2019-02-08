#!/usr/bin/python3
# This file is part of LCD1602 Driver project
# Last-Modified:2019-2-8 17:18:15
# Copyright (C) 2019 SENCOM <sencom1997@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lcd1602 import LCD1602
import time

lcd = LCD1602()
while True:
    localtime = time.asctime( time.localtime(time.time()) )
    sdate = localtime[0:11]
    stime = localtime[11:20]
    lcd.Write_String(1,1,sdate)
    lcd.Write_String(1,2,stime)
