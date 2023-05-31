
# Various utilities
import argparse
import sys
import os
import json
from shapely import geometry, wkt
import IPython.display
import datetime as dt
import numpy as np
from numpy import asarray as ar
import glob
import shutil
import logging
import concurrent.futures
import time
from multiprocessing import set_start_method,get_context
import geopandas as gpd
import rasterio as rio
from sentinelhub import SentinelHubBatch, SentinelHubRequest, Geometry, CRS, DataCollection, MimeType, SHConfig, BBox, bbox_to_dimensions, ServiceUrl
from utils import merge_tiffs, importToBucket
from shapely.geometry import Polygon
import tarfile
from sice_edc import pySICE_EDC
from pysice import proc
from cams import get_maps
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


if sys.version_info < (3, 4):
    raise "must use python 3.6 or greater"
    

def parse_arguments():
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("-d","--day", type=str,help="Please input the day you want to proces")
        parser.add_argument("-a","--area", type=str,help="Please input the area you want to proces")
        parser.add_argument("-r","--res", type=int,help="Please input the resolution you want to proces")
        parser.add_argument("-t","--test", type=int, default = 0)
        args = parser.parse_args()
        return args


    
#define the main processing function that call individual tiles on SX and storres the data locally

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
    
def tarextract(ff,dd):
        
        tar = tarfile.open(ff, "r:")
        tar.extractall(path=dd)
        tar.close()

def processList(folder, bounds,res,yes):
    bbox = BBox(bbox=bounds, crs="EPSG:3413")
    size = bbox_to_dimensions(bbox, resolution=res)
    folderPath = f'{DL_FOLDER}/{folder}'
    if yes == 1:
        print("Still Going")
    if os.path.exists(folderPath):
        if FORCE_DOWNLOAD:
            pass
        else:
            logging.info(f"Folder already exists {folderPath}")
            return
    
    try:
        #logging.info(f"Processing folder {folderPath}")
        request1 = SentinelHubRequest(
            evalscript=evalscript1,
            data_folder=folderPath,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL3_OLCI,
                    identifier="OLCI",
                    time_interval=date_range,
                    upsampling="BICUBIC",
                    downsampling="BICUBIC",
                ),
            ],
            responses=[
                SentinelHubRequest.output_response('toa1', MimeType.TIFF),
                SentinelHubRequest.output_response('toa2', MimeType.TIFF),
                SentinelHubRequest.output_response('toa3', MimeType.TIFF),
                SentinelHubRequest.output_response('toa4', MimeType.TIFF),
                SentinelHubRequest.output_response('toa5', MimeType.TIFF),
                SentinelHubRequest.output_response('toa6', MimeType.TIFF),
                SentinelHubRequest.output_response('toa7', MimeType.TIFF),
                SentinelHubRequest.output_response('toa8', MimeType.TIFF),
                SentinelHubRequest.output_response('toa9', MimeType.TIFF),
                SentinelHubRequest.output_response('toa10', MimeType.TIFF),
                SentinelHubRequest.output_response('toa11', MimeType.TIFF),
                SentinelHubRequest.output_response('toa12', MimeType.TIFF),
                SentinelHubRequest.output_response('toa13', MimeType.TIFF),
                SentinelHubRequest.output_response('toa14', MimeType.TIFF),
                SentinelHubRequest.output_response('toa15', MimeType.TIFF),
                SentinelHubRequest.output_response('toa16', MimeType.TIFF),
                SentinelHubRequest.output_response('toa17', MimeType.TIFF),
                SentinelHubRequest.output_response('toa18', MimeType.TIFF),
                SentinelHubRequest.output_response('toa19', MimeType.TIFF),
                SentinelHubRequest.output_response('toa20', MimeType.TIFF),
                SentinelHubRequest.output_response('toa21', MimeType.TIFF),
                SentinelHubRequest.output_response('saa', MimeType.TIFF),
                SentinelHubRequest.output_response('vaa', MimeType.TIFF),
                SentinelHubRequest.output_response('vza', MimeType.TIFF),
                SentinelHubRequest.output_response('sza', MimeType.TIFF),
                SentinelHubRequest.output_response('totalozone', MimeType.TIFF),
                SentinelHubRequest.output_response('pixelid', MimeType.TIFF),
                SentinelHubRequest.output_response('userdata', MimeType.JSON),
            ],
            bbox=bbox,
            size=size,
            config=sh_config,
        )
        
        resp1 = request1.get_data(save_data=True)
        request2 = SentinelHubRequest(
            evalscript=evalscript2,
            data_folder=folderPath,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL3_SLSTR,
                    identifier="SLSTR",
                    time_interval=date_range,
                    upsampling="BICUBIC",
                    downsampling="BICUBIC",
                ),
            ],
            responses=[
                SentinelHubRequest.output_response('S7', MimeType.TIFF),
                SentinelHubRequest.output_response('S8', MimeType.TIFF),
                SentinelHubRequest.output_response('S9', MimeType.TIFF),
            ],
            bbox=bbox,
            size=size,
            config=slstr_config,
        )
        resp2 = request2.get_data(save_data=True)
        
        
        request3 = SentinelHubRequest(
            evalscript=evalscript3,
            data_folder=folderPath,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL3_SLSTR,
                    identifier="SLSTR",
                    time_interval=date_range,
                    upsampling="BICUBIC",
                    downsampling="BICUBIC",
                ),
            ],
            responses=[
                SentinelHubRequest.output_response('S1', MimeType.TIFF),
                SentinelHubRequest.output_response('S5', MimeType.TIFF),
            ],
            bbox=bbox,
            size=size,
            config=slstr_config,
        )
        resp3 = request3.get_data(save_data=True)
        
        request4 = SentinelHubRequest(
            evalscript=evalscript4,
            data_folder=folderPath,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.DEM_COPERNICUS_30,
                    identifier="COP_30",
                    upsampling="BICUBIC",
                    downsampling="BICUBIC",
                ),
            ],
            responses=[
                SentinelHubRequest.output_response('dem', MimeType.TIFF),
            ],
            bbox=bbox,
            size=size,
            config=sh_config,
        )
        
        resp4 = request4.get_data(save_data=True)
        
        
         
        
    except Exception as e:
        logging.error(e)
        print(size)
        print(bbox)
        print(folder)    
        yes = 1
        
        
        
