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
from progress.bar import ChargingBar
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
        currentcentroids7 = pd.DataFrame(centroids[6])
        currentcentroids8 = pd.DataFrame(centroids[7])
        currentcentroids9 = pd.DataFrame(centroids[8])
        currentcentroids10 = pd.DataFrame(centroids[9])
        currentcentroids1.to_csv(".\CurrentCluster1.csv")
        currentcentroids2.to_csv(".\CurrentCluster2.csv")
        currentcentroids3.to_csv(".\CurrentCluster3.csv")
        currentcentroids4.to_csv(".\CurrentCluster4.csv")
        currentcentroids5.to_csv(".\CurrentCluster5.csv")
        currentcentroids6.to_csv(".\CurrentCluster6.csv")
        currentcentroids7.to_csv(".\CurrentCluster7.csv")
        currentcentroids8.to_csv(".\CurrentCluster8.csv")
        currentcentroids9.to_csv(".\CurrentCluster9.csv")
        currentcentroids10.to_csv(".\CurrentCluster10.csv")
    for key in assignments:
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
        currentcentroids7 = pd.DataFrame(centroids[6])
        currentcentroids8 = pd.DataFrame(centroids[7])
        currentcentroids9 = pd.DataFrame(centroids[8])
        currentcentroids10 = pd.DataFrame(centroids[9])
        currentcentroids1.to_csv(".\CurrentCluster1.csv")
        currentcentroids2.to_csv(".\CurrentCluster2.csv")
        currentcentroids3.to_csv(".\CurrentCluster3.csv")
        currentcentroids4.to_csv(".\CurrentCluster4.csv")
        currentcentroids5.to_csv(".\CurrentCluster5.csv")
        currentcentroids6.to_csv(".\CurrentCluster6.csv")
        currentcentroids7.to_csv(".\CurrentCluster7.csv")
        currentcentroids8.to_csv(".\CurrentCluster8.csv")
        currentcentroids9.to_csv(".\CurrentCluster9.csv")
        currentcentroids10.to_csv(".\CurrentCluster10.csv")
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

