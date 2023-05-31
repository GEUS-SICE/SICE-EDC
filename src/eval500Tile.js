//VERSION=3

function setup() {
  return {
    input: [  
      {
        datasource: "OLCI",
        bands: ["B01","B02","B03","B04","B05","B06","B07","B08","B09","B10","B11","B12","B13","B14","B15","B16","B17","B18","B19","B20","B21","SZA","VZA","SAA","VAA","TOTAL_COLUMN_OZONE"],                  
      }
    ],
    output: [
      {
        id: "toa1",
        bands: 1,
        sampleType: "FLOAT32",      
      },        
      {
        id: "toa2",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa3",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa4",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa5",
        bands: 1,
        sampleType: "FLOAT32",
      },
      {
        id: "toa6",
        bands: 1,
        sampleType: "FLOAT32",
      }, 
      {
        id: "toa7",
        bands: 1,
        sampleType: "FLOAT32",      
      },        
      {
        id: "toa8",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa9",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa10",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa11",
        bands: 1,
        sampleType: "FLOAT32",
      },
      {
        id: "toa12",
        bands: 1,
        sampleType: "FLOAT32",
      },
      {
        id: "toa13",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa14",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa15",
        bands: 1,
        sampleType: "FLOAT32",
      },
      {
        id: "toa16",
        bands: 1,
        sampleType: "FLOAT32",
      }, 
      {
        id: "toa17",
        bands: 1,
        sampleType: "FLOAT32",      
      },        
      {
        id: "toa18",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa19",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa20",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "toa21",
        bands: 1,
        sampleType: "FLOAT32",
      },        
      {
        id: "vza",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "sza",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "saa",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "vaa",
        bands: 1,
        sampleType: "FLOAT32",        
      },
      {
        id: "totalozone",
        bands: 1,
        sampleType: "FLOAT32",
      }
    ],
    mosaicking: "SIMPLE",
  };
}

//function updateOutput(outputs, collections) {
//  Object.values(outputs).forEach((output) => {
//    output.bands = collections.scenes.length;
//  });
//}

