import subprocess
import numpy as np

# Run the script
#subprocess.call(['python', 'hubGetTilesNew.py','-d', '2021-08-30', '-a', 'Greenland', '-r', '500']) 

for d in np.arange(20,31):
    
    day = str(d + 1)
    day = day.zfill(2)
    print("Processing 2018-08-" + day)
    subprocess.call(['python', 'hubGetTilesNew.py','-d', '2018-08-' + day, '-a', 'Greenland', '-r', '500']) 