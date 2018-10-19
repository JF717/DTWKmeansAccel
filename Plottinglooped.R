setwd("~/GitHub/UnsupCollar/DTWKmeansAccel")
library(ggplot2)
library(gridExtra)
library(grid)
library(lattice)

for (j in (1:14)){
  assign(paste("plts",sep=""),list())
  collarname <- paste("Collar",j,"AccelCor.csv", sep = "") 
  try(assign(paste("Collar",j,"Accel" ,sep = ""), read.csv(collarname, na.strings=c('NA'), header = T )))
  
  #create a filename for each collar and read in the data
  for (i in (1:10)){
  filename <- paste("Cluster",i,"Collar",j,".csv", sep = "") 
  try(assign(paste("cluster",i,"c",j,sep = ""), read.csv(filename, na.strings=c('NA'), header = T )))
  filename <- paste("Cluster",i,"C",j,".csv", sep = "") 
  try(assign(paste("cluster",i,"c",j,sep = ""), read.csv(filename, na.strings=c('NA'), header = T )))
  
  curclust <- paste("cluster",i,"c",j,sep = "")
  try(obj <- get(curclust))

  try(colnames(obj) <- c("Ind","X","Y","Z"))
  try(plts[[i]] <- ggplot()+
           theme_bw()+
           ggtitle(paste("Cluster",i))+
           geom_line(data =obj, aes(Ind, X),color = "Blue")+
           geom_line(data =obj, aes(Ind, Y),color = "Red")+
           geom_line(data =obj, aes(Ind, Z), color = "Green")+
           ylim(c(-40,40)))
  try(rm(curclust))
  try(rm(obj))
  }
  try(assign(paste("Collar",j,"ClusterPlots",sep=""),do.call(grid.arrange,plts)))
  try(rm(plts))
  try(assinam <- paste("Collar",j,"Assignments.csv",sep=""))
  try(assign(paste("AssignmentsCollar",j,sep=""), read.csv(assinam, header = T)))
  
}

ggplot()+
  theme_bw()+
  geom_line(data = Collar2Accel, aes(X, obj.X),color = "Blue")+
  geom_line(data =  Collar2Accel, aes(X, obj.Y),color = "Red")+
  geom_line(data =  Collar2Accel, aes(X, obj.Z), color = "Green")+
  xlim(c(4149500,4151200))+
  ylim(c(-40,40))


