
# coding: utf-8

# In[ ]:

class Led:
    seqSize = -1
    LEDplot = [[], [], []]

    def __init__(self):
        # print("Creating new cube")
        self.cube = self.newCube(4, 4, 4)
        Led.seqSize = 1
        self.funs = self.ledFuns()

    def newCube(self, a, b, c):
        return [[ ['o' for col in range(a)] for col in range(b)] for row in range(c)]

    def ledFuns(self):
        return  {
                    "newCube": self.newCube,
                    "ledScatter": self.ledScatter,
                    "cp": self.cp,
                    "cubify": self.cubify,
                    "printCube": self.printCube,
                    "asm": self.asm,
                    "rotateZccw": self.rotateZccw,
                    "rotateZcw": self.rotateZccw,
                    "rotateYccw": self.rotateYccw,
                    "rotateYcw": self.rotateYcw,
                    "rotateXccw": self.rotateYccw,
                    "rotateXcw": self.rotateXccw,
                    "shiftUp": self.shiftUp,
                    "shiftDown": self.shiftDown,
                    "mixDown": self.mixDown,
                    "mixUp": self.mixUp,
                    "fig8Z": self.fig8Z
                    }

    def ledScatter(self):
        '''Create X, Y and Z lists of coordinates where matrix cell == 1 for
        scatterplot'''
        self.LEDplot = [[], [], []]
        for i in range(64):
            l = int(i/16)
            r = int(i % 16 / 4)
            c = int(i % 4)
            if self.cube[l][r][c]:
                self.LEDplot[0].append(l)
                self.LEDplot[1].append(r)
                self.LEDplot[2].append(c)

    def cp(self):
        ''' Create new list and copy values from self to new list'''
        newObj = Led()
        newObj.cube = self.cube.copy()
#        self.ledScatter()
#        newObj.ledScatter()
        return newObj

    def cubify(self, cubeStr):
        '''Create binary cube with each cell filled with 1 or 0 as defined by
        string of hexadecimal values.  Each 4 digit hex value defines one
        layer of the cube.
        Example Hex String: "F99F, 9609, 9069, 900F"
        LEDmat = cube3D(4, 4, 4)'''
        for l, H16 in enumerate(cubeStr.split(', ')):
            H8H = H16[0:2]
            H8L = H16[2:]
            b8H = bin(int("0x"+H16[0:2],16))[2:].zfill(8)
            b8L = bin(int("0x"+H16[2:],16))[2:].zfill(8)
        #    print(H8H, "  _  ", H8L, b8H , b8L)
            for r in range(4):
                for c in range(4):
                    self.cube[l][r][c] = int((b8H+b8L)[r*4+c])
        self.ledScatter()

    # Print Cube 
    def printCube(self):
        for r in range(4):
            for l in range(4):
                print(self.cube[l][r][0]  , end='  ')
                print(self.cube[l][r][1]  , end='  ')
                print(self.cube[l][r][2]  , end='  ')
                print(self.cube[l][r][3]  , end='  ')
                print('     ', end='    ')
            print('\n')

    def asm(self):
        self.cubeHex = ".db    "
        for i, layer in enumerate(self.cube):
            R12 = layer[0] + layer[1]
            R34 = layer[2] + layer[3]
            hex12 = hex(int("".join([str(ch) for ch in R12]),2))
            hex34 = hex(int("".join([str(ch) for ch in R34]),2))
            self.cubeHex += (hex12 + ', ' + hex34 + (', ' if i < 3 else '')).upper()
        return self.cubeHex

