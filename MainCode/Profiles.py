from Devices import Device
from Areas import *

#Lista de Dispositivos:
ventilador = Device("192.168.0.105","Ventilador",cooldown= 8)


#lista de Areas
#Area("Area1",(50, 50), 200, 100, ventilador)

currentProfile = 0

def _setProfile(n):
    global currentProfile
    areasList.clear()
    #Area("SwitchProfile", origin=(254, 372), end=(402, 450))
    #Area('Quadro',origin=(26, 49), end=(623, 335))

    if n == 1:
        Area('Ventilador',origin=(8, 138), end=(148, 248) ,device=ventilador)
        Area("PassarSlide", origin=(466, 249), end=(582, 358))
        Area("VoltarSlide", origin=(8, 248),end=(148, 365))


    if n == 2:
        Area("Area1", (200, 200), 150, 150)

    if n == 3:
        Area("Area1", (200, 200), 500, 500)


    currentProfile = n