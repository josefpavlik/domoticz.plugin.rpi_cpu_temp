# rpi_cpu_temp
#
# Author: Jet 2020
#
#
"""
<plugin key="pri_cpu_temp" name="Raspberry CPU temperature" author="Jet" version="0.1" externallink="">
    <description>
    Measure Raspberry Pi CPU temperature
    </description>
    <params>
        <param field="Mode1" label="Polling period [s]" width="75px" default="3"/>
    </params>
</plugin>
"""
import Domoticz
import subprocess
import re

class BasePlugin:
   
    def __init__(self):
        return

    sProtocol = "HTTP"

    def onStart(self):

        Domoticz.Log("onStart - Plugin is starting.")
        self.period=int(Parameters["Mode1"])
        Domoticz.Heartbeat(self.period)

        if (not 1 in Devices):
            Domoticz.Device(Name="", Unit=1, TypeName="Temperature", Used=1).Create()

    def onHeartbeat(self):
        t=subprocess.getoutput("vcgencmd measure_temp")
#        Domoticz.Log("temp result="+t)
        temp=re.compile(r'=([0-9.]+)').search(t)[1]
        Domoticz.Log("temp="+temp)
        Devices[1].Update(0,temp)

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

