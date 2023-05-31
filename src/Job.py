import subprocess
import numpy as np
import os

# Run the script
# This script runs for all the days

for m in np.arange(9,10):
    month = str(m)
    month = month.zfill(2) 
    out_folder = os.getcwd() + os.sep + 'output'
    for d in np.arange(0,30):
        day = str(d + 1)
        day = day.zfill(2)
        
        
        date = "2018-" + month + "-" + day
        folder_exist = os.path.exists(out_folder + os.sep + 'sice_500_' + date.replace("-","_"))
        if not folder_exist:
            print(f"Processing {date}")
            subprocess.call(['python', 'hubGetTilesNew.py','-d', date, '-a', 'Greenland', '-r', '500']) 
        else:
            print(f"{date} has already been processed, skipping")    
        
        
        date = "2019-" + month + "-" + day
        folder_exist = os.path.exists(out_folder + os.sep + 'sice_500_' + date.replace("-","_"))
        if not folder_exist:
            print(f"Processing {date}")
            subprocess.call(['python', 'hubGetTilesNew.py','-d', date, '-a', 'Greenland', '-r', '500']) 
        else:
            print(f"{date} has already been processed, skipping")    
       
        date = "2020-" + month + "-" + day
        folder_exist = os.path.exists(out_folder + os.sep + 'sice_500_' + date.replace("-","_"))
        if not folder_exist:
            print(f"Processing {date}")
            subprocess.call(['python', 'hubGetTilesNew.py','-d', date, '-a', 'Greenland', '-r', '500']) 
        else:
            print(f"{date} has already been processed, skipping")    
        
        date = "2021-" + month + "-" + day
        folder_exist = os.path.exists(out_folder + os.sep + 'sice_500_' + date.replace("-","_"))
        if not folder_exist:
            print(f"Processing {date}")
            subprocess.call(['python', 'hubGetTilesNew.py','-d', date, '-a', 'Greenland', '-r', '500']) 
        else:
            print(f"{date} has already been processed, skipping")    
            
        date = "2022-" + month + "-" + day
        folder_exist = os.path.exists(out_folder + os.sep + 'sice_500_' + date.replace("-","_"))
        if not folder_exist:
            print(f"Processing {date}")
            subprocess.call(['python', 'hubGetTilesNew.py','-d', date, '-a', 'Greenland', '-r', '500']) 
        else:
            print(f"{date} has already been processed, skipping")    
       
      
    
for d in np.arange(0,30):
    
    day = str(d + 1)
    day = day.zfill(2)
    #print("Processing 2019-09-" + day)
    #subprocess.call(['python', 'hubGetTilesNew.py','-d', '2019-09-' + day, '-a', 'Greenland', '-r', '500']) 
    #print("Processing 2020-09-" + day)
    #subprocess.call(['python', 'hubGetTilesNew.py','-d', '2020-09-' + day, '-a', 'Greenland', '-r', '500'])
    print("Processing 2021-06-" + day)
    subprocess.call(['python', 'hubGetTilesNew.py','-d', '2021-06-' + day, '-a', 'Greenland', '-r', '500'])
    #print("Processing 2022-09-" + day)
    #subprocess.call(['python', 'hubGetTilesNew.py','-d', '2022-09-' + day, '-a', 'Greenland', '-r', '500']) 