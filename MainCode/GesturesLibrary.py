from Areas import areasList
import Profiles
from pynput.keyboard import Key, Controller
import time

#initializate some vars
kb = Controller()
lastcall = 0
current_profile = 0
locked = True
def controller(hands,distbetweenhands):
    for hand in hands:
        global lastcall
        global current_profile
        global locked
        #Switch Profile Buttom
        # if areasList['SwitchProfile']._isHandInside(hand['center']):
        #     current_time = time.time()
        #     elapsed_time = current_time - lastcall
        #
        #     if elapsed_time >= 1:
        #         if current_profile < 3:
        #             current_profile += 1
        #         else:
        #             current_profile = 1
        #
        #         Profiles._setProfile(current_profile)
        #         lastcall = current_time
        # Profile 1 Command
        #if Profiles.currentProfile == 1:
        #print(areasList['VoltarSlide']._isHandInside(hand['center']))
        if not locked:
            if areasList['VoltarSlide']._isHandInside(hand['center']):
                current_time = time.time()
                elapsed_time = current_time - lastcall

                if elapsed_time >= 1:
                    kb.press(Key.left)
                    print('voltou')
                    lastcall = current_time

            if areasList['PassarSlide']._isHandInside(hand['center']):
                current_time = time.time()
                elapsed_time = current_time - lastcall

                if elapsed_time >= 1:
                    kb.press(Key.right)
                    print('passou')
                    lastcall = current_time

            print(areasList['Ventilador']._isHandInside(hand['center']))
            if areasList['Ventilador']._isHandInside(hand['center']):
                print(areasList['Ventilador']._isHandInside(hand['center']))
                areasList['Ventilador']._ToggleDeviceState()


        if hand['type'] == "Right" and hand['fingers'] == [1, 1, 0, 0, 0]:
            locked = True
            print("travou")
            return

        if hand['type'] == "Left" and hand['fingers'] == [1, 1, 0, 0, 0]:
            locked = False
            print("destravou")
            return
                # Profile 2

    if distbetweenhands != None and distbetweenhands >= 10:
        print("maior que 10cm")
