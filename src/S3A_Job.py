import subprocess
import numpy as np

# Run the script
#subprocess.call(['python', 'hubGetTilesNew.py','-d', '2021-08-30', '-a', 'Greenland', '-r', '500']) 

day = "2021-08-23"

print("Processing " + day)
subprocess.call(['python', 'nocams_S3A.py','-d',day, '-a', 'Greenland', '-r', '500']) 
