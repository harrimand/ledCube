
import numpy as np

from os import system
cls = lambda: system("clear")

CubeSeq = lambda n: np.reshape(np.arange(0,n**3),[n,n,n])

C = np.reshape(np.arange(0,125),[5,5,5])

spin = lambda cm,n: np.array([[np.roll(r,n) for r in cm]])
twist = lambda cm: np.flipud(np.rot90(cm[0]))


def proll(C,p,n):
    ct = C[:p,:,:]
    cm = C[p:p+1,:,:]
    cb = C[p+1:,:,:]
    cm = np.array([[np.roll(r,1) for r in cm[0]]])

C = CubeSeq(4)
D = np.copy(C)
[D[2,:,2],D[2,:,1],D[1,:,2],D[1,:,1]]=[C[1,:,1],C[1,:,2],C[2,:,1],C[2,:,2]]

def mvr(C, to, fr):
"""mvr(C,[5,6], [10,9]) where C = 4x4x4 cube
    move cells on all columns to 5 frromm 10 and to 6 from 9
    select 1 page and 1 row
    pages 0..3, rows 0..3 columns 0..3
    page = [to,,fr] // 4  5 = page 1
    row  = [to,fr] %  4   5 = row 1
    col = all columns
"""
    D = np.copy(C)
    sz = np.size(C[0][0])
    for t, f in zip(to, fr):
        pt = np.floor_divide(t, 4)
        rt = t % sz
        pf = np.floor_divide(f, 4)
        rf = f % sz
        D[pt,rt,:] = C[pf,rf,:]
    return D

def mvc(C, to, fr):
"""mvr(C,[5,6], [10,9]) where C = 4x4x4 cube
    move cells on all rows to 5 frromm 10 and to 6 from 9
    select 1 page and 1 column
    pages 0..3, rows 0..3 columns 0..3
    page = [to,,fr] // 4  10 = page 2
    row = all rows
    col  = [to,fr] %  4   10 = column 2
"""
    D = np.copy(C)
    sz = np.size(C[0][0])
    for t, f in zip(to, fr):
        pt = np.floor_divide(t, 4)
        ct = t % sz
        pf = np.floor_divide(f, 4)
        cf = f % sz
        D[pt,:,ct] = C[pf,:,cf]
    return D

def mvp(C, to, fr):
"""mvr(C,[5,6], [10,9]) where C = 4x4x4 cube
    move cells on all pages to 5 from 10 and to 6 from 9
    select 1 row and 1 column
    pages 0..3, rows 0..3 columns 0..3
    page = all pages
    row = [to,,fr] // 4  9 = row 2
    col  = [to,fr] %  4  9 =  column 1
"""
    D = np.copy(C)
    sz = np.size(C[0][0])
    for t, f in zip(to, fr):
        rt = np.floor_divide(t, 4)
        ct = t % sz
        rf = np.floor_divide(f, 4)
        cf = f % sz
        D[:,rt,ct] = C[:,rf,cf]
    return D




