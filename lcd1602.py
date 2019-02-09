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

import RPi.GPIO as GPIO
import time

class LCD1602():
        SETMODE = 0x38        #16*2显示,5*8点阵,8位数据接口
        DISOPEN = 0x0C        #显示开,显示光标,光标不闪烁
        DISMODE = 0x06        #读写字符后地址加1,屏显不移动
        SETADDR = 0x80        #设置数据地址指针初始值
        CLEAR   = 0x01        #清屏,数据指针清零
        RET     = 0x02        #回车,数据指针清零
        LSHIFT  = 0x18        #屏幕左移
        RSHIFT  = 0x1C        #屏幕右移

        COM_SLEEP  = 0.02        #指令延时
        DATA_SLEEP = 0.01        #数据延时
        _data_pins = [0, 0, 0, 0, 0, 0, 0, 0]
        _rs_pin = 0
        _rw_pin = 0
        _en_pin = 0

        #初始化,参数为对应的GPIO针脚(BOARD编码)
        def __init__(   self, rs = 12,  rw = 16,  en = 18, \
                     d0 = 11, d1 = 13,  d2 = 15,  d3 = 29, \
                     d4 = 31, d5 = 33,  d6 = 35,  d7 = 37):
                GPIO.setwarnings(False)
                self._rs_pin = rs
                self._rw_pin = rw
                self._en_pin = en
                self._data_pins[0] = d0
                self._data_pins[1] = d1
                self._data_pins[2] = d2
                self._data_pins[3] = d3
                self._data_pins[4] = d4
                self._data_pins[5] = d5
                self._data_pins[6] = d6
                self._data_pins[7] = d7
                
                GPIO.setmode(GPIO.BOARD)
                for i in range(8):
                        GPIO.setup(self._data_pins[i], GPIO.OUT)
                GPIO.setup(self._rs_pin, GPIO.OUT)
                GPIO.setup(self._rw_pin, GPIO.OUT)
                GPIO.setup(self._en_pin, GPIO.OUT)

                self.__Write_Com(self.SETMODE)     #模式设置
                self.__Write_Com(self.DISOPEN)     #显示设置
                self.__Write_Com(self.DISMODE)     #显示模式
                self.__Write_Com(self.CLEAR)       #清屏

        #写命令
        def __Write_Com(self, com):
                GPIO.output(self._en_pin, GPIO.LOW)
                GPIO.output(self._rs_pin, GPIO.LOW)
                GPIO.output(self._rw_pin, GPIO.LOW)
                for i in range(8):
                        GPIO.output(self._data_pins[i],(com >> i) & 0x01)
                time.sleep(self.COM_SLEEP)
                GPIO.output(self._en_pin, GPIO.HIGH)
                time.sleep(self.COM_SLEEP)
                GPIO.output(self._en_pin, GPIO.LOW)
                time.sleep(self.COM_SLEEP)

        #写数据
        def __Write_Dat(self, dat):
                GPIO.output(self._en_pin, GPIO.LOW)
                GPIO.output(self._rs_pin, GPIO.HIGH)
                GPIO.output(self._rw_pin, GPIO.LOW)
                for i in range(8):
                        GPIO.output(self._data_pins[i],(ord(dat) >> i) & 0x01)
                time.sleep(self.DATA_SLEEP)
                GPIO.output(self._en_pin, GPIO.HIGH)
                time.sleep(self.DATA_SLEEP)
                GPIO.output(self._en_pin, GPIO.LOW)
                time.sleep(self.DATA_SLEEP)

        #写用户自定义字符数据
        def __Write_User_Dat(self, index):
                GPIO.output(self._en_pin, GPIO.LOW)
                GPIO.output(self._rs_pin, GPIO.HIGH)
                GPIO.output(self._rw_pin, GPIO.LOW)
                for i in range(8):
                        GPIO.output(self._data_pins[i],(index >> i) & 0x01)
                time.sleep(self.DATA_SLEEP)
                GPIO.output(self._en_pin, GPIO.HIGH)
                time.sleep(self.DATA_SLEEP)
                GPIO.output(self._en_pin, GPIO.LOW)
                time.sleep(self.DATA_SLEEP)

        #写字符串 x:列数 y:行数 (默认屏幕左上角为 第一行第一列) *s为字符串地址
        def Write_String(self, x, y, s):
                self.__Write_Com(0x80)
                if y == 1:
                        self.__Write_Com(0x80 + x - 1)
                else:
                        self.__Write_Com(0xC0 + x - 1)
                for c in s:
                        self.__Write_Dat(c)

        #清屏
        def Clear(self):
                self.__Write_Com(self.CLEAR)

        #字符位移 dire:移动方向 ms:移动速度(以毫秒为单位) len:移动长度
        def Shift(self, dire, ms, lens):
                if dire:
                        for i in range(0, lens):
                                self.__Write_Com(self.LSHIFT)
                                time.sleep(0.001 * ms)
                else:
                        for i in range(0, lens):
                                self.__Write_Com(self.RSHIFT)
                                time.sleep(0.001 * ms)

        #设置自定义字符 index 为自定义符号编号 从 0 --- 7 八个自定义字符编号，c为字符串
        def Set_User_Char(self, index, c):
                self.__Write_Com(0x80)
                self.__Write_Com(index | 0x40)
                for i in range(8):
                        self.__Write_User_Dat(c[i])

        #写用户自定义字符串 x:列数 y:行数 (默认屏幕左上角为 第一行第一列) index为用户自定义字符串编号
        def Write_User_Char(self, x, y, index):
                self.__Write_Com(0x80)
                if y == 1:
                        self.__Write_Com(0x80 + x - 1)
                else:
                        self.__Write_Com(0xC0 + x - 1)
                self.__Write_User_Dat(index)
