import shutil 
import os
import numpy as np
from multiprocessing import set_start_method,get_context

def deletefolders(folder,subfolder): 
    
    shutil.rmtree(folder + os.sep + subfolder)
    
    print("subfolder: ",subfolder," deleted")
    
if __name__ == "__main__":     

    

    delete = ["2017_","2018_","2019_","2020_","2021_","2022_"]
    
    base_folder = os.path.abspath('..')
    rawdata_folder = base_folder + os.sep + "downloads" + os.sep + "500"
    
    folders = os.listdir(rawdata_folder)
    
    folders_del = [[f for f in folders if y in f] for y in delete]
    folders_del = [item for sublist in folders_del for item in sublist] 

    
    try:
        set_start_method("spawn")
    except:
        pass

    for ff in folders_del:
        print("deleting in folder: ",ff)
        subf = os.listdir(ff)

        mainf = [ff for i in range(len(subf))]

        with get_context("spawn").Pool(12) as p:     
            p.starmap(deletefolders,zip(mainf,subf))

        shutil.rmtree(ff)
