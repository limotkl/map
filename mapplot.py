import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
import cv2
# Plotting the map  
import scipy
import matplotlib.pyplot as plt
from scipy import ndimage
import os
import substring

lats=[]
longs=[]
routes=['WSOUTDCLIN','UP','DCLOUTWSIN','RRT','OAK','LRS','CS','UDC','DCLIN','WSIN']

def createReference(final_way,path_curr):
    path1=os.path.join(path_curr,"input")
    path2=os.path.join(path1,"input")
    path3=os.path.join(path_curr,"input1")
    for files in os.listdir(path3):
        files=files.rstrip('.png')
        if(files==final_way):
            files=files+'.png'
            os.system("cp {}/{} {}".format(path3,files,path2))

def plottingPoints(lines,route,file):
    #print("--------------------------route sent to plot-----------------------------------",route)
    for line in lines:
        if("lat" in line):  # Data Cleaning
            continue
        line=line.rstrip('\n')
        line=line.split(',')
        lats.append(float(line[0]))
        longs.append(float(line[1]))
   
    my_plot=plt.plot(lats,longs)
    path_curr=os.getcwd()
    #save = str(route.split('\\')[0:-1])
    save = os.path.dirname(os.path.abspath(route))
    #print(save)
    graph = os.path.join(save,"map")
    if not os.path.exists(graph):
        os.makedirs(graph)
    plt.savefig(os.path.join(save,graph,file))  
    os.chdir(path_curr)

def main(arg):
    name = arg[1]
    pat = arg[1]
    #print(name)
    pattern = pat.replace('2017','-')
    #print(pattern)
    file = substring.substringByChar(pattern, startChar="-", endChar="_")
    #print(file)
    file = file[2:-1]
    file = file.replace(":","-") 
    file = file.replace(".","-") 
    print("--------reading file to plot --------------------")
    fileref=open(name,"r")  # Reading Lines from data
    lines=fileref.readlines()
    fileref.close()
    print(file)
    plottingPoints(lines,arg[1],file)	
main(sys.argv)

