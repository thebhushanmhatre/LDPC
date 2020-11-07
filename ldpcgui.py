"""
FYP : Wireless Transmission using LDPC Codes
@author: Bhushan Mhatre
"""

# Importing Libraries
import numpy as np
import pyldpc
import tkinter

# Functions 
def BreakingMessage(binmess, k, messlen):
    i = 0
    messarr = []
    while messlen >= k :
        messarr.append(binmess[i:i+k])
        i = i+k
        messlen = messlen-k
    if(messlen > 0):
        messarr.append(binmess[i:].zfill(k))
    return messarr

def CodingMessage(messarr, tG, snr, k):
    y = []
    for i in messarr:
        v = [int(d) for d in i]
        y.append(pyldpc.Coding(tG,v,snr))
    return y
    


def calhmat():
    binmess = ''.join(format(ord(x), 'b') for x in mess.get())
    temp =  "\nMessage '"+str(mess.get())+"' in Binary format is: "
    tkinter.Label(window, text = temp, font = ('ubuntu', 15, 'bold')).pack()
    tkinter.Label(window, text = binmess, font = ('ubuntu', 15, 'bold')).pack()
    
    num = 15       # Number of columns
    dv = 4         # Number of ones per column, must be lower than d_c (because H must have more rows than columns)
    dc = 5         # Number of ones per row, must divide n (because if H has m rows: m*d_c = n*d_v (compute number of ones in H))
    
    # H Matrix
    H = pyldpc.RegularH(num,dv,dc)
    
    # G Matrix
    tG = pyldpc.CodingMatrix(H)
    
    n,k = tG.shape     # n = 15, k = 6
    snr = 8
    messlen = len(binmess)
    messarr = BreakingMessage(binmess, k, messlen)
    print("Messarr = ", messarr)
    
    op = CodingMessage(messarr, tG, snr, k)
    print(op)
    
    temp2 = "Modulates Message to be sent is :\n "+str(op)
    tkinter.Label(window, text = temp2, font = ('ubuntu', 15, 'bold')).pack()

#    print("Full Message is --> ",binmess)
#    print("Size is --> ", len(binmess))    
#    print(messarr)
#    print("Shape of H: ", H.shape)
#    print("Shape of tG: ", tG.shape)
#    print("Binary message: ", binmess," in String format")
#    tkinter.Label(window, text = "Just for Reference: ").pack()
#    
#    str = "Regular parity-check matrix H({},{},{}):".format(num,dv,dc)
#    tkinter.Label(window, text = str).pack()
#    tkinter.Label(window, text = H).pack()
#
#    gstr = "\nTransposed Coding Matrix tG that goes with H above is:"
#    tkinter.Label(window, text = gstr).pack()
#    tkinter.Label(window, text = tG).pack()
#    
#    mstr = "\n With G,H you can code messages of {} bits into codewords of {} bits because G's shape is {}\n".format(tG.shape[1], tG.shape[0], tG.T.shape)
#    tkinter.Label(window, text = mstr).grid(row = 6, column = 2)

window = tkinter.Tk()
window.title("LDPC Transmitter")
window.geometry("900x700")

label = tkinter.Label(window, text = "Transmitter", font = ('arial', 25, 'bold'), pady=10).pack()

messlab = tkinter.Label(window, text = "Enter the message to be transmitted:", font = ('arial', 20, 'bold'), pady=5).pack()
mess = tkinter.Entry(window, font = ('arial', 25, 'bold'), width = 20, bg = "#ccc", bd = 3)
mess.pack()

tkinter.Button(window, text = "SEND IT", command = calhmat, bd=10, font = ('ubuntu', 15, 'bold'), pady=5).pack()

window.mainloop()
