import serial 
from time import sleep

ser = serial.Serial('COM6', 9600)
skillPositions = [
    (0, 0),
    # (0, 25),
    # (0, -25),
    # (25, 0),
    # (-25, 0),
]

def moveMouse(position):
    print(f'# Moving mouse to {position}')
    ser.write(bytes('move', encoding='utf-8'))
    sleep(0.02)
    ser.write(bytes(str(position[0]), encoding='utf-8'))
    sleep(0.1)
    ser.write(bytes(str(position[1]), encoding='utf-8'))
    sleep(0.1)

def typeInRagnarok(text):
    print(f'>>> {text}')
    ser.write(bytes('typeText', encoding='utf-8'))
    sleep(0.1)
    ser.write(bytes(text, encoding='utf-8'))
    sleep(0.1)

def castSkills():
    print('$$$ Casting skills')
    ser.write(bytes('F3', encoding='utf-8'))
    sleep(1.2)
    ser.write(bytes('F1', encoding='utf-8'))
    sleep(1)

def backHomeAndStoreStuff():
    print('# Back home and storing stuff')
    ser.write(bytes('ALT7', encoding='utf-8'))
    sleep(2)
    ser.write(bytes('simpleClick', encoding='utf-8'))
    sleep(0.1)
    ser.write(bytes('ALT1', encoding='utf-8'))
    sleep(0.5)
    ser.write(bytes('moveToStorage', encoding='utf-8'))
    sleep(2)

print('About to start... Focus Ragnarok screen')

sleep(2)

ser.write(bytes('start', encoding='utf-8'))
sleep(0.5)

while True:
    i = 0
    while i < 70:
        sleep(0.5)
        ser.write(bytes('ALT3', encoding='utf-8'))
        sleep(1.5)

        for position in skillPositions:
            moveMouse(position)
            castSkills()
            moveMouse((position[0]*-1, position[1]*-1))
        
        i += 1
    backHomeAndStoreStuff()
    

# while (True):
#     print('oi')
