\ Model diet
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2.49 buy[hamburger] + 2.89 buy[chicken] + 1.5 buy[hot_dog]
   + 1.89 buy[fries] + 2.09 buy[macaroni] + 1.99 buy[pizza]
   + 2.49 buy[salad] + 0.89 buy[milk] + 1.59 buy[ice_cream]
Subject To
 xxxxxx[calories]: 410 buy[hamburger] + 420 buy[chicken] + 560 buy[hot_dog]
   + 380 buy[fries] + 320 buy[macaroni] + 320 buy[pizza] + 320 buy[salad]
   + 100 buy[milk] + 330 buy[ice_cream] + Rgxxxxxx[calories] = 2200
 xxxxxx[protein]: 24 buy[hamburger] + 32 buy[chicken] + 20 buy[hot_dog]
   + 4 buy[fries] + 12 buy[macaroni] + 15 buy[pizza] + 31 buy[salad]
   + 8 buy[milk] + 8 buy[ice_cream] >= 91
 xxxxxx[fat]: 26 buy[hamburger] + 10 buy[chicken] + 32 buy[hot_dog]
   + 19 buy[fries] + 10 buy[macaroni] + 12 buy[pizza] + 12 buy[salad]
   + 2.5 buy[milk] + 10 buy[ice_cream] + Rgxxxxxx[fat] = 65
 xxxxxx[sodium]: 730 buy[hamburger] + 1190 buy[chicken] + 1800 buy[hot_dog]
   + 270 buy[fries] + 930 buy[macaroni] + 820 buy[pizza] + 1230 buy[salad]
   + 125 buy[milk] + 180 buy[ice_cream] + Rgxxxxxx[sodium] = 1779
 calories: 410 buy[hamburger] + 420 buy[chicken] + 560 buy[hot_dog]
   + 380 buy[fries] + 320 buy[macaroni] + 320 buy[pizza] + 320 buy[salad]
   + 100 buy[milk] + 330 buy[ice_cream] + Rgcalories = 2200
 protein: 24 buy[hamburger] + 32 buy[chicken] + 20 buy[hot_dog]
   + 4 buy[fries] + 12 buy[macaroni] + 15 buy[pizza] + 31 buy[salad]
   + 8 buy[milk] + 8 buy[ice_cream] >= 91
 fat: 26 buy[hamburger] + 10 buy[chicken] + 32 buy[hot_dog] + 19 buy[fries]
   + 10 buy[macaroni] + 12 buy[pizza] + 12 buy[salad] + 2.5 buy[milk]
   + 10 buy[ice_cream] + Rgfat = 65
 sodium: 730 buy[hamburger] + 1190 buy[chicken] + 1800 buy[hot_dog]
   + 270 buy[fries] + 930 buy[macaroni] + 820 buy[pizza] + 1230 buy[salad]
   + 125 buy[milk] + 180 buy[ice_cream] + Rgsodium = 1779
Bounds
 Rgxxxxxx[calories] <= 400
 Rgxxxxxx[fat] <= 65
 Rgxxxxxx[sodium] <= 1779
 Rgcalories <= 400
 Rgfat <= 65
 Rgsodium <= 1779
End
