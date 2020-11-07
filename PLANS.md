#   Wireless Transmission using LDPC codes
#
#   Bhushan Mhatre   1510900xx
#   Ankit Panchal    1510900xx
#
#   B.Tech EXTC
#   V.J.T.I.

# Algorithm 1 MacKay Neal LDPC Codes

1: procedure MN CONSTRUCTION(n,r,v,h) ⊲ Required length, rate and degree distributions
2: H = all zero n(1 − r) × n matrix ⊲ Initialization
3: α = [];
4: for i = 1 : max(v) do
5: for j = 1 : vi × n do
6: α = [α, i]
7: end for
8: end for
9: β = []
10: for i = 1 : max(h) do
11: for j = 1 : hi × m do
12: β = [β, i]
13: end for
14: end for
15:
16: for i = 1 : n do ⊲ Construction
17: c = random subset of β, of size αi
18: for j = 1 : αi do
19: H(cj , i) = 1
20: end for
21: α = α − c
22: end for
23:
24: repeat
25: for i = 1 : n − 1 do ⊲ Remove 4-cycles
26: for j = i + 1 : n do
27: if |H(:, i)
S
H(:, j)| > 1 then
28: permute the entries in the j-th column
29: end if
30: end for
31: end for
32: until cycles removed
33: end procedure




Algorithm 2 Erasure Decoding
1: procedure DECODE(y)
2:
3: I = 0 ⊲ Initialization
4: for i = 1 : n do
5: Mi = yi
6: end for
7: repeat
8:
9: for j = 1 : m do ⊲ Step 1: Check messages
10: for all i ∈ Bj do
11: if all messages into check j other than Mi are known then
12: Ej,i =
P
i′∈Bj ,i′6=i(Mi′ mod 2)
13: else
14: Ej,i = ‘x’
15: end if
16: end for
17: end for
18:
19: for i = 1 : n do ⊲ Step 2: Bit messages
20: if Mi = ‘unknown’ then
21: if there exists a j ∈ Ai s.t. Ej,i 6= ‘x’ then
22: Mi = Ej,i
23: end if
24: end if
25: end for
26:
27: if all Mi known or I = Imax then ⊲ Test
28: Finished
29: else
30: I = I + 1
31: end if
32: until Finished
33: end procedure




Algorithm 3 Bit-flipping Decoding
1: procedure DECODE(y)
2:
3: I = 0 ⊲ Initialization
4: for i = 1 : n do
5: Mi = yi
6: end for
7:
8: repeat
9: for j = 1 : m do ⊲ Step 1: Check messages
10: for i = 1 : n do
11: Ej,i =
P
i′∈Bj ,i′6=i(Mi′ mod 2)
12: end for
13: end for
14:
15: for i = 1 : n do ⊲ Step 2: Bit messages
16: if the messages Ej,i disagree with yi then
17: Mi = (ri + 1 mod 2)
18: end if
19: end for
20:
21: for j = 1 : m do ⊲ Test: are the parity-check
22: Lj =
P
i′∈Bj
(Mi′ mod 2) ⊲ equations satisfied
23: end for
24: if all Lj = 0 or I = Imax then
25: Finished
26: else
27: I = I + 1
28: end if
29: until Finished
30: end procedure




Algorithm 4 Sum-Product Decoding
1: procedure DECODE(r)
2:
3: I = 0 ⊲ Initialization
4: for i = 1 : n do
5: for j = 1 : m do
6: Mj,i = ri
7: end for
8: end for
9:
10: repeat
11: for j = 1 : m do ⊲ Step 1: Check messages
12: for i ∈ Bj do
13: Ej,i = log

1+
Q
i′∈Bj ,i′6=i tanh(Mj,i′/2)
1−
i′∈Bj , i′6=i tanh(Mj,i′/2)

14: end for
15: end for
16:
17: for i = 1 : n do ⊲ Test
18: Li =
P
j∈Ai
Ej,i + ri
19: zi =

1, Li ≤ 0
0, Li > 0.
20: end for
21: if I = Imax or HzT = 0 then
22: Finished
23: else
24: for i = 1 : n do ⊲ Step 2: Bit messages
25: for j ∈ Ai do
26: Mj,i =
P
j′∈Ai, j′6=j Ej′,i + ri
27: end for
28: end for
29: I = I + 1
30: end if
31: until Finished
32: end procedure




