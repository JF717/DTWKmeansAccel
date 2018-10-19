# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:34:09 2018

@author: James Foley
"""

import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.metrics import classification_report
import random
import os
#from progress.bar import ChargingBar
from numba import autojit
import time
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw



def DTWDistance(s1, s2,w):
    DTW={}

    w = max(w, abs(len(s1)-len(s2)))

    for i in range(-1,len(s1)):
        for j in range(-1,len(s2)):
            DTW[(i, j)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(max(0, i-w), min(len(s2), i+w)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])

    return np.sqrt(DTW[len(s1)-1, len(s2)-1])

def LB_Keogh(s1,s2,r):
    LB_sum=0
    for ind,i in enumerate(s1):

        lower_bound=min(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
        upper_bound=max(s2[(ind-r if ind-r>=0 else 0):(ind+r)])

        if i>upper_bound:
            LB_sum=LB_sum+(i-upper_bound)**2
        elif i<lower_bound:
            LB_sum=LB_sum+(i-lower_bound)**2

    return np.sqrt(LB_sum)

def k_means_clust(data,num_clust,num_iter,w=5):
    centroids=random.sample(list(data)[0],num_clust)
    counter=0
    for n in range(num_iter):
        counter+=1
        print(counter)
        assignments={}
        #assign data points to clusters
        for ind,i in enumerate(data):
            min_dist=float('inf')
            closest_clust=None
            for c_ind,j in enumerate(centroids):
                if LB_Keogh([i],[j],5)<min_dist:
                    cur_dist=DTWDistance([i],[j],w)
                    if cur_dist<min_dist:
                        min_dist=cur_dist
                        closest_clust=c_ind
            if closest_clust in assignments:
                assignments[closest_clust].append(ind)
            else:
                assignments[closest_clust]=[]

        #recalculate centroids of clusters
        for key in assignments:
            clust_sum=0
            for k in assignments[key]:
                clust_sum=clust_sum+data[k]
            centroids[key]=[m/len(assignments[key]) for m in clust_sum]

    return centroids



            
def DTWi_clusteringShort(data,num_clust,num_iter,window,dims):
    centroids = np.zeros([num_clust,dims,window])
    centroid_perc = {}
    for i in range(num_clust):
        for j in range((dims-1)):
            centroids[i][j]= random.sample(list(data[j][0]),window)    
    counter = 0
    for n in range(num_iter):
        counter+=1
        print("current Iteration is",n+1)
        assignments = {}
        for i in range(0,len(data[0][0]),window):
            closest_clust = None
            clust_dist = {}
            for c_ind,j in enumerate(centroids):
                cur_dist = 0
                for l in range(dims-1):
                    dat = data[l][0][i:(i+window)]
                    cur_dist+=DTWDistance(dat,j[0],window)
                clust_dist[c_ind] =[cur_dist]
                closest_clust=min(clust_dist, key=clust_dist.get)
            if closest_clust in assignments:
                assignments[closest_clust].append(i)
            else:
                assignments[closest_clust]=[]  
        for key in assignments:
            clust_sum= np.zeros([dims,window])
            for k in assignments[key]:
                for d in range(dims):
                    try: 
                        clust_sum[d,:] = clust_sum[d,:] + data[d,:,k:k+window] 
                    except:
                        next
            clust_sum = clust_sum / len(assignments[key])
            centroids[key]= clust_sum
        currentcentroids1 = pd.DataFrame(centroids[0])
        currentcentroids2 = pd.DataFrame(centroids[1])
        currentcentroids3 = pd.DataFrame(centroids[2])
        currentcentroids4 = pd.DataFrame(centroids[3])
        currentcentroids5 = pd.DataFrame(centroids[4])
        currentcentroids6 = pd.DataFrame(centroids[5])
#        currentcentroids7 = pd.DataFrame(centroids[6])
#        currentcentroids8 = pd.DataFrame(centroids[7])
#        currentcentroids9 = pd.DataFrame(centroids[8])
#        currentcentroids10 = pd.DataFrame(centroids[9])
        currentcentroids1.to_csv(".\CurrentCluster1.csv")
        currentcentroids2.to_csv(".\CurrentCluster2.csv")
        currentcentroids3.to_csv(".\CurrentCluster3.csv")
        currentcentroids4.to_csv(".\CurrentCluster4.csv")
        currentcentroids5.to_csv(".\CurrentCluster5.csv")
        currentcentroids6.to_csv(".\CurrentCluster6.csv")
#        currentcentroids7.to_csv(".\CurrentCluster7.csv")
#        currentcentroids8.to_csv(".\CurrentCluster8.csv")
#        currentcentroids9.to_csv(".\CurrentCluster9.csv")
#        currentcentroids10.to_csv(".\CurrentCluster10.csv")
#    for key in assignments:
        centroid_perc[key] = len(assignments[key])/sum([len(v) for v in assignments.values()])
    return centroids, centroid_perc,assignments    

def DTWi_clusteringLong(data,num_clust,num_iter,window,dims):
    centroids = np.zeros([num_clust,dims,window])
    centroid_perc = {}
    for i in range(num_clust):
        for j in range((dims-1)):
            centroids[i][j]= random.sample(list(data[j][0]),window)    
    counter = 0
    for n in range(num_iter):
        counter+=1
        print("current Iteration is",n+1)
        assignments = {}
        for i in range(0,len(data[0][0]),window):
            closest_clust = None
            clust_dist = {}
            for c_ind,j in enumerate(centroids):
                cur_dist = 0
                for l in range(dims-1):
                    dat = data[l][0][i:(i+window)]
                    cur_dist+=fastdtw(dat,j[0],dist = euclidean)[0]
                clust_dist[c_ind] =[cur_dist]
                closest_clust=min(clust_dist, key=clust_dist.get)
            if closest_clust in assignments:
                assignments[closest_clust].append(i)
            else:
                assignments[closest_clust]=[]  
        for key in assignments:
            clust_sum= np.zeros([dims,window])
            for k in assignments[key]:
                for d in range(dims):
                    try: 
                        clust_sum[d,:] = clust_sum[d,:] + data[d,:,k:k+window] 
                    except:
                        next
            clust_sum = clust_sum / len(assignments[key])
            centroids[key]= clust_sum
        currentcentroids1 = pd.DataFrame(centroids[0])
        currentcentroids2 = pd.DataFrame(centroids[1])
        currentcentroids3 = pd.DataFrame(centroids[2])
        currentcentroids4 = pd.DataFrame(centroids[3])
        currentcentroids5 = pd.DataFrame(centroids[4])
        currentcentroids6 = pd.DataFrame(centroids[5])
        #currentcentroids7 = pd.DataFrame(centroids[6])
        #currentcentroids8 = pd.DataFrame(centroids[7])
        #currentcentroids9 = pd.DataFrame(centroids[8])
        #currentcentroids10 = pd.DataFrame(centroids[9])
        currentcentroids1.to_csv(".\CurrentCluster1.csv")
        currentcentroids2.to_csv(".\CurrentCluster2.csv")
        currentcentroids3.to_csv(".\CurrentCluster3.csv")
        currentcentroids4.to_csv(".\CurrentCluster4.csv")
        currentcentroids5.to_csv(".\CurrentCluster5.csv")
        currentcentroids6.to_csv(".\CurrentCluster6.csv")
        #currentcentroids7.to_csv(".\CurrentCluster7.csv")
        #currentcentroids8.to_csv(".\CurrentCluster8.csv")
        #currentcentroids9.to_csv(".\CurrentCluster9.csv")
        #currentcentroids10.to_csv(".\CurrentCluster10.csv")
    for key in assignments:
        centroid_perc[key] = len(assignments[key])/sum([len(v) for v in assignments.values()])
    return centroids, centroid_perc,assignments         

Collardat = pd.read_csv(".\Collar4AccelCor.csv")
justdat = np.array([[Collardat["obj.X"]],[Collardat["obj.Y"]],[Collardat["obj.Z"]]])
testdat = np.array([[justdat[0][0][1:1000]],[justdat[1][0][1:1000]],[justdat[2][0][1:1000]]])
Centroids,cent_prec,assign = DTWi_clusteringShort(justdat,10,5,100,3)


ClusterFrame10 = pd.DataFrame(Centroids[9]).T
ClusterFrame9 = pd.DataFrame(Centroids[8]).T
ClusterFrame8 = pd.DataFrame(Centroids[7]).T
ClusterFrame7 = pd.DataFrame(Centroids[6]).T
ClusterFrame6 = pd.DataFrame(Centroids[5]).T
ClusterFrame5 = pd.DataFrame(Centroids[4]).T
ClusterFrame4 = pd.DataFrame(Centroids[3]).T
ClusterFrame3 = pd.DataFrame(Centroids[2]).T
ClusterFrame2 = pd.DataFrame(Centroids[1]).T
ClusterFrame1 = pd.DataFrame(Centroids[0]).T

ClusterFrame10.to_csv(".\Cluster10Collar4.csv")
ClusterFrame9.to_csv(".\Cluster9Collar4.csv")
ClusterFrame8.to_csv(".\Cluster8Collar4.csv")
ClusterFrame7.to_csv(".\Cluster7Collar4.csv")
ClusterFrame6.to_csv(".\Cluster6Collar4.csv") 
ClusterFrame5.to_csv(".\Cluster5Collar4.csv") 
ClusterFrame4.to_csv(".\Cluster4Collar4.csv")
ClusterFrame3.to_csv(".\Cluster3Collar4.csv")
ClusterFrame2.to_csv(".\Cluster2Collar4.csv") 
ClusterFrame1.to_csv(".\Cluster1Collar4.csv")

c4assigndat = pd.DataFrame.from_dict(assign, orient = 'index')

c4assigndat = c4assigndat.T

c4assigndat.to_csv(".\Collar4Assignments.csv")

Collardat10 = pd.read_csv(".\Collar10AccelCor.csv")
justdat10 = np.array([[Collardat10["obj.X"]],[Collardat10["obj.Y"]],[Collardat10["obj.Z"]]])

Centroids10,cent_prec10,assign10 = DTWi_clusteringShort(justdat10,10,5,100,3)

C10ClusterFrame10 = pd.DataFrame(Centroids10[9]).T
C10ClusterFrame9 = pd.DataFrame(Centroids10[8]).T
C10ClusterFrame8 = pd.DataFrame(Centroids10[7]).T
C10ClusterFrame7 = pd.DataFrame(Centroids10[6]).T
C10ClusterFrame6 = pd.DataFrame(Centroids10[5]).T
C10ClusterFrame5 = pd.DataFrame(Centroids10[4]).T
C10ClusterFrame4 = pd.DataFrame(Centroids10[3]).T
C10ClusterFrame3 = pd.DataFrame(Centroids10[2]).T
C10ClusterFrame2 = pd.DataFrame(Centroids10[1]).T
C10ClusterFrame1 = pd.DataFrame(Centroids10[0]).T

C10ClusterFrame10.to_csv(".\Cluster10Collar10.csv")
C10ClusterFrame9.to_csv(".\Cluster9Collar10.csv")
C10ClusterFrame8.to_csv(".\Cluster8Collar10.csv")
C10ClusterFrame7.to_csv(".\Cluster7Collar10.csv")
C10ClusterFrame6.to_csv(".\Cluster6Collar10.csv") 
C10ClusterFrame5.to_csv(".\Cluster5Collar10.csv") 
C10ClusterFrame4.to_csv(".\Cluster4Collar10.csv")
C10ClusterFrame3.to_csv(".\Cluster3Collar10.csv")
C10ClusterFrame2.to_csv(".\Cluster2Collar10.csv") 
C10ClusterFrame1.to_csv(".\Cluster1Collar10.csv")

c10assigndat = pd.DataFrame.from_dict(assign10, orient = 'index')

c10assigndat = c10assigndat.T

c10assigndat.to_csv(".\Collar10Assignments.csv")

Centroids1mwin4, cent_prec1mwin4,assign1mwin4 = DTWi_clusteringLong(justdat,10,5,600,3)

C41minClusterFrame10 = pd.DataFrame(Centroids1mwin4[9]).T
C41minClusterFrame9 = pd.DataFrame(Centroids1mwin4[8]).T
C41minClusterFrame8 = pd.DataFrame(Centroids1mwin4[7]).T
C41minClusterFrame7 = pd.DataFrame(Centroids1mwin4[6]).T
C41minClusterFrame6 = pd.DataFrame(Centroids1mwin4[5]).T
C41minClusterFrame5 = pd.DataFrame(Centroids1mwin4[4]).T
C41minClusterFrame4 = pd.DataFrame(Centroids1mwin4[3]).T
C41minClusterFrame3 = pd.DataFrame(Centroids1mwin4[2]).T
C41minClusterFrame2 = pd.DataFrame(Centroids1mwin4[1]).T
C41minClusterFrame1 = pd.DataFrame(Centroids1mwin4[0]).T

C41minClusterFrame10.to_csv(".\Cluster10C41min.csv")
C41minClusterFrame9.to_csv(".\Cluster9C41min.csv")
C41minClusterFrame8.to_csv(".\Cluster8C41min.csv")
C41minClusterFrame7.to_csv(".\Cluster7C41min.csv")
C41minClusterFrame6.to_csv(".\Cluster6C41min.csv") 
C41minClusterFrame5.to_csv(".\Cluster5C41min.csv") 
C41minClusterFrame4.to_csv(".\Cluster4C41min.csv")
C41minClusterFrame3.to_csv(".\Cluster3C41min.csv")
C41minClusterFrame2.to_csv(".\Cluster2C41min.csv") 
C41minClusterFrame1.to_csv(".\Cluster1C41min.csv")


c41minassigndat = pd.DataFrame.from_dict(assign1mwin4, orient = 'index')

c41minassigndat = c41minassigndat.T

c41minassigndat.to_csv(".\Collar41minAssignments.csv")

Collardat4 = pd.read_csv(".\Collar4AccelCor.csv")
justdat4 = np.array([[Collardat4["obj.X"]],[Collardat4["obj.Y"]],[Collardat4["obj.Z"]]])

Centroids4,cent_prec4,assign4 = DTWi_clusteringLong(justdat4,6,5,100,3)

C4ClusterFrame6 = pd.DataFrame(Centroids4[5]).T
C4ClusterFrame5 = pd.DataFrame(Centroids4[4]).T
C4ClusterFrame4 = pd.DataFrame(Centroids4[3]).T
C4ClusterFrame3 = pd.DataFrame(Centroids4[2]).T
C4ClusterFrame2 = pd.DataFrame(Centroids4[1]).T
C4ClusterFrame1 = pd.DataFrame(Centroids4[0]).T


C4ClusterFrame6.to_csv(".\Cluster6C4.csv") 
C4ClusterFrame5.to_csv(".\Cluster5C4.csv") 
C4ClusterFrame4.to_csv(".\Cluster4C4.csv")
C4ClusterFrame3.to_csv(".\Cluster3C4.csv")
C4ClusterFrame2.to_csv(".\Cluster2C4.csv") 
C4ClusterFrame1.to_csv(".\Cluster1C4.csv")

c4assigndat = pd.DataFrame.from_dict(assign4, orient = 'index')

c4assigndat = c4assigndat.T

c4assigndat.to_csv(".\Collar4Assignments.csv")

Collardat5 = pd.read_csv(".\Collar5AccelCor.csv")
justdat5 = np.array([[Collardat5["obj.X"]],[Collardat5["obj.Y"]],[Collardat5["obj.Z"]]])

Centroids5,cent_prec5,assign5 = DTWi_clusteringShort(justdat5,6,5,100,3)

C5ClusterFrame6 = pd.DataFrame(Centroids5[5]).T
C5ClusterFrame5 = pd.DataFrame(Centroids5[4]).T
C5ClusterFrame4 = pd.DataFrame(Centroids5[3]).T
C5ClusterFrame3 = pd.DataFrame(Centroids5[2]).T
C5ClusterFrame2 = pd.DataFrame(Centroids5[1]).T
C5ClusterFrame1 = pd.DataFrame(Centroids5[0]).T


C5ClusterFrame6.to_csv(".\Cluster6C5.csv") 
C5ClusterFrame5.to_csv(".\Cluster5C5.csv") 
C5ClusterFrame4.to_csv(".\Cluster4C5.csv")
C5ClusterFrame3.to_csv(".\Cluster3C5.csv")
C5ClusterFrame2.to_csv(".\Cluster2C5.csv") 
C5ClusterFrame1.to_csv(".\Cluster1C5.csv")

c5assigndat = pd.DataFrame.from_dict(assign5, orient = 'index')

c5assigndat = c5assigndat.T

c5assigndat.to_csv(".\Collar5Assignments.csv")


Collardat7 = pd.read_csv(".\Collar7AccelCor.csv")
justdat7 = np.array([[Collardat7["obj.X"]],[Collardat7["obj.Y"]],[Collardat7["obj.Z"]]])

Centroids7,cent_prec7,assign7 = DTWi_clusteringShort(justdat7,6,5,100,3)


C7ClusterFrame6 = pd.DataFrame(Centroids7[5]).T
C7ClusterFrame5 = pd.DataFrame(Centroids7[4]).T
C7ClusterFrame4 = pd.DataFrame(Centroids7[3]).T
C7ClusterFrame3 = pd.DataFrame(Centroids7[2]).T
C7ClusterFrame2 = pd.DataFrame(Centroids7[1]).T
C7ClusterFrame1 = pd.DataFrame(Centroids7[0]).T


C7ClusterFrame6.to_csv(".\Cluster6C7.csv") 
C7ClusterFrame5.to_csv(".\Cluster5C7.csv") 
C7ClusterFrame4.to_csv(".\Cluster4C7.csv")
C7ClusterFrame3.to_csv(".\Cluster3C7.csv")
C7ClusterFrame2.to_csv(".\Cluster2C7.csv") 
C7ClusterFrame1.to_csv(".\Cluster1C7.csv")

c7assigndat = pd.DataFrame.from_dict(assign7, orient = 'index')

c7assigndat = c7assigndat.T

c7assigndat.to_csv(".\Collar7Assignments.csv")
Collardat12 = pd.read_csv(".\Collar12AccelCor.csv")

justdat12 = np.array([[Collardat12["obj.X"]],[Collardat12["obj.Y"]],[Collardat12["obj.Z"]]])

Centroids12,cent_prec12,assign12 = DTWi_clusteringShort(justdat12,6,5,100,3)

C12ClusterFrame6 = pd.DataFrame(Centroids12[5]).T
C12ClusterFrame5 = pd.DataFrame(Centroids12[4]).T
C12ClusterFrame4 = pd.DataFrame(Centroids12[3]).T
C12ClusterFrame3 = pd.DataFrame(Centroids12[2]).T
C12ClusterFrame2 = pd.DataFrame(Centroids12[1]).T
C12ClusterFrame1 = pd.DataFrame(Centroids12[0]).T


C12ClusterFrame6.to_csv(".\Cluster6C12.csv") 
C12ClusterFrame5.to_csv(".\Cluster5C12.csv") 
C12ClusterFrame4.to_csv(".\Cluster4C12.csv")
C12ClusterFrame3.to_csv(".\Cluster3C12.csv")
C12ClusterFrame2.to_csv(".\Cluster2C12.csv") 
C12ClusterFrame1.to_csv(".\Cluster1C12.csv")

c12assigndat = pd.DataFrame.from_dict(assign12, orient = 'index')

c12assigndat = c12assigndat.T

c12assigndat.to_csv(".\Collar12Assignments.csv")

Collardat2 = pd.read_csv(".\Collar2AccelCor.csv")
justdat2 = np.array([[Collardat2["obj.X"]],[Collardat2["obj.Y"]],[Collardat2["obj.Z"]]])

Centroids2,cent_prec2,assign2 = DTWi_clusteringShort(justdat2,6,5,100,3)

C2ClusterFrame6 = pd.DataFrame(Centroids2[5]).T
C2ClusterFrame5 = pd.DataFrame(Centroids2[4]).T
C2ClusterFrame4 = pd.DataFrame(Centroids2[3]).T
C2ClusterFrame3 = pd.DataFrame(Centroids2[2]).T
C2ClusterFrame2 = pd.DataFrame(Centroids2[1]).T
C2ClusterFrame1 = pd.DataFrame(Centroids2[0]).T


C2ClusterFrame6.to_csv(".\Cluster6C2.csv") 
C2ClusterFrame5.to_csv(".\Cluster5C2.csv") 
C2ClusterFrame4.to_csv(".\Cluster4C2.csv")
C2ClusterFrame3.to_csv(".\Cluster3C2.csv")
C2ClusterFrame2.to_csv(".\Cluster2C2.csv") 
C2ClusterFrame1.to_csv(".\Cluster1C2.csv")

c2assigndat = pd.DataFrame.from_dict(assign2, orient = 'index')

c2assigndat = c2assigndat.T

c2assigndat.to_csv(".\Collar2Assignments.csv")

Collardat6 = pd.read_csv(".\Collar6AccelCor.csv")
justdat6 = np.array([[Collardat6["obj.X"]],[Collardat6["obj.Y"]],[Collardat6["obj.Z"]]])

Centroids6,cent_prec6, assign6 = DTWi_clusteringShort(justdat6,6,5,100,3)   

C6ClusterFrame6 = pd.DataFrame(Centroids6[5]).T
C6ClusterFrame5 = pd.DataFrame(Centroids6[4]).T
C6ClusterFrame4 = pd.DataFrame(Centroids6[3]).T
C6ClusterFrame3 = pd.DataFrame(Centroids6[2]).T
C6ClusterFrame2 = pd.DataFrame(Centroids6[1]).T
C6ClusterFrame1 = pd.DataFrame(Centroids6[0]).T


C6ClusterFrame6.to_csv(".\Cluster6C6.csv") 
C6ClusterFrame5.to_csv(".\Cluster5C6.csv") 
C6ClusterFrame4.to_csv(".\Cluster4C6.csv")
C6ClusterFrame3.to_csv(".\Cluster3C6.csv")
C6ClusterFrame2.to_csv(".\Cluster2C6.csv") 
C6ClusterFrame1.to_csv(".\Cluster1C6.csv")

c6assigndat = pd.DataFrame.from_dict(assign6, orient = 'index')

c6assigndat = c6assigndat.T

c6assigndat.to_csv(".\Collar6Assignments.csv")

Collardat9 = pd.read_csv(".\Collar9AccelCor.csv")
justdat9 = np.array([[Collardat9["obj.X"]],[Collardat9["obj.Y"]],[Collardat9["obj.Z"]]])


Centroids9,cent_prec9, assign9 = DTWi_clusteringShort(justdat9,6,5,100,3)   

C9ClusterFrame6 = pd.DataFrame(Centroids9[5]).T
C9ClusterFrame5 = pd.DataFrame(Centroids9[4]).T
C9ClusterFrame4 = pd.DataFrame(Centroids9[3]).T
C9ClusterFrame3 = pd.DataFrame(Centroids9[2]).T
C9ClusterFrame2 = pd.DataFrame(Centroids9[1]).T
C9ClusterFrame1 = pd.DataFrame(Centroids9[0]).T


C9ClusterFrame6.to_csv(".\Cluster6C9.csv") 
C9ClusterFrame5.to_csv(".\Cluster5C9.csv") 
C9ClusterFrame4.to_csv(".\Cluster4C9.csv")
C9ClusterFrame3.to_csv(".\Cluster3C9.csv")
C9ClusterFrame2.to_csv(".\Cluster2C9.csv") 
C9ClusterFrame1.to_csv(".\Cluster1C9.csv")

c9assigndat = pd.DataFrame.from_dict(assign9, orient = 'index')

c9assigndat = c9assigndat.T

c9assigndat.to_csv(".\Collar9Assignments.csv")

Collardat102 = pd.read_csv(".\Collar9AccelCor.csv")
justdat10 = np.array([[Collardat9["obj.X"]],[Collardat9["obj.Y"]],[Collardat9["obj.Z"]]])


Centroids102,cent_prec102, assign102 = DTWi_clusteringShort(justdat10,6,5,100,3)   

C102ClusterFrame6 = pd.DataFrame(Centroids102[5]).T
C102ClusterFrame5 = pd.DataFrame(Centroids102[4]).T
C102ClusterFrame4 = pd.DataFrame(Centroids102[3]).T
C102ClusterFrame3 = pd.DataFrame(Centroids102[2]).T
C102ClusterFrame2 = pd.DataFrame(Centroids102[1]).T
C102ClusterFrame1 = pd.DataFrame(Centroids102[0]).T


C102ClusterFrame6.to_csv(".\Cluster6C10.csv") 
C102ClusterFrame5.to_csv(".\Cluster5C10.csv") 
C102ClusterFrame4.to_csv(".\Cluster4C10.csv")
C102ClusterFrame3.to_csv(".\Cluster3C10.csv")
C102ClusterFrame2.to_csv(".\Cluster2C10.csv") 
C102ClusterFrame1.to_csv(".\Cluster1C10.csv")

c102assigndat = pd.DataFrame.from_dict(assign102, orient = 'index')

c102assigndat = c102assigndat.T

c102assigndat.to_csv(".\Collar10Assignments2.csv")