class ConcurrentSHRequestExecutor:
    def __init__(self, toProcess):
        self.toProcess = toProcess
        
    def operation(self, chunk):
        processList(round(self.toProcess.id[chunk]) , list(self.toProcess.geometry[chunk].bounds),res,0)
        
    def executeRequests(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.operation, np.arange(0, len(self.toProcess.values)), chunksize=4)
        print("done")

        
def cloudfilt(profile,scene,cd):
    
    scenespath = glob.glob(scene + os.sep + "*.tif")
    
    if len(scenespath) == 0:
        
        scenespath = glob.glob(scene + os.sep + "*.tiff")
    
    for i,scene in enumerate(scenespath):
        
        name = scene.split(os.sep)[-1]
        
        if name != "SCDA.tif":
            
           
            
            data = rio.open(scene).read(1)
            
            if name == "Snow_Albedo_Sph.tif":
                print(np.nanmean(data)) 
            
            data[cd == 255] = np.nan
            #data[data == 0] = np.nan
            
            if name == "response.tiff":
                out = scene[:-5] + "_filt.tif"
            else:
                out = scene[:-4] + "_filt.tif"
            
            with rio.open(out,'w',**profile) as dst:
                dst.write(data, 1)        
        
    
        
def CloudMasking(mainpath,scene):
    

    #saving profile metadata only for the first iteration
    meta = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*toa1.tif')
    metaresponse = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*response.tiff')
    if meta:

        cdpath = glob.glob(mainpath + os.sep + scene +  os.sep + "*" + os.sep + "*SCDA.tif")

        cd = rio.open(cdpath[0]).read(1)

        profile = rio.open(meta[0]).profile
        #print(meta[0][:-18])
        cloudfilt(profile,meta[0][:-8],cd)

        try:
            cloudfilt(profile,metaresponse[0][:-13],cd)
        except: 
            logging.info("Error in Meta Response Tiff")
            logging.info(scene)
            logging.info(metaresponse)
                
            

