"""
FYP : Wireless Transmission using LDPC Codes
@author: Bhushan Mhatre
"""

# Importing Libraries
import pyldpc
import tkinter

mess = "helloo"

# Functions 
# Breaking Message bits into k bits
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

def DecodingMessage(H, op, snr, tG):
    x = []
    for i in op:
        x_decoded = pyldpc.Decoding_logBP(H, i, snr, 5)
        v_received = pyldpc.DecodedMessage(tG, x_decoded)
        x.append(v_received)
    return x

def decode_binary_string(s):
    return ''.join(chr(int(s[i*7:i*7+7],2)) for i in range(len(s)//7))


# Encoding Message bits
def calhmat():
    binmess = ''.join(format(ord(x), 'b') for x in mess)
#    temp =  "\nMessage '"+str(mess)+"' is sent."
#    tkinter.Label(window, text = temp, font = ('ubuntu', 15, 'bold')).pack()
    
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
    
    op = CodingMessage(messarr, tG, snr, k)
    
    x_dec = DecodingMessage(H, op, snr, tG)
    
    x = ""
    for i in x_dec:
        x1 = [str(j) for j in i]
        x2 = "".join(x1)
        x = x + x2
#    print("b is ", binmess)
    
    print("H matrix is \n", H)
#    print("\n\nG transpose matrix is \n", tG,)
#    print("\nMessarr = \n", messarr)
#    print("\n\nEncoded Message is")
#    print("\n Dimnesion", len(op))
    
    print("\nMessage Received is: ", op)
    
    print("\nThe decoded n-bits codeword is:\n", x)
    
    x_req = decode_binary_string(x)
    print("\nConverting back to text :\n", x_req)
    
    tempor = "Message decoded after receving is : " + x_req
    label = tkinter.Label(window, text = tempor, font = ('arial', 25, 'bold'), pady=10).pack()

window = tkinter.Tk()
window.title("LDPC Transmitter")
window.geometry("900x700")

label = tkinter.Label(window, text = "Receiver", font = ('arial', 25, 'bold'), pady=10).pack()

#messlab = tkinter.Label(window, text = "The message to be transmitted is :\n'Hello'", font = ('arial', 20, 'bold'), pady=5).pack()

tkinter.Button(window, text = "Start Receving", command = calhmat, bd=10, font = ('ubuntu', 15, 'bold'), pady=5).pack()

window.mainloop()
