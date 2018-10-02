from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from led import Led

fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(1,1,1, projection='3d')

ax.set_xlabel('Column')
ax.set_ylabel('Row')
ax.set_zlabel('Layer')

ax.set_xticks([0, 1, 2, 3])
ax.set_yticks([3, 2, 1, 0])
ax.set_zticks([3, 2, 1, 0])

# ax.set_autoscale_on(False)

plt.xlim(0, 4)
plt.ylim(0, 4)
# plt.zlim(0, 4)
# plt.autoscale(False)

ax.view_init(elev=-160, azim=-50)

def setAxis(ax):
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.set_zlabel('Layer')

    ax.set_xticks([0, 1, 2, 3])
    ax.set_yticks([3, 2, 1, 0])
    ax.set_zticks([3, 2, 1, 0])

    ax.set_xlim(-1,4)
    ax.set_ylim(-1,4)
    ax.set_zlim(-1,4)

def animLED(i):
    ''' Get LED plot data and Plot '''
    global animCount
    plotLED = cubes[animCount].LEDplot
    ax.clear()
    setAxis(ax)
    ax.scatter(plotLED[2], plotLED[1], plotLED[0], c='g', marker='o', s=300)
    animCount = (animCount + 1) % len(cubes)

#----------------------------------------------------------------------
def cubeFun(cubeStr, fun=None, n=None):
    '''Create new cube and execute function n times '''
    for c in range(n):
        if c == 0:
            newCube = [Led()]
            newCube[0].cubify(cubeStr)
            newCube[0].ledScatter()
            newCube[0].seqSize = n * 8
        newCube.append(newCube[c].cp())
        newCube[-1].funs[fun]()
        newCube[-1].ledScatter()
    return newCube

#----------------------------------------------------------------------
def cubeStrFun(cubeStrList):
    '''Create new cubes from a list of hex strings'''
    cubeSeq = []
    for i, hexStr in enumerate(cubeStrList):
        newCube = Led()
        newCube.cubify(hexStr)
        newCube.ledScatter()
        if i == 0:
            newCube.seqSize = 8 * len(cubeStrList)
        cubeSeq.append(newCube)
        # print("CubeStr== ", newCube[-1].LEDplot)
    return cubeSeq

#----------------------------------------------------------------------

# led class functions:
#        "newCube"
#        "ledScatter"
#        "cp"
#        "cubify"
#        "printCube"
#        "asm"
#        "rotateZccw"
#        "rotateZcw"
#        "rotateYccw"
#        "rotateYcw"
#        "rotateXccw"
#        "rotateXcw"
#        "shiftUp"
#        "shiftDown"
#        "mixDown"
#        "mixUp"

#----------------------------------------------------------------------
prn = False  #option to print cube data
#----------------------------------------------------------------------
cubeStr = []
cubes = []

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("F731, FEC8, 137F, 8CEF")
cubes.append(cubeFun(cubeStr[-1], "rotateZccw", 12))

'''
cubes1 = [Led()]
cubes1[0].cubify(cubeStr1[0])
cubes1[0].ledScatter()

if prn:
    print("\nCube 1\n")
    cubes1[0].printCube()
    print()

for c in range(12):
    cubes1.append(cubes1[c].cp())
    cubes1[-1].rotateZccw()
    cubes1[-1].ledScatter()
    if prn:
        cubes1[-1].printCube()
        print()
'''
#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("D100, D100, D100, D100")
cubes.append(cubeFun(cubeStr[-1], "rotateZcw", 12))

'''
cubeStr2 = []
cubeStr2.append("D100, D100, D100, D100")

cubes2 = [Led()]
cubes2[0].cubify(cubeStr2[0])
cubes2[0].ledScatter()

if prn:
    print("\nCube 2\n")
    cubes2[0].printCube()
    print()

for c in range(12):
    cubes2.append(cubes2[c].cp())
    cubes2[-1].rotateZcw()
    cubes2[-1].ledScatter()
    if prn:
        cubes2[-1].printCube()
        print()
'''

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubes.append(cubeFun(cubeStr[-1], "rotateXcw", 12))

'''
cubeStr3 = []
cubeStr3.append("FFFF, 0000, 0000, 0000")

cubes3 = [Led()]
cubes3[0].cubify(cubeStr3[0])
cubes3[0].ledScatter()

if prn:
    print("\nCube 3\n")
    cubes3[0].printCube()
    print()

for c in range(12):
    cubes3.append(cubes3[c].cp())
    cubes3[-1].rotateXcw()
    cubes3[-1].ledScatter()
    if prn:
        cubes3[-1].printCube()
        print()
'''

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubes.append(cubeFun(cubeStr[-1], "rotateXccw", 12))

'''
cubeStr4 = []
cubeStr4.append("FFFF, 0000, 0000, 0000")

cubes4 = [Led()]
cubes4[0].cubify(cubeStr4[0])
cubes4[0].ledScatter()

if prn:
    print("\nCube 4\n")
    cubes4[0].printCube()
    print()

for c in range(12):
    cubes4.append(cubes4[c].cp())
    cubes4[-1].rotateXccw()
    cubes4[-1].ledScatter()
    if prn:
        cubes4[-1].printCube()
        print()
'''
#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubes.append(cubeFun(cubeStr[-1], "rotateYcw", 12))

'''
cubeStr5 = []
cubeStr5.append("FFFF, 0000, 0000, 0000")

cubes5 = [Led()]
cubes5[0].cubify(cubeStr5[0])
cubes5[0].ledScatter()

if prn:
    print("\nCube 5\n")
    cubes5[0].printCube()
    print()

for c in range(12):
    cubes5.append(cubes5[c].cp())
    cubes5[-1].rotateYcw()
    cubes5[-1].ledScatter()
    if prn:
        cubes5[-1].printCube()
        print()
'''
#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubes.append(cubeFun(cubeStr[-1], "rotateYccw", 12))

