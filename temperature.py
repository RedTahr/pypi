from gpiozero import MCP3008, LED #, RGBLED
from time import sleep
deg = chr(176)+'C'
tmp = MCP3008(channel=0, device=0)
red = LED(19)
green = LED(17)
blue = LED(18)
# led = RBGLED(red=20, green=21, blue=22)

while True:
    temperature = (tmp.value * 3.3 - 0.5)*100
    if temperature > 24:
        red.on()
    else:
        red.off()
        
    if temperature > 18 and temperature < 25:
        green.on()
    else:
        green.off()
        
    if temperature < 19:
        blue.on()
    else:
        blue.off()
        
        
    print('{:.1f}'.format(temperature), deg, 10 * ' ')
    sleep(0.5)
