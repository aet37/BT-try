from mbientlab.metawear import MetaWear, libmetawear
from mbientlab.metawear.cbindings import *

BleScanner.set_handler(device_discover_task)
BleScanner.start()
e.wait()
BleScanner.stop()

address = C5:02:6A:76:E4:5D

device = MetaWear(address)
device.connect()

pattern= LedPattern(repeat_count= Const.LED_REPEAT_INDEFINITELY)