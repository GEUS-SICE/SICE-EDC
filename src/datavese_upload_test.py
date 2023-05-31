

from datetime import datetime
import json
import requests  # http://docs.python-requests.org/en/master/
import zipfile
import glob 
import os
import numpy as np
from pyproj import CRS,Transformer
import netCDF4 as nc 
import xarray as xr
from rasterio.transform import Affine
import rasterio
import pandas as pd

def opentiff(filename):

    "Input: Filename of GeoTIFF File "
    "Output: xgrid,ygrid, data paramater of Tiff, the data projection"

    da = xr.open_rasterio(filename)
    proj = CRS.from_string(da.crs)


    transform = Affine(*da.transform)
    elevation = np.array(da.variable[0],dtype=np.float32)
    nx,ny = da.sizes['x'],da.sizes['y']
    x,y = np.meshgrid(np.arange(nx,dtype=np.float32), np.arange(ny,dtype=np.float32)) * transform

    da.close()

    return x,y,elevation,proj

def to_netcdf(folder):
    
    files = glob.glob(folder + os.sep + "*.tif")
    output = [f.split(os.sep)[-1][:-4] for f in files]
    filename = folder.split(os.sep)[-1] + ".nc"
    ds = nc.Dataset(folder + os.sep + filename, 'w', format='NETCDF4')
    
    x,y,z,proj = opentiff(files[0])
    
    ds.createDimension('id1', np.shape(x)[0])
    ds.createDimension('id2', np.shape(x)[1])

    x_out = ds.createVariable('x', 'f4', ('id1', 'id2'), zlib=True)
    y_out = ds.createVariable('y', 'f4', ('id1', 'id2'), zlib=True)
    
    x_out[:,:] = x
    y_out[:,:] = y
    
    for f,o in zip(files,output):
    
        x,y,z,proj = opentiff(f)
        
        
        z_out = ds.createVariable(o, 'f4', ('id1', 'id2'), zlib=True)
        
        z_out[:,:] = z
        
    ds.close()
    
    return folder + os.sep + filename

def dataverse_upload(folder):
    
    # --------------------------------------------------
    # Update the 4 params below to run this code
    # --------------------------------------------------
    dataverse_server = 'https://dataverse.geus.dk'
    api_key = '44154c44-ec27-46c5-945e-9f46bb102950'
    #persistentId = 'doi:10.22008/FK2/V9XDJT'    
    
    
    doi = pd.read_csv("GEUSdataverse_doi.csv")
    
    basefolder = os.getcwd()
    
    #os.chdir(folder.split(os.sep)[-2])
    
    nc_file = to_netcdf(basefolder + folder)
    
    
    #os.chdir(folder.split(os.sep)[-2])
    
    #files = glob.glob(folder.split(os.sep)[-1] + os.sep + "*.tif")
    
    #print(files)
    
    #output_filename = folder.split(os.sep)[-1] + ".zip"
    #output_filename_done = folder.split(os.sep)[-1] + "zip.zip"
    
    #zout = zipfile.ZipFile(output_filename, "w", zipfile.ZIP_LZMA)
    #zout_out =  zipfile.ZipFile(output_filename_done, "w", zipfile.ZIP_LZMA)
    
    
    #for i,fname in enumerate(files):
    #    zout.write(fname)
        
    #zout.close()
    
    #zout_out.write(output_filename)
    
    #zout_out.close()
    
    
    #zipname = output_filename.split(os.sep)[-1]
    fileup = {'file': open(nc_file, "rb")}
    
    #fileup = open(output_filename, "rb")
    output_filename = nc_file.split(os.sep)[-1]
    filedate =  nc_file[-13:-3]
    fileyear = filedate[:4]
    persistentId = doi[fileyear][0]
    
    
    url_persistent_id = '%s/api/datasets/:persistentId/add?persistentId=%s&key=%s' % (dataverse_server, persistentId, api_key)
    
    #print(fileup)
    
    file_description = f"EDC SICE output: {output_filename}, date: {filedate}"
    
    params = dict(description=file_description,
                        directoryLabel=filedate)

    params_as_json_string = json.dumps(params)

    payload = dict(jsonData=params_as_json_string)

    r = requests.post(url_persistent_id,data = payload, files=fileup)
    
    #print(r.json())
    
    os.chdir(basefolder)
    print(r.json()['status'])
    
    if r.json()['status'] == 'ERROR':
            print(r.json())
    
 