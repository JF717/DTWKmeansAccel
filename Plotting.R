setwd("~/GitHub/UnsupCollar/DTWKmeansAccel")
library(ggplot2)
cluster10c4 <- read.csv("Cluster10Collar4.csv")
cluster1c4 <- read.csv("Cluster1Collar4.csv)")
cluster2c4 <- read.csv("Cluster2Collar4.csv")
cluster3c4 <- read.csv("Cluster3Collar4.csv")
cluster4c4 <- read.csv("Cluster4Collar4.csv")
cluster5c4 <- read.csv("Cluster5Collar4.csv")
cluster6c4 <- read.csv("Cluster6Collar4.csv")
cluster7c4 <- read.csv("Cluster7Collar4.csv")
cluster8c4 <- read.csv("Cluster8Collar4.csv")
cluster9c4 <- read.csv("Cluster9Collar4.csv")

colnames(cluster10c4) <- c("Ind","X","Y","Z")
colnames(cluster1c4) <- c("Ind","X","Y","Z")
colnames(cluster2c4) <- c("Ind","X","Y","Z")
colnames(cluster3c4) <- c("Ind","X","Y","Z")
colnames(cluster4c4) <- c("Ind","X","Y","Z")
colnames(cluster5c4) <- c("Ind","X","Y","Z")
colnames(cluster6c4) <- c("Ind","X","Y","Z")
colnames(cluster7c4) <- c("Ind","X","Y","Z")
colnames(cluster8c4) <- c("Ind","X","Y","Z")
colnames(cluster9c4) <- c("Ind","X","Y","Z")



c4cl10 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster10c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster10c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster10c4, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c4cl1 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster1c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster1c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster1c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c4cl2 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster2c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster2c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster2c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))


c4cl3 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster3c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster3c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster3c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c4cl4 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster4c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster4c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster4c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))
c4cl5 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster5c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster5c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster5c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))
c4cl6 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster6c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster6c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster6c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c4cl7 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster7c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster7c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster7c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c4cl8 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster8c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster8c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster8c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c4cl9<-ggplot()+
  theme_bw()+
  geom_line(data = cluster9c4, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster9c4, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster9c4, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))


ggplot()+
  theme_bw()+
  geom_line(data = collar4, aes(X, obj.X),color = "Blue")+
  geom_line(data = collar4, aes(X, obj.Y),color = "Red")+
  geom_line(data = collar4, aes(X, obj.Z), color = "Green")+
  xlim(c(200000,236000))
ggplot()+
  theme_bw()+
  geom_line(data = collar4, aes(X, obj.X),color = "Blue")+
  geom_line(data = collar4, aes(X, obj.Y),color = "Red")+
  geom_line(data = collar4, aes(X, obj.Z), color = "Green")+
  xlim(c(211000,211100))

ggplot()+
  theme_bw()+
  geom_line(data = collar10, aes(X, obj.X),color = "Blue")+
  geom_line(data = collar10, aes(X, obj.Y),color = "Red")+
  geom_line(data = collar10, aes(X, obj.Z), color = "Green")+
  xlim(c(100000,136000))



cluster10c10 <- read.csv("Cluster10Collar10.csv")
cluster1c10 <- read.csv("Cluster1Collar10.csv")
cluster2c10 <- read.csv("Cluster2Collar10.csv")
cluster3c10 <- read.csv("Cluster3Collar10.csv")
cluster4c10 <- read.csv("Cluster4Collar10.csv")
cluster5c10 <- read.csv("Cluster5Collar10.csv")
cluster6c10 <- read.csv("Cluster6Collar10.csv")
cluster7c10 <- read.csv("Cluster7Collar10.csv")
cluster8c10 <- read.csv("Cluster8Collar10.csv")
cluster9c10 <- read.csv("Cluster9Collar10.csv")

colnames(cluster10c10) <- c("Ind","X","Y","Z")
colnames(cluster1c10) <- c("Ind","X","Y","Z")
colnames(cluster2c10) <- c("Ind","X","Y","Z")
colnames(cluster3c10) <- c("Ind","X","Y","Z")
colnames(cluster4c10) <- c("Ind","X","Y","Z")
colnames(cluster5c10) <- c("Ind","X","Y","Z")
colnames(cluster6c10) <- c("Ind","X","Y","Z")
colnames(cluster7c10) <- c("Ind","X","Y","Z")
colnames(cluster8c10) <- c("Ind","X","Y","Z")
colnames(cluster9c10) <- c("Ind","X","Y","Z")