def nanRemoval(datapath,inpath):

    data = rio.open(datapath)
    profile = data.profile
    
    dataz = data.read(1)
    #print("no of nans: ",dataz[np.isnan(dataz)] )
    dataz[np.isnan(dataz)] = np.nanmean(dataz)
    #print("no of zeros: ", dataz[dataz == 0]  )
    dataz[dataz == 0] = np.nanmean(dataz)
    
    with rio.open(datapath,'w',**profile) as dst:
        dst.write(dataz, 1)            

        
def radiometric_calibration(R16path,scene,inpath):
    '''
    Sentinel-3 Product Notice – SLSTR:
    "Based on the analysis performed to-date, a recommendation has been put forward to users to
    adjust the S5 and S6 reflectances by factors of 1.12 and 1.20 respectively in the nadir view and
    1.15 and 1.26 in the oblique view. Uncertainty estimates on these differences are still to be
    evaluated and comparisons with other techniques have yet to be included."
    
    INPUTS:
        R16: Dataset reader for Top of Atmosphere (TOA) reflectance channel S5.
             Central wavelengths at 1.6um. [rasterio.io.DatasetReader]
        scene: Scene on which to compute SCDA. [string]
        
    OUTPUTS:
        {inpath}/r_TOA_S5_rc.tif: Adjusted Top of Atmosphere (TOA)
                                  reflectance for channel S5.
    '''
    R16 = rio.open(R16path)
    profile_R16 = R16.profile
    factor = 1.12
    R16_data = R16.read(1)
    R16_rc = R16_data*factor
    outpath =  R16path[:-6] 
    with rio.open(outpath + 'S5_rc.tif','w',**profile_R16) as dst:
        dst.write(R16_rc, 1)        
        
