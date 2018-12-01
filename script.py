# Plotting the map  
import scipy
import matplotlib.pyplot as plt
import os,fnmatch

def opendirectory(root):
	sub_dir  = list(os.listdir(root))
	#print(sub_dir)
	for i in range(len(sub_dir)):
	#for i in range(13):
		print("------------------------------Checking  routes for the driver-------------------------------- ",sub_dir[i] , "Driver" ,i)
		if sub_dir[i] != ".DS_Store":
				pattern = "*_Web.csv"
				file = list(os.listdir(os.path.join(root,sub_dir[i])))
				dir = (os.path.join(root,sub_dir[i]))
				dir1 = dir.replace(" ","")
				os.rename(dir,dir1)
				#print(sub_dir[i])
				for j in range(len(file)):
				#for j in range(1):	
					if fnmatch.fnmatch(file[j],pattern):
							#print(file[j])
							file_r = (os.path.join(dir1,file[j]))
							#os.rename(os.path.join(root,sub_dir[i],file[j]), os.path.join(root,sub_dir[i].replace(" ",""),file[j].replace(" ","")))
							file_route = file_r.replace(" ","")
							#print("##########",file_route)
							os.rename(file_r,file_route)

							#print(os.path.join(root,sub_dir[i],file[j]))
							#print("##########",file_route)
							#os.rename(os.path.join(root,sub_dir[i],file[j]), file_route)
							#print("-------------------------",file_route)
							#print(file[j])
							if "PARK" in file[j]:
								continue
							if "PRETRIP" in file[j]:
								continue
							if "GAS" in file[j]:
								continue	
							os.system("python mapplot.py {}".format(file_route,file[j]))	

def main():
	root = '/Users/fang/Desktop/map/output/18_24/'
	

	opendirectory(root)
	
main()