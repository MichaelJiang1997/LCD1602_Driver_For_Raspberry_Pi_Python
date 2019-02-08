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

pi = [0x00, 0x1f, 0x0a, 0x0a, 0x0a, 0x13, 0x00, 0x00]  #自定义 pai 字模

lcd = LCD1602()
lcd.Set_User_Char(0, pi);#在 0 号自定义字符位置写入 pi
lcd.Write_User_Char(1, 1, 0);#把 0 号单元的自定义字符 打印到(1,1)