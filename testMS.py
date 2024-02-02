import keyboard
import time
import xml.etree.ElementTree as ET
import requests

# url = 'http://192.168.11.160/plant.xml'
# resp = requests.get(url)

# xml = '''<?xml version="1.0" encoding="ISO-8859-1"?><data timezone="Europe/Rome-GMT1" dst="-9999" time="02-02-24 16:20:23" sun="DAY" weblanguage="ITALIANO" dataqu_start="100" dataqu_stop="101" dataqu_cnt="111" send_al="0" getpoststate="1" alarmqu_first="25" alarmqu_last="26" dhcpstatus="0" gateway="OK" upg_portal="OK" data_portal="ERROR" msgdatalive="0" upgreqs="60" rise_h="7" rise_m="32" set_h="17" set_m="22" latout="43.5" longout="11.6" tzout="1.0"><eth macaddr="00:04:A3:B8:3F:7D" ipaddr="192.168.11.160" pn="3N28" sn="118069" fw_vers="1.1.1" > <inv alarmstate="0" pn="3M99" sn="109415" wkman="3818" protocol="Hyperlink" model="R" countrystd="i" invtype="Photovoltaic version" co2_t="30.487" status="OK" vgrid="230.4" igrid="1.5" pout_KW="0.614" fgrid="50.0" vin1="532.7" iin1="0.7" vin2="532.5" iin2="0.6" pin1="324.0" pin2="309.3" tinv="27.3" tboost="25.7" globstat="6" dcdc1stat="2" dcdc2stat="2" modeldesc="TRIO-8.5-TL-OUTD" fwmicver="CAA8" fwdspvers="B6B1" p1idmi="CAA8" p1iddi="B6B1" fwdspboovers="A0AA" p1idbooi="A0AA" alarmstat="0" eday_KWh="24.177" eweek_KWh="111.977" emonth_KWh="38.527" eyear_KWh="474.327" etot_KWh="55430.175" epart_KWh="55430.175" inputmode="0" riso_Mohm="3.30" windfreq_Hz="0.0" fan1sp_rpm="0.0" ntc="27.8"> <disp_trio sn="546593" pn="V13081" wkman="0515" fwmicver="D206" p1idmd="D206" />  </inv> </eth></data>'''
#
# with open('plant.xml', 'wb') as f:
#     f.write(resp.content)
#
# # mytree = ET.parse(xml)
# # mytree = ET.parse('plant.xml')
# # myroot = mytree.getroot()
# myroot = ET.fromstring(resp.content)
#
#
# print(myroot.items())
# print(myroot[0][0].items())
#
# print(myroot[0][0].attrib['pout_KW'])


t0 = time.time()
while not keyboard.is_pressed('esc'):
    url = 'http://192.168.11.160/plant.xml'
    resp = requests.get(url)
    myroot = ET.fromstring(resp.content)

    if time.time() - t0 > 2:
        print('P:', myroot[0][0].attrib['pout_KW'], 'kW')
        t0 = time.time()
    time.sleep(0.05)
