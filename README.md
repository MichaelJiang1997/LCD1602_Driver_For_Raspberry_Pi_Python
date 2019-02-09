# LCD1602_Driver_For_Raspberry_Pi_Python
<br>LCD 1602 Driver For Raspberry Pi 3B (Python)

树莓派3b的Lcd1602驱动(Python版)<br/>
开发环境 <code>Python 3.5.3 (default, Sep 27 2018, 17:25:39)</code><br/>
运行例子方法：</br>
1.确保你的树莓派已经安装 rpi.gpio 如果没有<code>sudo apt install python-rpi.gpio</code></br>
2.连线</br>
VSS -> GND</br>
VDD -> VCC</br>
VO  -> 偏压信号</br>
RS  -> GPIO1</br>
RW  -> GPIO4</br>
E   -> GPIO5</br>
D0   -> GPIO0</br>
D1   -> GPIO2</br>
D2   -> GPIO3</br>
D3   -> GPIO21</br>
D4   -> GPIO22</br>
D5   -> GPIO23</br>
D6   -> GPIO24</br>
D7   -> GPIO25</br>
A   -> VCC</br>
K   -> GND</br>
3.切换到项目目录然后<code>python example_tiny_clock.py</code></br>
4.完成</br>
<br/>
更新日志<br/>
<br/>与C++版保持一致<br/>
<br/>
<br/>
2019年2月8日23:02:57</br>
