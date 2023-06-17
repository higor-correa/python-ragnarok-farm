import serial
from time import sleep

ser = serial.Serial("COM6", 9600)
warps = [
    "@warp tha_t07",
    "@warp tha_t08",
    "@warp tha_t09",
    "@warp tha_t10",
]
loots = ["@alootid +12040", "@alootid +644", "@alootid +603", "@alootid +617"]

skillPositions = [
    (0, 0),
    # (0, 25),
    # (0, -25),
    # (25, 0),
    # (-25, 0),
]


def moveMouse(position):
    print(f"# Moving mouse to {position}")
    ser.write(bytes("move", encoding="utf-8"))
    sleep(0.02)
    ser.write(bytes(str(position[0]), encoding="utf-8"))
    sleep(0.1)
    ser.write(bytes(str(position[1]), encoding="utf-8"))
    sleep(0.1)


def typeInRagnarok(text):
    print(f"\t>>> {text}")
    ser.write(bytes("typeText", encoding="utf-8"))
    sleep(0.1)
    ser.write(bytes(text, encoding="utf-8"))
    sleep(0.2)


def castSkills():
    print("\t$$$ Casting skills")
    ser.write(bytes("F3", encoding="utf-8"))
    sleep(1.3)
    ser.write(bytes("F1", encoding="utf-8"))
    sleep(1)


def backHomeAndStoreStuff():
    print("\t# Back home and storing stuff")
    ser.write(bytes("ALT7", encoding="utf-8"))
    sleep(2)
    ser.write(bytes("simpleClick", encoding="utf-8"))
    sleep(0.1)
    ser.write(bytes("ALT1", encoding="utf-8"))
    sleep(0.5)
    ser.write(bytes("moveToStorage", encoding="utf-8"))
    sleep(2.5)


print("About to start... Focus Ragnarok screen")

sleep(2)

for loot in loots:
    typeInRagnarok(loot)

maxIterations = 70
while True:
    for warp in warps:
        i = 0
        while i < maxIterations:
            print(f"= Iteration {i+1} of {maxIterations}")
            typeInRagnarok(warp)
            sleep(0.5)

            for position in skillPositions:
                castSkills()
            i += 1
        backHomeAndStoreStuff()