def SCDA_v20(R550, R16, BT37, BT11, BT12, profile, scene, 
             inpath, despath, SICE_toolchain=True):
    
    '''
    
    INPUTS:
        inpath: Path to the folder of a given date containing extracted scenes
                in .tif format. [string]
        SICE_toolchain: if True: cloud=255, clear=1
                        if False: cloud=1, clear=0
        profile: Profile to save outputs. [rasterio.profiles.Profile]
        scene: Scene on which to compute the SCDA. [string]
        R550, R16: Top of Atmosphere (TOA) reflectances for channels S1 and S5.
                   Central wavelengths at 550nm and 1.6um. [arrays]
        BT37, BT11, BT12: Gridded pixel Brightness Temperatures (BT) for channels 
                          S7, S8 and S9 (1km TIR grid, nadir view). Central 
                          wavelengths at 3.7, 11 and 12 um. [arrays]
              
    OUTPUTS:
        {inpath}/NDSI.tif: Normalized Difference Snow Index (NDSI) in a 
                           .tif file, stored in {inpath}. [.tif]
        {inpath}/SCDA.tif: Simple Cloud Detection Algorithm (SCDA) results 
                           in a .tif file, stored in {inpath}. 
                           clouds=1, clear=0 [.tif]
         
    '''
    
    
    # Checking for nan - getting mean val. 
    
    #determining the NDSI, needed for the cloud detection
    NDSI=(R550-R16)/(R550+R16)
    
    
    
    
    
    #NDSIpath = glob.glob(inpath + os.sep + scene + os.sep + * + os.sep + '*NDSI.tif')
    #with rasterio.open(inpath+os.sep+scene+os.sep+'NDSI.tif','w',**profile) as dst:
    #    dst.write(NDSI, 1)
    
    #initializing thresholds
    base=np.empty((R550.shape[0],R550.shape[1]))
    THR=base.copy()
    THR[:]=np.nan
    THRmax=base.copy()
    THRmax[:]=-5.5 
    S=base.copy()
    S[:]=1.1
    
    #masking nan values
    mask_invalid=np.isnan(R550)
    
    #tests 1 to 5, only based on inputs
    t1=ar(R550>0.30)*ar(NDSI/R550<0.8)*ar(BT12<=290)
    t2=ar(BT11-BT37<-13)*ar(R550>0.15)*ar(NDSI >= -0.30)\
       *ar(R16>0.10)*ar(BT12<=293)
    t3=ar(BT11-BT37<-30)
    t4=ar(R550<0.75)*ar(BT12>265)
    t5=ar(R550>0.75)
    
    cloud_detection=t1
    cloud_detection[cloud_detection==False]=t2[cloud_detection==False]
    cloud_detection[cloud_detection==False]=t3[cloud_detection==False]
    
    THR1=0.5*BT12-133
    
    THRmax[t4==False]=-8
    THR=np.minimum(THR1,THRmax)
    S[t5==False]=1.5
    
    #test 6, based on fluctuating thresholds
    t6=ar(BT11-BT37<THR)*ar(NDSI/R550<S)*ar((NDSI>=-0.02) & (NDSI<=0.75))\
       *ar(BT12<=270)*ar(R550>0.18)

    cloud_detection[cloud_detection==False]=t6[cloud_detection==False]
    
    
    #masking nan values
    #cloud_detection[mask_invalid]=True
    
    
    
    if SICE_toolchain:
        cloud_detection = np.where(cloud_detection==True, 255.0, 1.0)
    
    #writing results
    profile_cloud_detection=profile.copy()
    if SICE_toolchain:
        profile_cloud_detection.update(dtype=rio.uint8, nodata=255)
    else:
        profile_cloud_detection.update(dtype=rio.uint8)
    #print(despath + 'SCDA.tif')
    with rio.open(despath + 'SCDA.tif','w',**profile_cloud_detection) as dst:
        dst.write(cloud_detection.astype(np.uint8), 1)
        
    return cloud_detection, NDSI

def SCDA(mainpath,scene):
    
    #saving profile metadata only for the first iteration
    meta = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S1.tif')
    #pathjohn = mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S1.tif'
    #print("metapath: " + pathjohn)
    if meta:

        profile = rio.open(meta[0]).profile

        #calibrating R16
        R16path = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S5.tif')
        nanRemoval(datapath = R16path[0], inpath = mainpath)
        radiometric_calibration(R16path = R16path[0], scene = scene, inpath = mainpath)


        #loading inputs
        R550path = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S1.tif')

        nanRemoval(datapath = R550path[0], inpath = mainpath)
        R550=rio.open(R550path[0]).read(1)


        R16path = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S5_rc.tif')
        R16=rio.open(R16path[0]).read(1)
        
        BT37path = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S7.tif')
        nanRemoval(datapath = BT37path[0], inpath = mainpath)
        BT37 = rio.open(BT37path[0]).read(1)
        
        BT11path = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S8.tif')
        nanRemoval(datapath = BT11path[0], inpath = mainpath)
        BT11=rio.open(BT11path[0]).read(1)
        
        BT12path = glob.glob(mainpath + os.sep + scene + os.sep + "*" + os.sep + '*S9.tif')
        nanRemoval(datapath = BT12path[0], inpath = mainpath)
        BT12=rio.open(BT12path[0]).read(1)
        
        #running SCDA v2.0 and v1.4
        cd,NDSI=SCDA_v20(R550 = R550, R16 = R16, BT37 = BT37, BT11 = BT11, BT12 = BT12, scene = scene, profile = profile, inpath = mainpath,despath = BT12path[0][:-6])

        #os.remove(R16path[0])
        #os.remove(R550path[0])

    else: 
        print("Scene is corrupted, Skipping...") 
        
