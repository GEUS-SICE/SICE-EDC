import shutil 
import os
import numpy as np

base_folder = os.path.abspath('..')
output_folder = base_folder + os.sep + "output"

folders = os.listdir(output_folder)

folders = os.listdir()

delete = ["2017","2018","2019","2020","2021","2022"]
        
folders_del = [[f for f in folders if y in f] for y in delete]
folders_del = [item for sublist in folders_del for item in sublist]        
#print(folders_del)

for ff in folders_del:
    print(f'deleting {ff}')
    shutil.rmtree(ff)