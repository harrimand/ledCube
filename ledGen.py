from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from led import Led

fig = plt.figure()

ax = fig.add_subplot(1,1,1, projection='3d')

ax.set_xlabel('Column')
ax.set_ylabel('Row')
ax.set_zlabel('Layer')

ax.set_xticks([0, 1, 2, 3])
ax.set_yticks([3, 2, 1, 0])
ax.set_zticks([3, 2, 1, 0])

plt.xlim(0, 4)
plt.ylim(0, 4)

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
    plotLED = cubePlots[animCount].LEDplot
    ax.clear()
    setAxis(ax)
    ax.scatter(plotLED[2], plotLED[1], plotLED[0], c='g', marker='o', s=300)
    animCount = (animCount + 1) % len(cubePlots)

#----------------------------------------------------------------------
def cubeFun(fun=None, n=None):
    '''Create new cube and execute function n times '''
    for c in range(n):
        if c == 0:
            newCube = [Led()]
            newCube[0].cubify(cubeStr[-1])
            newCube[0].ledScatter()
            newCube[0].seqSize = n * 8
        newCube.append(newCube[c].cp())
        newCube[-1].funs[fun]()
        newCube[-1].ledScatter()
    cubes.append(newCube)

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
    cubes.append(cubeSeq)

#----------------------------------------------------------------------

# Led class functions:
#  "newCube"      Create a new 4x4x4 list for cube
#  "ledScatter"   Create X,Y,Z plot data from cube
#  "cp"           Create a copy of Led object
#  "cubify"       Convert Hex string to populate cube
#  "printCube"    Print binary cube layers
#  "asm"          Generate Hex data for ASM file
#  "rotateZccw"   Rotate counter clockwise on Z axis from top view
#  "rotateZcw"    Rotate clockwise on Z axis from top view
#  "rotateYccw"   Rotate counter clockwise on Y axis from front view
#  "rotateYcw"    Rotate clockwise on Y axis from front view
#  "rotateXccw"   Rotate counter clockwise on X axis from left view
#  "rotateXcw"    Rotate clockwise on X axis from left view
#  "shiftUp"      Shift layers Up; Top layer shifted to bottom layer
#  "shiftDown"    Shift layers Down; Bottom layer shifted to top layer
#  "mixDown"      Rotate left columns clockwise; Right columns counterclockwise
#  "mixUp"        Rotate left columns counterclockwise; Right columns clockwise
#  "fig8Z"        Figure 8 motion from top view
#----------------------------------------------------------------------
prn = False  #option to print cube data
#----------------------------------------------------------------------
cubeStr = []
cubes = []

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("F731, FEC8, 137F, 8CEF")
cubeFun("rotateZccw", 12)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("D100, D100, D100, D100")
cubeFun("rotateZcw", 12)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubeFun("rotateXcw", 12)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubeFun("rotateXccw", 12)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubeFun("rotateYcw", 12)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFFF, 0000, 0000, 0000")
cubeFun("rotateYccw", 12)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("FFF0, F000, 0000, 0000")
cubeFun("rotateXccw", 2)

#----------------------------------------------------------------------
#Tumble Forward Strings
cubeStrA = []
cubeStrA.append("0F00, F000, F000, F000")
cubeStrA.append("00F0, 0F00, F000, F000")
cubeStrA.append("000F, 00F0, 0F00, F000")
cubeStrA.append("0000, 00FF, 0F00, F000")
cubeStrA.append("0000, 0000, 0FFF, F000")
cubeStrA.append("0000, 0000, 0000, FFFF")
cubeStrA.append("0000, 0000, F000, 0FFF")
cubeStrA.append("0000, F000, 0F00, 00FF")
cubeStrA.append("F000, 0F00, 00F0, 000F")
cubeStrA.append("F000, 0F00, 00F0, 00F0")
cubeStrA.append("F000, 0F00, 0F00, 0F00")
cubeStrA.append("F000, F000, F000, F000")
cubeStrA.append("0F00, F000, F000, F000")
cubeStrA.append("00F0, 0F00, F000, F000")
cubeStrA.append("000F, 00F0, 0F00, F000")
cubeStrA.append("000F, 00F0, FF00, 0000")
cubeStrA.append("000F, FFF0, 0000, 0000")
cubeStrA.append("FFFF, 0000, 0000, 0000")
cubeStrA.append("FFF0, 000F, 0000, 0000")
cubeStrA.append("FF00, 00F0, 000F, 0000")
cubeStrA.append("F000, 0F00, 00F0, 000F")
cubeStrA.append("0F00, 0F00, 00F0, 000F")
cubeStrA.append("00F0, 00F0, 00F0, 000F")
cubeStrA.append("000F, 000F, 000F, 000F")
cubeStrA.append("000F, 000F, 000F, 00F0")
cubeStrA.append("000F, 000F, 00F0, 0F00")
cubeStrA.append("000F, 00F0, 0F00, F000")
cubeStrA.append("0000, 00FF, 0F00, F000")
cubeStrA.append("0000, 0000, 0FFF, F000")
cubeStrA.append("0000, 0000, 0000, FFFF")
cubeStrA.append("0000, 0000, F000, 0FFF")
cubeStrA.append("0000, F000, 0F00, 00FF")
cubeStrA.append("F000, 0F00, 00F0, 000F")
cubeStrA.append("F000, F000, 0F00, 00F0")
cubeStrA.append("F000, F000, F000, 0F00")
cubeStrA.append("F000, F000, F000, F000")

cubeStrFun(cubeStrA)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("F000, 0F00, 00F0, 000F")
cubeFun("shiftUp", 24)

#----------------------------------------------------------------------
#Create cubes and animation data

cubeStr.append("0000, 0000, 0000, FFFF")
cubeFun("shiftUp", 12)

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("9999, 6666, 0000, 0000")
cubeFun("shiftDown", 12)

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("FF00, FF00, FF00, FF00")
cubeFun("mixDown", 12)

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("FF00, FF00, FF00, FF00")
cubeFun("mixUp", 12)

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("1111, 1111, 1111, 1111")
cubeFun("fig8Z", 48)

#----------------------------------------------------------------------
#Create cubes and animation data
cubeStr.append("F000, F000, F000, F000")
cubeFun("fig8Z", 48)

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
# Print pointers to Led objects
if(0):
    for i, c in enumerate(cubes):
        print("\nCube#: ", i, "Size: ", c[0].seqSize)
        for n, a in enumerate(c):
            print(n, " : ", a)
            a.printCube()

#----------------------------------------------------------------------
# Create list of sequence sizes
seqSizes = [c[0].seqSize for c in cubes]
print("\nSequence Sizes: ", seqSizes)

# Flatten Cube List for animation
cubePlots = [p for sl in cubes for p in sl]

#----------------------------------------------------------------------
# Generate and print asm data

print("\nGenerating ASM data")

asmData = []
for i, c in enumerate(cubes):
    print("Seq"+ str(i)+':\n.db    '+ hex(seqSizes[i]) + "  //Sequence Size" )
    for H in c:
        asmHex = H.asm()
        asmData.append(asmHex)
        print(asmHex)
    print()

#----------------------------------------------------------------------
# Printing Hex Data Size
print("\n//ASM data Length: ", len(asmData) * 8, "\n\n")

#----------------------------------------------------------------------
# Plotting animation data
animCount = 0
ani = animation.FuncAnimation(fig, animLED, interval=100)
plt.show()


