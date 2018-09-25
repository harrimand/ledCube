
# coding: utf-8

# In[ ]:

class Led:
    seq = -1

    def __init__(self):
        print("Creating new cube")
        self.newcube(4, 4, 4)
        Led.seq += 2

    def newcube(self, a, b, c):
        # return [[ ['o' for col in range(a)] for col in range(b)] for row in range(c)]
        self.cube = [[ ['o' for col in range(a)] for col in range(b)] for row in range(c)]
        # return self.cube

    def cubify(self, cubeStr):
        # Create binary cube with each cell filled with 1 or 0 as defined by string of
        #    hexadecimal values.  Each 4 digit hex value defines one layer of the cube.
        # Example Hex String: "F99F, 9609, 9069, 900F"
        # LEDmat = cube3D(4, 4, 4)
        for l, H16 in enumerate(cubeStr.split(', ')):
            H8H = H16[0:2]
            H8L = H16[2:]
            b8H = bin(int("0x"+H16[0:2],16))[2:].zfill(8)
            b8L = bin(int("0x"+H16[2:],16))[2:].zfill(8)
        #    print(H8H, "  _  ", H8L, b8H , b8L)
            for r in range(4):
                for c in range(4):
                    self.cube[l][r][c] = int((b8H+b8L)[r*4+c])

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


