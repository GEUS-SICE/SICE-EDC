import ftplib
import zipfile
import numpy as np
import glob
import os 
from multiprocessing import set_start_method,get_context

def ftpsend(output_filename,name):

    ftp = ftplib.FTP('ftp.brockmann-consult.de')
    ftp.login('s3snow','$3Sn0W@bc')
    ftp.cwd('data/SICE_EDC/S3A_S3B_mix')
    
    file = open(output_filename,'rb')                 # file to send
    ftp.storbinary('STOR ' + name, file)     # send the file
    
    file.close()
    ftp.quit() # close file and FTP
    

def multisend(folder): 
    
    output_filename = folder + "_zipped.zip"
    files = glob.glob(folder + os.sep + "*.tif")
    zout = zipfile.ZipFile(output_filename, "w", zipfile.ZIP_LZMA)
    for i,fname in enumerate(files):
        zout.write(fname)
    zout.close()
    zipname = output_filename.split(os.sep)[-1]
    ftpsend(output_filename,zipname)    


if __name__ == "__main__":     

    ftp = ftplib.FTP('ftp.brockmann-consult.de')
    ftp.login('s3snow','$3Sn0W@bc')
    ftp.cwd('data/SICE_EDC//S3A_S3B_mix')
    allfiles = ftp.nlst('*sice*')
    ftp.quit()

    #basename = "sice_500_2017_09_"
    os.chdir("output")

    basefolder = os.listdir()
    basefolder = [f for f in basefolder if f[-1].isnumeric()]

    send = ["2021","2022"]

    folders_send = [[f for f in basefolder if y in f] for y in send]
    folders_send = [item for sublist in folders_send for item in sublist] 
    folders_send = [f for f in folders_send if (f + "_zipped.zip") not in allfiles]

    print("folders to send: ",folders_send)

    try:
        set_start_method("spawn")
    except:
        pass

    print("zipping and uploading folders.....")
    with get_context("spawn").Pool(12) as p:     
            p.starmap(multisend,zip(folders_send))

    print("Done")