c10cl10 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster10c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster10c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster10c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c10cl1 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster1c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster1c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster1c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c10cl2 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster2c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster2c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster2c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))


c10cl3 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster3c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster3c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster3c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c10cl4 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster4c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster4c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster4c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))
c10cl5 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster5c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster5c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster5c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))
c10cl6 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster6c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster6c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster6c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c10cl7 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster7c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster7c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster7c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c10cl8 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster8c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster8c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster8c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c10cl9<-ggplot()+
  theme_bw()+
  geom_line(data = cluster9c10, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster9c10, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster9c10, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))



cluster10c41min <- read.csv("Cluster10C41min.csv")
cluster1c41min <- read.csv("Cluster1C41min.csv")
cluster2c41min <- read.csv("Cluster2C41min.csv")
cluster3c41min <- read.csv("Cluster3C41min.csv")
cluster4c41min <- read.csv("Cluster4C41min.csv")
cluster5c41min <- read.csv("Cluster5C41min.csv")
cluster6c41min <- read.csv("Cluster6C41min.csv")
cluster7c41min <- read.csv("Cluster7C41min.csv")
cluster8c41min <- read.csv("Cluster8C41min.csv")
cluster9c41min <- read.csv("Cluster9C41min.csv")

colnames(cluster10c41min) <- c("Ind","X","Y","Z")
colnames(cluster1c41min) <- c("Ind","X","Y","Z")
colnames(cluster2c41min) <- c("Ind","X","Y","Z")
colnames(cluster3c41min) <- c("Ind","X","Y","Z")
colnames(cluster4c41min) <- c("Ind","X","Y","Z")
colnames(cluster5c41min) <- c("Ind","X","Y","Z")
colnames(cluster6c41min) <- c("Ind","X","Y","Z")
colnames(cluster7c41min) <- c("Ind","X","Y","Z")
colnames(cluster8c41min) <- c("Ind","X","Y","Z")
colnames(cluster9c41min) <- c("Ind","X","Y","Z")

c41mincl10 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster10c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster10c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster10c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-40,40))

c41mincl1 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster1c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster1c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster1c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c41mincl2 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster2c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster2c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster2c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))


c41mincl3 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster3c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster3c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster3c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c41mincl4 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster4c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster4c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster4c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))
c41mincl5 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster5c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster5c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster5c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))
c41mincl6 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster6c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster6c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster6c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c41mincl7 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster7c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster7c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster7c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c41mincl8 <-ggplot()+
  theme_bw()+
  geom_line(data = cluster8c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster8c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster8c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

c41mincl9<-ggplot()+
  theme_bw()+
  geom_line(data = cluster9c41min, aes(Ind, X),color = "Blue")+
  geom_line(data = cluster9c41min, aes(Ind, Y),color = "Red")+
  geom_line(data = cluster9c41min, aes(Ind, Z), color = "Green")+
  ylim(c(-14,14))

#collar 4 proportions of each cluster
  c(9: 0.7934758281110116,
  5: 0.031222023276633842,
  2: 0.009679946284691137,
  0: 0.011806177260519248,
  1: 0.03553043867502238,
  7: 0.044762757385854966,
  8: 0.01947179946284691,
  4: 0.01812891674127126,
  3: 0.00346911369740376,
  6: 0.032452999104744855)
  #collar 10 proportions of each cluster
  c(8: 0.603288840537261,
    5: 0.04201012594669233,
    7: 0.07385246244612745,
    1: 0.04431147746767647,
    2: 0.05401899661073685,
    9: 0.016988158500355663,
    3: 0.012845725762584208,
    0: 0.008703293024812753,
    6: 0.005439558140507971,
    4: 0.1385413615632453)
  #collar 4 1 min window
  c(0: 0.7340962638842141,
    7: 0.0568832043083137,
    5: 0.028946482665769102,
    8: 0.021878155503197577,
    1: 0.041400201952204646,
    6: 0.017839111410299563,
    3: 0.03635139683608213,
    2: 0.023897677549646584,
    9: 0.01716593739481656,
    4: 0.021541568495456076)
  

  
assign4 <- read.csv("Collar4Assignments.csv")
assign41min <- read.csv("collar41minAssignments.csv")
assign10 <- read.csv("Collar10Assignments.csv")