'''
cubeStr6 = []
cubeStr6.append("FFFF, 0000, 0000, 0000")

cubes6 = [Led()]
cubes6[0].cubify(cubeStr6[0])
cubes6[0].ledScatter()

if prn:
    print("\nCube 6\n")
    cubes6[0].printCube()
    print()

for c in range(12):
    cubes6.append(cubes6[c].cp())
    cubes6[-1].rotateYccw()
    cubes6[-1].ledScatter()
    if prn:
        cubes6[-1].printCube()
        print()
'''
#----------------------------------------------------------------------
#Tumble Forward Strings
cubeStrT = []
cubeStrT.append("0F00, F000, F000, F000")
cubeStrT.append("00F0, 0F00, F000, F000")
cubeStrT.append("000F, 00F0, 0F00, F000")
cubeStrT.append("0000, 00FF, 0F00, F000")
cubeStrT.append("0000, 0000, 0FFF, F000")
cubeStrT.append("0000, 0000, 0000, FFFF")
cubeStrT.append("0000, 0000, F000, 0FFF")
cubeStrT.append("0000, F000, 0F00, 00FF")
cubeStrT.append("F000, 0F00, 00F0, 000F")
cubeStrT.append("F000, 0F00, 00F0, 00F0")
cubeStrT.append("F000, 0F00, 0F00, 0F00")
cubeStrT.append("F000, F000, F000, F000")
cubeStrT.append("0F00, F000, F000, F000")
cubeStrT.append("00F0, 0F00, F000, F000")
cubeStrT.append("000F, 00F0, 0F00, F000")
cubeStrT.append("000F, 00F0, FF00, 0000")
cubeStrT.append("000F, FFF0, 0000, 0000")
cubeStrT.append("FFFF, 0000, 0000, 0000")
cubeStrT.append("FFF0, 000F, 0000, 0000")
cubeStrT.append("FF00, 00F0, 000F, 0000")
cubeStrT.append("F000, 0F00, 00F0, 000F")
cubeStrT.append("0F00, 0F00, 00F0, 000F")
cubeStrT.append("00F0, 00F0, 00F0, 000F")
cubeStrT.append("000F, 000F, 000F, 000F")
cubeStrT.append("000F, 000F, 000F, 00F0")
cubeStrT.append("000F, 000F, 00F0, 0F00")
cubeStrT.append("000F, 00F0, 0F00, F000")
cubeStrT.append("0000, 00FF, 0F00, F000")
cubeStrT.append("0000, 0000, 0FFF, F000")
cubeStrT.append("0000, 0000, 0000, FFFF")
cubeStrT.append("0000, 0000, F000, 0FFF")
cubeStrT.append("0000, F000, 0F00, 00FF")
cubeStrT.append("F000, 0F00, 00F0, 000F")
cubeStrT.append("F000, F000, 0F00, 00F0")
cubeStrT.append("F000, F000, F000, 0F00")
cubeStrT.append("F000, F000, F000, F000")

cubes.append(cubeStrFun(cubeStrT))

'''
cubes7 = []

for hs in cubeStr7:
	cubes7.append(Led())
	cubes7[-1].cubify(hs)
	cubes7[-1].ledScatter()


if (0): # prn:
    print("\nCube 7\n")
    for c7 in cubes7:
        c7.printCube()
        print()
'''

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("0000, 0000, 0000, FFFF")
cubes.append(cubeFun(cubeStr[-1], "shiftUp", 12))

'''
for c in range(12):
    if c == 0:
        cubes8 = [Led()]
        cubes8[0].cubify(cubeStr8[0])
        cubes8[0].ledScatter()
    cubes8.append(cubes8[c].cp())
    cubes8[-1].shiftUp()
    cubes8[-1].ledScatter()
    if prn:
        cubes8[-1].printCube()
        print()

if prn:
    print("\nCube 8\n")
    cubes8[0].printCube()
    print()
'''

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("9999, 6666, 0000, 0000")
cubes.append(cubeFun(cubeStr[-1], "shiftDown", 12))

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("FF00, FF00, FF00, FF00")
cubes.append(cubeFun(cubeStr[-1], "mixDown", 12))

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("FF00, FF00, FF00, FF00")
cubes.append(cubeFun(cubeStr[-1], "mixUp", 12))

#----------------------------------------------------------------------
if(0):
    for c in cubes1:
        print(c.cube)
        print()

    print('@'*60)

    for c in cubes2:
        print(c.cube)
        print()

#----------------------------------------------------------------------
# Combining cubes and cubes2 for animation

for i, c in enumerate(cubes):
    print("\nCube#: ", i, "Size: ", c[0].seqSize)
    for n, a in enumerate(c):
        print(n, " : ", a)

seqSizes = [c[0].seqSize for c in cubes]
print("\nSequence Sizes: ", seqSizes)
cubes = [p for sl in cubes for p in sl] #Flatten cubes list

#----------------------------------------------------------------------
# Generate and print asm data

print("\nGenerating ASM data  ", 8 * len(cubes), " Bytes\n")
asmData = []
''
for c in cubes:
    asmHex = c.asm()
    asmData.append(asmHex)
    print(asmHex)
''

#----------------------------------------------------------------------
# Example accessing Hex Data
print("\nCube Hex Data:\n")
# print(cubes[5].cubeHex)
# print(asmData[5])
print("\nASM data Length: ", len(asmData) * 8, "\n\n")
#----------------------------------------------------------------------
# Plotting animation data
animCount = 0
ani = animation.FuncAnimation(fig, animLED, interval=200)
plt.show()


