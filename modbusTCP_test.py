import numpy as np
import time
from pyModbusTCP.client import ModbusClient

c = ModbusClient()
c.host("127.0.0.1")
c.port(502)
c.open()
reg = np.uint16(0)

reg = c.read_holding_registers(0, 1) #read from address 0 for 1 register
print(reg)
  
time.sleep(3)

reg = c.read_holding_registers(1, 1) #read from address 1 for 1 register
print(reg)

time.sleep(3)

reg = c.read_holding_registers(2, 1) #read from address 2 for 1 register
print(reg)

c.close()