# ------------------------------------------------------------------------------
    def rotateZccw(self):
        '''Rotate Cube counterclockwise from TOP view '''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            T = self.cube[L][0][0]
            cuben[L][0][0] = self.cube[L][0][1]
            cuben[L][0][1] = self.cube[L][0][2]
            cuben[L][0][2] = self.cube[L][0][3]
            cuben[L][0][3] = self.cube[L][1][3]
            cuben[L][1][3] = self.cube[L][2][3]
            cuben[L][2][3] = self.cube[L][3][3]
            cuben[L][3][3] = self.cube[L][3][2]
            cuben[L][3][2] = self.cube[L][3][1]
            cuben[L][3][1] = self.cube[L][3][0]
            cuben[L][3][0] = self.cube[L][2][0]
            cuben[L][2][0] = self.cube[L][1][0]
            cuben[L][1][0] = T
            T = self.cube[L][1][1]
            cuben[L][1][1] = self.cube[L][1][2]
            cuben[L][1][2] = self.cube[L][2][2]
            cuben[L][2][2] = self.cube[L][2][1]
            cuben[L][2][1] = T
        self.cube = cuben.copy()

    def rotateZcw(self):
        '''Rotate Cube clockwise from TOP view '''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            T = self.cube[L][0][0]
            cuben[L][0][0] = self.cube[L][1][0]
            cuben[L][1][0] = self.cube[L][2][0]
            cuben[L][2][0] = self.cube[L][3][0]
            cuben[L][3][0] = self.cube[L][3][1]
            cuben[L][3][1] = self.cube[L][3][2]
            cuben[L][3][2] = self.cube[L][3][3]
            cuben[L][3][3] = self.cube[L][2][3]
            cuben[L][2][3] = self.cube[L][1][3]
            cuben[L][1][3] = self.cube[L][0][3]
            cuben[L][0][3] = self.cube[L][0][2]
            cuben[L][0][2] = self.cube[L][0][1]
            cuben[L][0][1] = T
            T = self.cube[L][1][1]
            cuben[L][1][1] = self.cube[L][2][1]
            cuben[L][2][1] = self.cube[L][2][2]
            cuben[L][2][2] = self.cube[L][1][2]
            cuben[L][1][2] = T
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------
    def rotateXccw(self):
        '''Rotate Cube counterclockwise from LEFT view '''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            T = self.cube[0][0][L]
            cuben[0][0][L] = self.cube[1][0][L]
            cuben[1][0][L] = self.cube[2][0][L]
            cuben[2][0][L] = self.cube[3][0][L]
            cuben[3][0][L] = self.cube[3][1][L]
            cuben[3][1][L] = self.cube[3][2][L]

            cuben[0][0][L] = self.cube[1][0][L]
            cuben[1][0][L] = self.cube[2][0][L]
            cuben[2][0][L] = self.cube[3][0][L]
            cuben[3][0][L] = self.cube[3][1][L]
            cuben[3][1][L] = self.cube[3][2][L]
            cuben[3][2][L] = self.cube[3][3][L]
            cuben[3][3][L] = self.cube[2][3][L]
            cuben[2][3][L] = self.cube[1][3][L]
            cuben[1][3][L] = self.cube[0][3][L]
            cuben[0][3][L] = self.cube[0][2][L]
            cuben[0][2][L] = self.cube[0][1][L]
            cuben[0][1][L] = T
            T = self.cube[1][1][L]
            cuben[1][1][L] = self.cube[2][1][L]
            cuben[2][1][L] = self.cube[2][2][L]
            cuben[2][2][L] = self.cube[1][2][L]
            cuben[1][2][L] = T
        self.cube = cuben.copy()

    def rotateXcw(self):
        '''Rotate Cube clockwise from LEFT view '''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            T = self.cube[0][0][L]
            cuben[0][0][L] = self.cube[0][1][L]
            cuben[0][1][L] = self.cube[0][2][L]
            cuben[0][2][L] = self.cube[0][3][L]
            cuben[0][3][L] = self.cube[1][3][L]
            cuben[1][3][L] = self.cube[2][3][L]
            cuben[2][3][L] = self.cube[3][3][L]
            cuben[3][3][L] = self.cube[3][2][L]
            cuben[3][2][L] = self.cube[3][1][L]
            cuben[3][1][L] = self.cube[3][0][L]
            cuben[3][0][L] = self.cube[2][0][L]
            cuben[2][0][L] = self.cube[1][0][L]
            cuben[1][0][L] = T
            T = self.cube[1][1][L]
            cuben[1][1][L] = self.cube[1][2][L]
            cuben[1][2][L] = self.cube[2][2][L]
            cuben[2][2][L] = self.cube[2][1][L]
            cuben[2][1][L] = T
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------

    def rotateYccw(self):
        '''Rotate Cube counterclockwise from FRONT view '''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            T = self.cube[0][L][0]
            cuben[0][L][0] = self.cube[0][L][1]
            cuben[0][L][1] = self.cube[0][L][2]
            cuben[0][L][2] = self.cube[0][L][3]
            cuben[0][L][3] = self.cube[1][L][3]
            cuben[1][L][3] = self.cube[2][L][3]
            cuben[2][L][3] = self.cube[3][L][3]
            cuben[3][L][3] = self.cube[3][L][2]
            cuben[3][L][2] = self.cube[3][L][1]
            cuben[3][L][1] = self.cube[3][L][0]
            cuben[3][L][0] = self.cube[2][L][0]
            cuben[2][L][0] = self.cube[1][L][0]
            cuben[1][L][0] = T
            T = self.cube[1][L][1]
            cuben[1][L][1] = self.cube[1][L][2]
            cuben[1][L][2] = self.cube[2][L][2]
            cuben[2][L][2] = self.cube[2][L][1]
            cuben[2][L][1] = T
        self.cube = cuben.copy()

    def rotateYcw(self):
        '''Rotate Cube clockwise from FRONT view '''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            # T = self.cube[0][L][0]
            cuben[0][L][0] = self.cube[1][L][0]
            cuben[1][L][0] = self.cube[2][L][0]
            cuben[2][L][0] = self.cube[3][L][0]
            cuben[3][L][0] = self.cube[3][L][1]
            cuben[3][L][1] = self.cube[3][L][2]
            cuben[3][L][2] = self.cube[3][L][3]
            cuben[3][L][3] = self.cube[2][L][3]
            cuben[2][L][3] = self.cube[1][L][3]
            cuben[1][L][3] = self.cube[0][L][3]
            cuben[0][L][3] = self.cube[0][L][2]
            cuben[0][L][2] = self.cube[0][L][1]
            cuben[0][L][1] = self.cube[0][L][0]

            # T = self.cube[1][L][1]
            cuben[1][L][1] = self.cube[2][L][1]
            cuben[2][L][1] = self.cube[2][L][2]
            cuben[2][L][2] = self.cube[1][L][2]
            cuben[1][L][2] = self.cube[1][L][1]
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------
    def shiftUp(self):
        '''Rotate layers up; Top layer copied to bottom layer'''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            cuben[L] = self.cube[(L+1)%4]
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------

    def shiftDown(self):
        '''Rotate layers up; Top layer copied to bottom layer'''
        cuben = self.newCube(4, 4, 4)
        for L in range(4):
            cuben[(L+1)%4] = self.cube[L]
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------

    def mixDown(self):
        '''Rotate Cube counterclockwise from TOP view '''
        cuben = self.newCube(4, 4, 4)
        ocSeq = [4, 0, 3, 7, 8, 1, 2, 11, 12, 5, 6, 15, 13, 9, 10, 14]
        for L in range(4):
            for nc, oc in enumerate(ocSeq):
                cuben[L][int(nc/4)][nc%4] = self.cube[L][int(oc/4)][oc%4]
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------

    def mixUp(self):
        '''Rotate Cube counterclockwise from TOP view '''
        cuben = self.newCube(4, 4, 4)
        ocSeq = [1, 5, 6, 2, 0, 9, 10, 3, 4, 13, 14, 7, 8, 12, 15, 11]
        for L in range(4):
            for nc, oc in enumerate(ocSeq):
                cuben[L][int(nc/4)][nc%4] = self.cube[L][int(oc/4)][oc%4]
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------

    def fig8Z(self):
        '''Figure 8 from TOP view '''
        cuben = self.newCube(4, 4, 4)
        ocSeq = [1, 5, 6, 2, 0, 10, 9, 3, 4, 13, 14, 7, 8, 12, 15, 11]
        for L in range(4):
            for nc, oc in enumerate(ocSeq):
                cuben[L][int(nc/4)][nc%4] = self.cube[L][int(oc/4)][oc%4]
        self.cube = cuben.copy()

# ------------------------------------------------------------------------------

