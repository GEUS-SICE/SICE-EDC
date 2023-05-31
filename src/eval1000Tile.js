
// VERSION=3

function setup() {
  return {
    input: [
        {
        datasource: "OLCI",
        bands: ["SZA"],                  
      },
      {
        datasource: "SLSTR",
        bands: ["S7","S8","S9"]
      },
    ],
    output: [
     {
        id: "pixelid",
        bands: 1,
        sampleType: "FLOAT32",      
      },
      {
        id: "S7",
        bands: 1,
        sampleType: "FLOAT32",      
      },
      {
        id: "S8",
        bands: 1,
        sampleType: "FLOAT32",      
      },
      {
        id: "S9",
        bands: 1,
        sampleType: "FLOAT32",      
      }
    ],
    mosaicking: "TILE",
  };
}

// function updateOutput(outputs, collections) {
//  Object.values(outputs).forEach((output) => {
//    output.bands = collections.scenes.length;
//  });
// }

// Set constants as global variables which can be used in all functions

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {
    
    
    let S7_out = [];
    let S8_out = [];
    let S9_out = [];
    let pixelid_out = [];
    let time_slstr = 0;
    let sza_all = 180;
    let time_idx = 0;
    let idx = 0;
    
    for (var i=0; i < scenes.OLCI.scenes.length; i++){
        if (scenes.OLCI.scenes[i].tileOriginalId.slice(43, 46) == "S3A") {
            if (samples.OLCI[i].SZA < sza_all) {
                time_idx = scenes.OLCI.scenes[i].tileOriginalId.slice(68, 70)
                sza_all = samples.OLCI[i].SZA
            }
        }
    }
    
    //for (var i=0; i < scenes.OLCI.scenes.length; i++){
    //    if (scenes.OLCI.scenes[i].tileOriginalId.slice(43, 46) == "S3A") {
    //        
    //            time_idx = scenes.OLCI.scenes[i].tileOriginalId.slice(68, 70)
    //            
    //        
    //    }
   // }
    
    
    for (var i=0; i < scenes.SLSTR.scenes.length; i++){
        
        if (scenes.SLSTR.scenes[i].tileOriginalId.slice(44, 47) == "S3A") {
           time_slstr = scenes.SLSTR.scenes[i].tileOriginalId.slice(69, 71)
            
            if (parseInt(time_idx) == parseInt(time_slstr)) {
                
                idx = scenes.SLSTR.scenes[i].__idx
              
            }
        }
    }
    
    pixelid_out.push(idx);
    S7_out.push(samples.SLSTR[idx].S7);
    S8_out.push(samples.SLSTR[idx].S8);
    S9_out.push(samples.SLSTR[idx].S9);
    
    
    return {
      pixelid: pixelid_out,  
      S7: S7_out,
      S8: S8_out,
      S9: S9_out,  
    };
  }

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
  outputMetadata.userData = { "tiles":  scenes }
    
  }
