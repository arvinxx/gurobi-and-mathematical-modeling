\ Model Complex Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  8 x[0] + 10 x[1] + 6 x[2] + 6 x[3] + 11 x[4] + 9 x[5]
Subject To
 R0: 12 x[0] + 9 x[1] + 25 x[2] + 20 x[3] + 17 x[4] + 13 x[5] >= 60
 R1: 35 x[0] + 42 x[1] + 18 x[2] + 31 x[3] + 56 x[4] + 49 x[5] >= 150
 R2: 37 x[0] + 53 x[1] + 28 x[2] + 24 x[3] + 29 x[4] + 20 x[5] >= 125
Bounds
 x[0] <= 1
 x[1] <= 1
 x[2] <= 1
 x[3] <= 1
 x[4] <= 1
 x[5] <= 1
End
