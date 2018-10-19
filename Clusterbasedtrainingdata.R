###file to use clusters to build trainingdataset

setwd("~/GitHub/UnsupCollar/DTWKmeansAccel")

#lying down.

for (j in (c()))
numdat = 200
longestclust = 0
longlen = 0
for (i in c(1:length(AssignmentsCollar10))){
  print(longestclust)
  clustlen = length(AssignmentsCollar10[!is.na(AssignmentsCollar10[i]),i])
  print(clustlen)
  if(clustlen > longlen){
    longestclust = i
    longlen = clustlen
  }

}

liedownlist = list()
liedowndat = data.frame()
i = 1
while(i < numdat){

  ind = AssignmentsCollar10[sample(nrow(AssignmentsCollar10), 1),longestclust]
  if (ind < 300){
  next}
  extr = c((ind-300):(ind+300))
  
  if(abs(max(Collar10Accel[extr,4]) - min(Collar10Accel[extr,4]))>1){
    next
  }else{liedownlist[[i]] <- Collar10Accel[extr,] 
        i = i + 1}
  
  if(i == numdat){
    for (x in c(1:length(liedownlist))){
    liedowndat <- rbind(liedowndat,liedownlist[[x]])}
    rm(liedownlist)
  }
}