// Set constants as global variables which can be used in all functions

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {

   
    var avg1 = 0;
    var avg2 = 0;
    var avg4 = 0;
    var avg5 = 0;
    var avg6 = 0;
    var avg7 = 0;
    var avg8 = 0;
    var avg9 = 0;
    var avg10 = 0;
    var avg11 = 0;
    var avg12 = 0;
    var avg13 = 0;
    var avg14 = 0;
    var avg15 = 0;
    var avg16 = 0;
    var avg17 = 0;
    var avg18 = 0;
    var avg19 = 0;
    var avg20 = 0;
    var avg21 = 0;
    var avgsza = 0;
    var avgvza = 0;
    var avgsaa = 0;
    var avgvaa = 0;
    var avgtotalozone = 0;
    
    
    var count = 0;
    
    
    let toa1_out = [];
    let toa2_out = [];
    let toa3_out = [];
    let toa4_out = [];
    let toa5_out = [];
    let toa6_out = [];
    let toa7_out = [];
    let toa8_out = [];
    let toa9_out = [];
    let toa10_out = [];
    let toa11_out = [];
    let toa12_out = [];
    let toa13_out = [];
    let toa14_out = [];
    let toa15_out = [];
    let toa16_out = [];
    let toa17_out = [];
    let toa18_out = [];
    let toa19_out = [];
    let toa20_out = [];
    let toa21_out = [];
    let sza_out = [];
    let vza_out = [];
    let saa_out = [];
    let vaa_out = [];
    let totalozone_out = [];
    let stop = 0;
    
    // (scenes.tiles[i].tileOriginalId.slice(43, 46) == "S3B") 
    
    //for (var i=0; i < samples.length; i++){        
          
    //    if (stop == 0){ 
    //        if (Number(scenes.tiles[i].date.slice(-9, -7)) < "12"){ 
    //        
    //            toa1_out.push(samples[i].B01);
    //            toa2_out.push(samples[i].B02);  
    //            toa3_out.push(samples[i].B03);
    //            toa4_out.push(samples[i].B04);
    //            toa5_out.push(samples[i].B05);
    //            toa6_out.push(samples[i].B06);
    //            toa7_out.push(samples[i].B07);
    //            toa8_out.push(samples[i].B08);
    //            toa9_out.push(samples[i].B09);
    //            toa10_out.push(samples[i].B10);
    //            toa11_out.push(samples[i].B11);
    //            toa12_out.push(samples[i].B12);
    //            toa13_out.push(samples[i].B13);
    //            toa14_out.push(samples[i].B14);
    //            toa15_out.push(samples[i].B15);
    //            toa16_out.push(samples[i].B16);
    //            toa17_out.push(samples[i].B17);
    //            toa18_out.push(samples[i].B18);
    //            toa19_out.push(samples[i].B19);
    //            toa20_out.push(samples[i].B20);
    //            toa21_out.push(samples[i].B21); 

    //            sza_out.push(samples[i].SZA);
    //            vza_out.push(samples[i].VZA);
    //            saa_out.push(samples[i].SAA);
    //            vaa_out.push(samples[i].VAA);
    //            totalozone_out.push(samples[i].TOTAL_COLUMN_OZONE);

    //            stop = 1
        

                
        //avg1 = avg1 + samples[i].B01
        //avg2 = avg2 + samples[i].B02
        //avg3 = avg3 + samples[i].B03
        //avg4 = avg4 + samples[i].B04
        //avg5 = avg5 + samples[i].B05
        //avg6 = avg6 + samples[i].B06
        //avg7 = avg7 + samples[i].B07
        //avg8 = avg8 + samples[i].B08
        //avg9 = avg9 + samples[i].B09
        //avg10 = avg10 + samples[i].B10
        //avg11 = avg11 + samples[i].B11
        //avg12 = avg12 + samples[i].B12
        //avg13 = avg13 + samples[i].B13
        //avg14 = avg14 + samples[i].B14
        //avg15 = avg15 + samples[i].B15
        //avg16 = avg16 + samples[i].B16
        //avg17 = avg17 + samples[i].B17
        //avg18 = avg18 + samples[i].B18
        //avg19 = avg19 + samples[i].B19
        //avg20 = avg20 + samples[i].B20
        //avg21 = avg21 + samples[i].B21
        //avgsza = avgsza + samples[i].SZA
        //avgvza = avgvza + samples[i].VZA
        //avgsaa = avgsaa + samples[i].SAA
        //avgvaa = avgvaa + samples[i].VAA
        //avgtotalozone = avgtotalozone + samples[i].TOTAL_COLUMN_OZONE
        
         //    }
         //}
         //count++
    
    
     //}
    
    
    //toa1_out.push(avg1/count);
    //toa2_out.push(avg2/count);  
    //toa3_out.push(avg3/count);
    //toa4_out.push(avg4/count);
    //toa5_out.push(avg5/count);
    //toa6_out.push(avg6/count);
    //toa7_out.push(avg7/count);
    //toa8_out.push(avg8/count);
    //toa9_out.push(avg9/count);
    //toa10_out.push(avg10/count);
    //toa11_out.push(avg11/count);
    //toa12_out.push(avg12/count);
    //toa13_out.push(avg13/count);
    //toa14_out.push(avg14/count);
    //toa15_out.push(avg15/count);
    //toa16_out.push(avg16/count);
    //toa17_out.push(avg17/count);
    //toa18_out.push(avg18/count);
    //toa19_out.push(avg19/count);
    //toa20_out.push(avg20/count);
    //toa21_out.push(avg21/count); 
      
    //sza_out.push(avgsza/count);
    //vza_out.push(avgvza/count);
    //saa_out.push(avgsaa/count);
    //vaa_out.push(avgvaa/count);
    //totalozone_out.push(avgtotalozone/count);
    
    toa1_out.push(samples.B01);
    toa2_out.push(samples.B02);  
    toa3_out.push(samples.B03);
    toa4_out.push(samples.B04);
    toa5_out.push(samples.B05);
    toa6_out.push(samples.B06);
    toa7_out.push(samples.B07);
    toa8_out.push(samples.B08);
    toa9_out.push(samples.B09);
    toa10_out.push(samples.B10);
    toa11_out.push(samples.B11);
    toa12_out.push(samples.B12);
    toa13_out.push(samples.B13);
    toa14_out.push(samples.B14);
    toa15_out.push(samples.B15);
    toa16_out.push(samples.B16);
    toa17_out.push(samples.B17);
    toa18_out.push(samples.B18);
    toa19_out.push(samples.B19);
    toa20_out.push(samples.B20);
    toa21_out.push(samples.B21); 

    sza_out.push(samples.SZA);
    vza_out.push(samples.VZA);
    saa_out.push(samples.SAA);
    vaa_out.push(samples.VAA);
    totalozone_out.push(samples.TOTAL_COLUMN_OZONE);
  
    return {
      toa1 : toa1_out,
      toa2 : toa2_out,
      toa3 : toa3_out,
      toa4 : toa4_out,
      toa5 : toa5_out,
      toa6 : toa6_out,
      toa7 : toa7_out,
      toa8 : toa8_out,
      toa9 : toa9_out,
      toa10 : toa10_out,
      toa11 : toa11_out,
      toa12 : toa12_out,
      toa13 : toa13_out,
      toa14 : toa14_out,
      toa15 : toa15_out,
      toa16 : toa16_out,
      toa17 : toa17_out,
      toa18 : toa18_out,
      toa19 : toa19_out,
      toa20 : toa20_out,
      toa21 : toa21_out,
      saa : saa_out,
      vaa : vaa_out,
      sza : sza_out,
      vza : vza_out,
      totalozone : totalozone_out,
 
    };
}
        
function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
  outputMetadata.userData = { "tiles":  scenes.tiles }
  }

