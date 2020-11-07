"""
FYP : Wireless Transmission using LDPC Codes
@author: Bhushan Mhatre
"""

# Importing Libraries
import numpy as np
import pyldpc
import tkinter

def calhmat():
    
    num = 15       # Number of columns
    dv = 4         # Number of ones per column, must be lower than d_c (because H must have more rows than columns)
    dc = 5         # Number of ones per row, must divide n (because if H has m rows: m*d_c = n*d_v (compute number of ones in H))
    
    # H Matrix
    H = pyldpc.RegularH(num,dv,dc)
    
    # G Matrix
    tG = pyldpc.CodingMatrix(H)
    
    n,k = tG.shape     # n = 15, k = 6
    snr = 8

window = tkinter.Tk()
window.title("LDPC Transmitter")
window.geometry("900x700")

label = tkinter.Label(window, text = "Receiver", font = ('arial', 25, 'bold'), pady=10).pack()

messlab = tkinter.Label(window, text = "The message received is:", font = ('arial', 20, 'bold'), pady=5).pack()

window.mainloop()
