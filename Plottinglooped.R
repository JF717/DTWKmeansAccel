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

row.names(rundat) <- c(1:nrow(rundat))
rundat$rid <- as.numeric(row.names(rundat))

ggplot()+
  theme_bw()+
  geom_line(data = rundat, aes(rid, obj.X),color = "Blue")+
  geom_line(data =  rundat, aes(rid, obj.Y),color = "Red")+
  geom_line(data = rundat, aes(rid, obj.Z), color = "Green")+
  ylim(c(-40,40))+
  xlim(c(12000,12100))


row.names(walkdat) <- c(1:nrow(walkdat))
walkdat$rid <- as.numeric(row.names(walkdat))

ggplot()+
  theme_bw()+
  geom_line(data = walkdat, aes(rid, obj.X),color = "Blue")+
  geom_line(data =  walkdat, aes(rid, obj.Y),color = "Red")+
  geom_line(data = walkdat, aes(rid, obj.Z), color = "Green")+
  ylim(c(-40,40))
  xlim(c(15000,15100))
  
  
row.names(foragedat) <- c(1:nrow(foragedat))
foragedat$rid <- as.numeric(row.names(foragedat))
  
  ggplot()+
    theme_bw()+
    geom_line(data = foragedat, aes(rid, obj.X),color = "Blue")+
    geom_line(data =  foragedat, aes(rid, obj.Y),color = "Red")+
    geom_line(data = foragedat, aes(rid, obj.Z), color = "Green")+
    ylim(c(-40,40))+
  xlim(c(15000,15100))
  
row.names(sitdat) <- c(1:nrow(sitdat))
sitdat$rid <- as.numeric(row.names(sitdat))
  
ggplot()+
    theme_bw()+
    geom_line(data = sitdat, aes(rid, obj.X),color = "Blue")+
    geom_line(data =  sitdat, aes(rid, obj.Y),color = "Red")+
    geom_line(data = sitdat, aes(rid, obj.Z), color = "Green")+
    ylim(c(-40,40))+
    xlim(c(15000,15100))

sitdat$rid <- NULL
