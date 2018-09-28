
# coding: utf-8

# In[ ]:

class Led:
    seq = -1
    LEDplot = [[], [], []]

    def __init__(self):
        # print("Creating new cube")
        self.cube = self.newcube(4, 4, 4)
        Led.seq += 1

    def newcube(self, a, b, c):
        return [[ ['o' for col in range(a)] for col in range(b)] for row in range(c)]
        # self.cube = [[ ['o' for col in range(a)] for col in range(b)] for row in range(c)]

    def ledScatter(self):
    '''Create X, Y and Z lists of coordinates where matrix cell == 1 for scatterplot'''
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
        '''Create binary cube with each cell filled with 1 or 0 as defined by string of
              hexadecimal values.  Each 4 digit hex value defines one layer of the cube.
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

    def rotateCCW(self):
        cuben = self.newcube(4, 4, 4)
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

# ------------------------------------------------------------------------------
    def rotateCW(self):
        cuben = self.newcube(4, 4, 4)
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


