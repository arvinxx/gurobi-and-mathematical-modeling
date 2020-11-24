\ Model Activity
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  used[0] + used[1] + 2 used[2]
Subject To
 mustXorY: used[0] + used[1] >= 1
 timeLimit: used[0] + 2 used[1] + 3 used[2] = 4
Bounds
Binaries
 used[0] used[1] used[2]
End