if __name__ == "__main__":       
    
    try:
        set_start_method("spawn")
    except:
        pass
    
    args = parse_arguments()

    date = args.day
    area = args.area
    res = args.res # minimum resolution of data is 300m
    test = args.test
    
    
    # create logs folder
    if not os.path.exists("logs"):
        os.makedirs("logs")
                                                          
    # right now we only log to consol
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(f'logs/sice_sh_{time.strftime("%Y_%m_%d",time.localtime())}.log'),
            logging.StreamHandler()
        ])

    #External variables
    # Set the date of calculation
    # resolution (m)

 
    #area of interest
    if area == "Greenland":
        
        toProcess = gpd.read_file("Greenland_50kmTiles.geojson")

    #target projection of the final results
    projection = '3413'

    # log processing parameters - don't log any S3 information
    logging.info(f'Date: {date}')
    logging.info(f'AOI: {area}')
    logging.info(f'Projection: {projection}')

    #system settings

    #base folder where the code is located
    USR_PATH = os.path.abspath('.')
    EVAL_SCRIPT1_PATH = os.path.join(USR_PATH, 'S3Adata.js') 
    EVAL_SCRIPT2_PATH = os.path.join(USR_PATH, 'eval1000Tile.js') 
    EVAL_SCRIPT3_PATH = os.path.join(USR_PATH, 'evalSLSTR500.js') 
    EVAL_SCRIPT4_PATH = os.path.join(USR_PATH, 'dem.js') 
    
    #delete download folder after processing - will save space but will download all the data for each requwst (otherwise the cached tile data will be used)
    DELETE_DOWNLOAD_FOLDER = True
    FORCE_DOWNLOAD = True
    #OUTPUT_DIR = os.path.join(USR_PATH, "output") #local folder
    OUTPUT_DIR =  os.path.join(USR_PATH, "output") #local folder # will be copied to the local folder of the user requesting the data
    # create logs folder

    if not os.path.exists("output"):
        os.makedirs("output")


    logging.info("System configuration ok.")    

    # initial ENV configuration
    #SH_CLIENT_ID = %env SH_CLIENT_ID
    #SH_CLIENT_SECRET = %env SH_CLIENT_SECRET
    
    SH_CLIENT_ID = os.environ.get('SH_CLIENT_ID')
    SH_CLIENT_SECRET = os.environ.get('SH_CLIENT_SECRET')
    
    #print(SH_CLIENT_ID)
    #print(SH_CLIENT_SECRET)
    
    sh_config = SHConfig()
    sh_config.sh_base_url = "https://creodias.sentinel-hub.com"
    sh_config.download_timeout_seconds=300

    sh_config.sh_client_id = SH_CLIENT_ID
    sh_config.sh_client_secret = SH_CLIENT_SECRET

    sh_config.save()
    
    slstr_config = SHConfig()
    slstr_config.sh_base_url = "https://creodias.sentinel-hub.com"
    slstr_config.download_timeout_seconds=300

    slstr_config.sh_client_id = SH_CLIENT_ID
    slstr_config.sh_client_secret = SH_CLIENT_SECRET

    slstr_config.save()

    # Evalscript
    with open(EVAL_SCRIPT1_PATH, "r") as f:
        evalscript1 = f.read()
        
    # Evalscript
    with open(EVAL_SCRIPT2_PATH, "r") as f:
        evalscript2 = f.read()
        
        # Evalscript
    with open(EVAL_SCRIPT3_PATH, "r") as f:
        evalscript3 = f.read()
        
    with open(EVAL_SCRIPT4_PATH, "r") as f:
        evalscript4 = f.read()    
    

    logging.info("Configuration ok.")    

    date_range = (f'{date}T08:00:00', f'{date}T18:00:00')


    DATE_FOLDER = date.replace("-","_")
    DL_FOLDER =  os.path.join('downloads', str(res), DATE_FOLDER)
    PROCESSED_FOLDER = f'{DL_FOLDER}/processed'

    

    logging.info("Loading grid")

    logging.info("Calculating tiles to be processed.")    

    #make the intersection with the polygon so that we only calculate tiles inside the polygon
    #Remove chunks that are too small to be processed

    #if os.path.exists(DL_FOLDER):
    #    shutil.rmtree(DL_FOLDER)
    #    logging.info(f'Folder {DL_FOLDER} deleted')


    # make concurrent calls using all the available processor
    logging.info(f'Processing tiles. Number of tiles to process: {len(toProcess.id)}')

    # This downloads all the tiles and do some proc
    # Merging happens after!!!
    executor = ConcurrentSHRequestExecutor(toProcess)
    executor.executeRequests()  

    logging.info('Done')

    # check if all the tiles were correctly downloaded - sometimes some fail in the multi-thread mode
    filenamesList = glob.glob(f'./{DL_FOLDER}/*/*/response.tar')
    missing = [];

    for id in toProcess.id:
        id = round(id)
        isPresent = False
        for f in filenamesList:
            if str(id) in f: 
                isPresent = True
                continue
        if not isPresent:    
            missing.append(id)
            logging.debug(f"Id is missing: {id}")

    notProcessed = toProcess[toProcess.id.isin(missing)]

    logging.info(f'Number of failed tiles: {len(missing)}')

    # compute missing tile individually - much slower than multy-threaded
    logging.info('Computing failed tiles')
    for idx in notProcessed.index: 
        id = round(notProcessed.id[idx])
        bounds = list(notProcessed.loc[idx].geometry.bounds)
        processList(id, bounds,res,0)    

    logging.info('Done')

    #extract data from tar responses
    logging.info('Extracting .tar responses')
    filenamesList = glob.glob(f'./{DL_FOLDER}/*/*/response.tar')
    dest = [file.replace('response.tar', '') for file in filenamesList]
    with get_context("spawn").Pool(12) as p:     
            p.starmap(tarextract,zip(filenamesList,dest))
            
    

    logging.info("Done")
    
    
    

    #define the products that will be computed
    products = ['toa1_filt.tif','toa2_filt.tif','toa3_filt.tif','toa4_filt.tif','toa5_filt.tif','toa6_filt.tif','toa7_filt.tif','toa8_filt.tif','toa9_filt.tif',\
               'toa10_filt.tif','toa11_filt.tif','toa12_filt.tif','toa13_filt.tif','toa14_filt.tif','toa15_filt.tif','toa16_filt.tif','toa17_filt.tif','toa18_filt.tif',\
               'toa19_filt.tif','toa20_filt.tif','toa21_filt.tif','vza_filt.tif','sza_filt.tif','vaa_filt.tif','saa_filt.tif','totalozone_filt.tif','albedo_bb_spherical_sw.tif',
               'albedo_bb_planar_sw.tif','grain_diameter.tif','r0.tif','SCDA.tif','albedo_spectral_planar_21.tif','albedo_spectral_planar_17.tif','isnow.tif','factor.tif']
    #products = ['Snow_Grain_Diameter.tif']
    
    # Create SCDA of each tile
           
        


    logging.info("Calculating Cloud Mask")
    basefolder = os.getcwd()
    parent = basefolder + os.sep + DL_FOLDER
    scenes = os.listdir(parent)
    main = [parent for x in range(len(scenes))]
    #print(main)
    #print(scenes)
    
    try: 

        with get_context("spawn").Pool(12) as p:     

            p.starmap(SCDA,zip(main,scenes))

    except:
        logging.info("Error in SCDA")
    #SCDA("/home/jovyan/SICE/" + DL_FOLDER)

    logging.info('Done')

    logging.info("Removing Clouds")
    try: 

        with get_context("spawn").Pool(12) as p:     

            p.starmap(CloudMasking,zip(main,scenes))

    except:
        logging.info("Error in CloudMasking")
    
    logging.info('Done')
        
    sicePaths = glob.glob(basefolder  + os.sep + DL_FOLDER + "/*/*/*toa1.tif")
    demPaths = glob.glob(basefolder + os.sep +  DL_FOLDER + "/*/*/*response.tiff")

    sicePathsfilt = [[s[:-8]  for s in sicePaths if (s.split(os.sep)[-3]==d.split(os.sep)[-3])] for d in demPaths]
    sicePathsfilt = [item for sublist in sicePathsfilt for item in sublist]
    
    demPathsfilt = [[d[:-13]  for s in sicePaths if (s.split(os.sep)[-3]==d.split(os.sep)[-3])] for d in demPaths]
    demPathsfilt = [item for sublist in demPathsfilt for item in sublist]
   
    sceneno = [[s.split(os.sep)[-3]  for s in sicePaths if (s.split(os.sep)[-3]==d.split(os.sep)[-3])] for d in demPaths]
    sceneno = [item for sublist in sceneno for item in sublist]
    
    datecams = [date for x in range(len(demPathsfilt))]
    
    logging.info("Getting Cams Maps.....")
    old_stdout = sys.stdout # backup current stdout
    sys.stdout = open(os.devnull, "w")

    
    with get_context("spawn").Pool(12) as p:     
            #print(sceneno)
            p.starmap(get_maps,zip(sicePathsfilt,sicePathsfilt, datecams,sceneno))
    
    
    sys.stdout = old_stdout # reset old stdout
    
    logging.info('Done')

    logging.info('Executing pysice')
    
    with get_context("spawn").Pool(12) as p:     
                    
            p.starmap(proc,zip(sicePathsfilt,demPathsfilt))

    logging.info('Done')
        


    #merge individual tiles into one single image
    for productName in products:
        prodResult = productName.replace(".tif", '_merged.tif')
        if os.path.exists(prodResult):
            os.remove(prodResult)
            logging.info(f'Deleted file: {prodResult}')
        logging.info(f'Creating file {prodResult}')
        filenamesList = glob.glob(f'./{DL_FOLDER}/*/*/{productName}')
        merge_tiffs(filenamesList, prodResult, overwrite=True)
        if not os.path.exists(PROCESSED_FOLDER):
            os.makedirs(PROCESSED_FOLDER)
        shutil.move(prodResult, f'{PROCESSED_FOLDER}/{prodResult}')


    resultsDataPath = os.path.join(USR_PATH, PROCESSED_FOLDER)
    processedDataPath = os.path.join(USR_PATH, PROCESSED_FOLDER)
    for product in products:
            srcFile = processedDataPath + "/" + product.replace(".tif", "_merged.tif")
            destFile = processedDataPath + "/" + product
            if os.path.exists(srcFile):
                os.rename(srcFile, destFile)
                
    finalOutput = f'{OUTPUT_DIR}/sice_{res}_{DATE_FOLDER}'

    if os.path.exists(finalOutput):
            shutil.rmtree(finalOutput)
            logging.info(f'Folder {finalOutput} deleted')

    logging.info(f'Copying results to {finalOutput}')
    shutil.copytree(resultsDataPath, finalOutput)

    if DELETE_DOWNLOAD_FOLDER and os.path.exists(DL_FOLDER):
        shutil.rmtree(DL_FOLDER)
        logging.info(f'Folder {DL_FOLDER} deleted')
        if os.path.exists(resultsDataPath):
            shutil.rmtree(resultsDataPath)
            logging.info(f'Folder {resultsDataPath} deleted')


    finalOutput =  f'{OUTPUT_DIR}/sice_{res}_{DATE_FOLDER}'
    
    
    