start = [[0] * 16] * 34

AA = 0
ZZ = 0
A1 = 1
A2 = 2
A3 = 3
A4 = 4
B1 = 5
B2 = 6
B3 = 7
B4 = 8
C1 = 9
C2 = 10
C3 = 11
C4 = 12
D1 = 13
D2 = 14
D3 = 15
D4 = 16
E1 = 17
E2 = 18
E3 = 19
E4 = 20
F1 = 21
F2 = 22
F3 = 23
F4 = 24
G1 = 25
G2 = 26
G3 = 27
G4 = 28
H1 = 29
H2 = 30
H3 = 31
H4 = 32
I1 = 33
I2 = 34
I3 = 35
I4 = 36
J1 = 37
J2 = 38
J3 = 39
J4 = 40
K1 = 41
K2 = 42
K3 = 43
K4 = 44
L1 = 45
L2 = 46
L3 = 47
L4 = 48
M1 = 49
M2 = 50
M3 = 51
M4 = 52
N1 = 53
N2 = 54
N3 = 55
N4 = 56
O1 = 57
O2 = 58
O3 = 59
O4 = 60
P1 = 61
P2 = 62
P3 = 63
P4 = 64
Q1 = 65
Q2 = 66
Q3 = 67
Q4 = 68
R1 = 69
R2 = 70
R3 = 71
R4 = 72
S1 = 73
S2 = 74
S3 = 75
S4 = 76
T1 = 77
T2 = 78
T3 = 79
T4 = 80

land_map = [
    'ABCDABCD',  # ____ABCD AB__CDAB ABAB__AB
    '___HEFGH',  # ____EFGH ____GHEF
    '___BCD__',  # _B______ ____AB__
    '___FGH__',  # _F______ ____CD__
    '________',  # __AB__AB ______AB
    '________',  # ________ ________
    '________',  # ________ ________
    'EF__EF__',  # ________ __C_____
    '__AB____',  # ________ ________
    '__EF____',  # ________ ________
    '__CDAB__',  # ________ ________
    '__GHE___',  # ________ ________
    '__AB____',  # ________ AB______
    '__EF____',  # ________ ________
    'A_ABAB__',  # ________ ________
    'E_EFEF__',  # ________ __EF____
    '__AB__AB',  # ________ ____AB__
    '__EF__EF',  # ________ ____EF__
    'CD__CD__',  # ________ ____CD__
    'GH__GH__',  # ________ ____GH__
    '___B____',  # __AB____ ________
    '___F____',  # __EF____ ________
    '__AB____',  # ________ AB____AB
    '__EF____',  # ________ EF____EF
    '____A___',  # __CDAB__ CDAB____
    '____E___',  # __GHEF__ GHEF____
    '__AB____',  # AB__CDAB ________
    '________',  # EF__GHEF ________
    '________',  # CD__AB__ AB__AB__
    'EF______',  # EF__CD__ ________
    'CDAB__AB',  # ________ ________
    'GHEF___F',  # ________ ________
    'AB__A___',  # CD______ ________
    'EF__E___',  # EF______ ________
]

level_map = [
    *start,
    A1, A2, B1, B2, C1, C2, D1, D2, A1, A2, B1, B2, C1, C2, D1, D2,
    A3, A4, B3, B4, C3, C4, D3, D4, A3, A4, B3, B4, C3, C4, D3, D4,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, E1, E2, F1, F2, G1, G2, H1, H2, E1, E2,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, E3, E4, F3, F4, G3, G4, H3, H4, E3, E4,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, B1, B2, C1, C2, D1, D2, I1, I2, J1, J2,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, B3, B4, C3, C4, D3, D4, I3, I4, J3, J4,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, G1, G2, H1, H2, E1, E2, K1, K2, L1, L2,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, G3, G4, H3, H4, E3, E4, K3, K4, L3, L4,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, AA, AA, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, AA, AA, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    F1, F2, G1, G2, AA, AA, AA, AA, F1, ZZ, ZZ, G2, AA, AA, AA, AA,
    F3, F4, G3, G4, AA, AA, AA, AA, F3, ZZ, ZZ, G4, AA, AA, AA, AA,
    M1, M2, N1, N2, A1, A2, B1, B2, AA, ZZ, ZZ, AA, AA, AA, AA, AA,
    M3, M4, N3, N4, A3, A4, B3, B4, AA, ZZ, ZZ, AA, AA, AA, AA, AA,
    O1, O2, P1, P2, F1, F2, G1, G2, AA, ZZ, ZZ, AA, AA, AA, AA, AA,
    O3, O4, P3, P4, F3, F4, G3, G4, AA, ZZ, ZZ, AA, AA, AA, AA, AA,
    Q1, Q2, R1, R2, C1, C2, D1, D2, A1, ZZ, ZZ, B2, AA, AA, AA, AA,
    Q3, Q4, R3, R4, C3, C4, D3, D4, A3, ZZ, ZZ, B4, AA, AA, AA, AA,
    S1, S2, T1, T2, H1, H2, E1, E2, F1, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    S3, S4, T3, T4, H3, H4, E3, E4, F3, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ, ZZ,
    I1, I2, J1, J2, A1, A2, B1, B2, AA, AA, AA, AA, Q1, Q2, R1, R2,
    I3, I4, J3, J4, A3, A4, B3, B4, AA, AA, AA, AA, Q3, Q4, R3, R4,
    J1, J2, K1, K2, F1, F2, G1, G2, AA, AA, AA, AA, S1, S2, T1, T2,
    J3, J4, K3, K4, F3, F4, G3, G4, AA, AA, AA, AA, S3, S4, T3, T4,

]