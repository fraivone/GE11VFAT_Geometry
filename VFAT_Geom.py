import ROOT
import numpy as np

## Region chamber layer to chamber name
def ReChLa2chamberName(re,ch,la):
    endcap = "M" if re == -1 else "P"
    size = "S" if ch%2 == 1 else "L"
    chID = 'GE11-'+endcap+'-%02d' % ch +"L"+str(la)+"-"+size
    return chID

def chamberName2ReChLa(chamberName):
    ## Accepts as input either 
    ## GE11-M-03L1 or GE11-M-03L1-S
    if len(chamberName)==13:
        chamberName = chamberName[:11]
    re = -1 if "M" in chamberName else 1
    ch = int( chamberName.split("-")[-1][:2] )
    la = int( chamberName.split("-")[-1][-1] )

    return [re,ch,la]

## GEOMETRY DEFINITION
def GE11VFATGeometry():
    VFATGeometryDict = {"Long":dict((VFATN,{}) for VFATN in range(0,24)),"Short":dict((VFATN,{}) for VFATN in range(0,24))}

    VFATGeometryDict['Short'][0]['x'] = np.asarray([-3.83938562003834,-4.14080692494689,-12.4513908518566,-11.5450181214881],dtype=float)
    VFATGeometryDict['Short'][0]['y'] = np.asarray([0,10.206,10.206,0],dtype=float)
    VFATGeometryDict['Short'][1]['x'] = np.asarray([-4.14080692494689,-4.44222822985544,-13.3577635822252,-12.4513908518566],dtype=float)
    VFATGeometryDict['Short'][1]['y'] = np.asarray([10.206,20.412,20.412,10.206],dtype=float)
    VFATGeometryDict['Short'][2]['x'] = np.asarray([-4.44222822985544,-4.79536310569235,-14.4196388259069,-13.3577635822252],dtype=float)
    VFATGeometryDict['Short'][2]['y'] = np.asarray([20.412,32.369,32.369,20.412],dtype=float)
    VFATGeometryDict['Short'][3]['x'] = np.asarray([-4.79536310569235,-5.14849798152926,-15.4815140695887,-14.4196388259069],dtype=float)
    VFATGeometryDict['Short'][3]['y'] = np.asarray([32.369,44.326,44.326,32.369],dtype=float)
    VFATGeometryDict['Short'][4]['x'] = np.asarray([-5.14849798152926,-5.56365370199756,-16.7298857598484,-15.4815140695887],dtype=float)
    VFATGeometryDict['Short'][4]['y'] = np.asarray([44.326,58.383,58.383,44.326],dtype=float)
    VFATGeometryDict['Short'][5]['x'] = np.asarray([-5.56365370199756,-5.97880942246586,-17.9782574501081,-16.7298857598484],dtype=float)
    VFATGeometryDict['Short'][5]['y'] = np.asarray([58.383,72.44,72.44,58.383],dtype=float)
    VFATGeometryDict['Short'][6]['x'] = np.asarray([-5.97880942246586,-6.47069378786385,-19.4573518871341,-17.9782574501081],dtype=float)
    VFATGeometryDict['Short'][6]['y'] = np.asarray([72.4399999999999,89.0949999999999,89.0949999999999,72.4399999999999],dtype=float)
    VFATGeometryDict['Short'][7]['x'] = np.asarray([-6.47069378786385,-6.96257815326184,-20.9364463241602,-19.4573518871341],dtype=float)
    VFATGeometryDict['Short'][7]['y'] = np.asarray([89.0949999999999,105.75,105.75,89.0949999999999],dtype=float)
    VFATGeometryDict['Short'][8]['x'] = np.asarray([-3.83938562003834,-4.14080692494689,4.14080692494689,3.83938562003834],dtype=float)
    VFATGeometryDict['Short'][8]['y'] = np.asarray([0,10.206,10.206,0],dtype=float)
    VFATGeometryDict['Short'][9]['x'] = np.asarray([-4.14080692494689,-4.44222822985544,4.44222822985544,4.14080692494689],dtype=float)
    VFATGeometryDict['Short'][9]['y'] = np.asarray([10.206,20.412,20.412,10.206],dtype=float)
    VFATGeometryDict['Short'][10]['x'] = np.asarray([-4.44222822985544,-4.79536310569235,4.79536310569235,4.44222822985544],dtype=float)
    VFATGeometryDict['Short'][10]['y'] = np.asarray([20.412,32.369,32.369,20.412],dtype=float)
    VFATGeometryDict['Short'][11]['x'] = np.asarray([-4.79536310569235,-5.14849798152926,5.14849798152926,4.79536310569235],dtype=float)
    VFATGeometryDict['Short'][11]['y'] = np.asarray([32.369,44.326,44.326,32.369],dtype=float)
    VFATGeometryDict['Short'][12]['x'] = np.asarray([-5.14849798152926,-5.56365370199756,5.56365370199756,5.14849798152926],dtype=float)
    VFATGeometryDict['Short'][12]['y'] = np.asarray([44.326,58.383,58.383,44.326],dtype=float)
    VFATGeometryDict['Short'][13]['x'] = np.asarray([-5.56365370199756,-5.97880942246586,5.97880942246586,5.56365370199756],dtype=float)
    VFATGeometryDict['Short'][13]['y'] = np.asarray([58.383,72.44,72.44,58.383],dtype=float)
    VFATGeometryDict['Short'][14]['x'] = np.asarray([-5.97880942246586,-6.47069378786385,6.47069378786385,5.97880942246586],dtype=float)
    VFATGeometryDict['Short'][14]['y'] = np.asarray([72.4399999999999,89.0949999999999,89.0949999999999,72.4399999999999],dtype=float)
    VFATGeometryDict['Short'][15]['x'] = np.asarray([-6.47069378786385,-6.96257815326184,6.96257815326184,6.47069378786385],dtype=float)
    VFATGeometryDict['Short'][15]['y'] = np.asarray([89.0949999999999,105.75,105.75,89.0949999999999],dtype=float)
    VFATGeometryDict['Short'][16]['x'] = np.asarray([3.83938562003834,4.14080692494689,12.4513908518566,11.5450181214881],dtype=float)
    VFATGeometryDict['Short'][16]['y'] = np.asarray([0,10.206,10.206,0],dtype=float)
    VFATGeometryDict['Short'][17]['x'] = np.asarray([4.14080692494689,4.44222822985544,13.3577635822252,12.4513908518566],dtype=float)
    VFATGeometryDict['Short'][17]['y'] = np.asarray([10.206,20.412,20.412,10.206],dtype=float)
    VFATGeometryDict['Short'][18]['x'] = np.asarray([4.44222822985544,4.79536310569235,14.4196388259069,13.3577635822252],dtype=float)
    VFATGeometryDict['Short'][18]['y'] = np.asarray([20.412,32.369,32.369,20.412],dtype=float)
    VFATGeometryDict['Short'][19]['x'] = np.asarray([4.79536310569235,5.14849798152926,15.4815140695887,14.4196388259069],dtype=float)
    VFATGeometryDict['Short'][19]['y'] = np.asarray([32.369,44.326,44.326,32.369],dtype=float)
    VFATGeometryDict['Short'][20]['x'] = np.asarray([5.14849798152926,5.56365370199756,16.7298857598484,15.4815140695887],dtype=float)
    VFATGeometryDict['Short'][20]['y'] = np.asarray([44.326,58.383,58.383,44.326],dtype=float)
    VFATGeometryDict['Short'][21]['x'] = np.asarray([5.56365370199756,5.97880942246586,17.9782574501081,16.7298857598484],dtype=float)
    VFATGeometryDict['Short'][21]['y'] = np.asarray([58.383,72.44,72.44,58.383],dtype=float)
    VFATGeometryDict['Short'][22]['x'] = np.asarray([5.97880942246586,6.47069378786385,19.4573518871341,17.9782574501081],dtype=float)
    VFATGeometryDict['Short'][22]['y'] = np.asarray([72.4399999999999,89.0949999999999,89.0949999999999,72.4399999999999],dtype=float)
    VFATGeometryDict['Short'][23]['x'] = np.asarray([6.47069378786385,6.96257815326184,20.9364463241602,19.4573518871341],dtype=float)
    VFATGeometryDict['Short'][23]['y'] = np.asarray([89.0949999999999,105.75,105.75,89.0949999999999],dtype=float)
    VFATGeometryDict['Long'][0]['x'] = np.asarray([-3.83938562003834,-4.17332356777506,-12.5491682745625,-11.5450181214881],dtype=float)
    VFATGeometryDict['Long'][0]['y'] = np.asarray([0,11.307,11.307,0],dtype=float)
    VFATGeometryDict['Long'][1]['x'] = np.asarray([-4.17332356777506,-4.50726151551178,-13.5533184276368,-12.5491682745625],dtype=float)
    VFATGeometryDict['Long'][1]['y'] = np.asarray([11.307,22.614,22.614,11.307],dtype=float)
    VFATGeometryDict['Long'][2]['x'] = np.asarray([-4.50726151551178,-4.90466746092129,-14.7483166110425,-13.5533184276368],dtype=float)
    VFATGeometryDict['Long'][2]['y'] = np.asarray([22.614,36.07,36.07,22.614],dtype=float)
    VFATGeometryDict['Long'][3]['x'] = np.asarray([-4.90466746092129,-5.30207340633079,-15.9433147944483,-14.7483166110425],dtype=float)
    VFATGeometryDict['Long'][3]['y'] = np.asarray([36.07,49.526,49.526,36.07],dtype=float)
    VFATGeometryDict['Long'][4]['x'] = np.asarray([-5.30207340633079,-5.77777328465355,-17.3737425397006,-15.9433147944483],dtype=float)
    VFATGeometryDict['Long'][4]['y'] = np.asarray([49.526,65.633,65.633,49.526],dtype=float)
    VFATGeometryDict['Long'][5]['x'] = np.asarray([-5.77777328465355,-6.2534731629763,-18.804170284953,-17.3737425397006],dtype=float)
    VFATGeometryDict['Long'][5]['y'] = np.asarray([65.633,81.74,81.74,65.633],dtype=float)
    VFATGeometryDict['Long'][6]['x'] = np.asarray([-6.2534731629763,-6.82657530110586,-20.5274862591644,-18.804170284953],dtype=float)
    VFATGeometryDict['Long'][6]['y'] = np.asarray([81.74,101.145,101.145,81.74],dtype=float)
    VFATGeometryDict['Long'][7]['x'] = np.asarray([-6.82657530110586,-7.39967743923543,-22.2508022333757,-20.5274862591644],dtype=float)
    VFATGeometryDict['Long'][7]['y'] = np.asarray([101.145,120.55,120.55,101.145],dtype=float)
    VFATGeometryDict['Long'][8]['x'] = np.asarray([-3.83938562003834,-4.17332356777506,4.17332356777506,3.83938562003834],dtype=float)
    VFATGeometryDict['Long'][8]['y'] = np.asarray([0,11.307,11.307,0],dtype=float)
    VFATGeometryDict['Long'][9]['x'] = np.asarray([-4.17332356777506,-4.50726151551178,4.50726151551178,4.17332356777506],dtype=float)
    VFATGeometryDict['Long'][9]['y'] = np.asarray([11.307,22.614,22.614,11.307],dtype=float)
    VFATGeometryDict['Long'][10]['x'] = np.asarray([-4.50726151551178,-4.90466746092129,4.90466746092129,4.50726151551178],dtype=float)
    VFATGeometryDict['Long'][10]['y'] = np.asarray([22.614,36.07,36.07,22.614],dtype=float)
    VFATGeometryDict['Long'][11]['x'] = np.asarray([-4.90466746092129,-5.30207340633079,5.30207340633079,4.90466746092129],dtype=float)
    VFATGeometryDict['Long'][11]['y'] = np.asarray([36.07,49.526,49.526,36.07],dtype=float)
    VFATGeometryDict['Long'][12]['x'] = np.asarray([-5.30207340633079,-5.77777328465355,5.77777328465355,5.30207340633079],dtype=float)
    VFATGeometryDict['Long'][12]['y'] = np.asarray([49.526,65.633,65.633,49.526],dtype=float)
    VFATGeometryDict['Long'][13]['x'] = np.asarray([-5.77777328465355,-6.2534731629763,6.2534731629763,5.77777328465355],dtype=float)
    VFATGeometryDict['Long'][13]['y'] = np.asarray([65.633,81.74,81.74,65.633],dtype=float)
    VFATGeometryDict['Long'][14]['x'] = np.asarray([-6.2534731629763,-6.82657530110586,6.82657530110586,6.2534731629763],dtype=float)
    VFATGeometryDict['Long'][14]['y'] = np.asarray([81.74,101.145,101.145,81.74],dtype=float)
    VFATGeometryDict['Long'][15]['x'] = np.asarray([-6.82657530110586,-7.39967743923543,7.39967743923543,6.82657530110586],dtype=float)
    VFATGeometryDict['Long'][15]['y'] = np.asarray([101.145,120.55,120.55,101.145],dtype=float)
    VFATGeometryDict['Long'][16]['x'] = np.asarray([3.83938562003834,4.17332356777506,12.5491682745625,11.5450181214881],dtype=float)
    VFATGeometryDict['Long'][16]['y'] = np.asarray([0,11.307,11.307,0],dtype=float)
    VFATGeometryDict['Long'][17]['x'] = np.asarray([4.17332356777506,4.50726151551178,13.5533184276368,12.5491682745625],dtype=float)
    VFATGeometryDict['Long'][17]['y'] = np.asarray([11.307,22.614,22.614,11.307],dtype=float)
    VFATGeometryDict['Long'][18]['x'] = np.asarray([4.50726151551178,4.90466746092129,14.7483166110425,13.5533184276368],dtype=float)
    VFATGeometryDict['Long'][18]['y'] = np.asarray([22.614,36.07,36.07,22.614],dtype=float)
    VFATGeometryDict['Long'][19]['x'] = np.asarray([4.90466746092129,5.30207340633079,15.9433147944483,14.7483166110425],dtype=float)
    VFATGeometryDict['Long'][19]['y'] = np.asarray([36.07,49.526,49.526,36.07],dtype=float)
    VFATGeometryDict['Long'][20]['x'] = np.asarray([5.30207340633079,5.77777328465355,17.3737425397006,15.9433147944483],dtype=float)
    VFATGeometryDict['Long'][20]['y'] = np.asarray([49.526,65.633,65.633,49.526],dtype=float)
    VFATGeometryDict['Long'][21]['x'] = np.asarray([5.77777328465355,6.2534731629763,18.804170284953,17.3737425397006],dtype=float)
    VFATGeometryDict['Long'][21]['y'] = np.asarray([65.633,81.74,81.74,65.633],dtype=float)
    VFATGeometryDict['Long'][22]['x'] = np.asarray([6.2534731629763,6.82657530110586,20.5274862591644,18.804170284953],dtype=float)
    VFATGeometryDict['Long'][22]['y'] = np.asarray([81.74,101.145,101.145,81.74],dtype=float)
    VFATGeometryDict['Long'][23]['x'] = np.asarray([6.82657530110586,7.39967743923543,22.2508022333757,20.5274862591644],dtype=float)
    VFATGeometryDict['Long'][23]['y'] = np.asarray([101.145,120.55,120.55,101.145],dtype=float)

    ## Additional polygon to standardize Axis ranges
    shape_x = np.asarray([-120.55/2,-120.55/2,120.55/2,120.55/2],dtype=float)
    shape_y = np.asarray([125.,125.01,125.01,125.],dtype=float)
    ## END OF GEOMETRY DEFINITION
    return VFATGeometryDict,shape_x,shape_y


def PlotGE11VFATWheel(target_wheel,dict_content): ## target wheels "ML1","ML2","PL1","PL2"
    h2p = ROOT.TH2Poly()
    VFATGeometryDict,shape_x,shape_y = GE11VFATGeometry()
    
    for chamber_number in range(1,37):
        chamberSize = "Short" if chamber_number%2 == 1 else "Long"
        region = 1 if target_wheel[0]=="P" else -1
        chamber_ID = ReChLa2chamberName(region,chamber_number,target_wheel[-1])           
        angle_deg = -90 + (chamber_number - 1)*10## degrees
        angle_rad = np.radians(angle_deg)
        for VFATN in range(24):
            original_x = VFATGeometryDict[chamberSize][VFATN]['x']
            original_y = VFATGeometryDict[chamberSize][VFATN]['y']
            ## fix needed to respect GE11 installation, long SCs have Drift facing the Interaction Point. Short SCs have ReadOut Board facing the IP
            ## Applying reflection along y axis
            if (region == 1 and chamber_number % 2 == 0) or (region == -1 and chamber_number % 2 == 1):
                original_x = -original_x
            translated_x = original_x
            translated_y = original_y + 130 ## GE11 ~ min R = 130 cm                
            rotated_and_translated_x = np.asarray([ translated_x[i]*np.cos(angle_rad) - translated_y[i]*np.sin(angle_rad) for i in range(len(translated_x)) ],dtype=float)
            rotated_and_translated_y = np.asarray([ translated_x[i]*np.sin(angle_rad) + translated_y[i]*np.cos(angle_rad) for i in range(len(translated_x)) ],dtype=float)
            
            selected_bin = h2p.AddBin(4,rotated_and_translated_x,rotated_and_translated_y)
            h2p.SetBinContent(selected_bin,dict_content[chamber_ID][VFATN])
            h2p.SetMarkerSize(.3) ## Reduces the text size when drawing the option "COLZ TEXT"
            h2p.GetXaxis().SetTitle("Glb x (cm)")
            h2p.GetYaxis().SetTitle("Glb y (cm)")
    
    return h2p

def PlotGE11ChamberVFAT(chamber_ID,dict_content): 
    h2p = ROOT.TH2Poly()
    VFATGeometryDict,shape_x,shape_y = GE11VFATGeometry()

    re_ch_la_list = chamberName2ReChLa(chamber_ID)
    re = re_ch_la_list[0]
    ch = re_ch_la_list[1]
    la = re_ch_la_list[2]
    chamberSize = "Short" if ch%2 == 1 else "Long"
    endcapTag = EndcapLayer2label(re,la)
    for VFATN in range(24):
        selected_bin = h2p.AddBin(4,VFATGeometryDict[chamberSize][VFATN]['x'],VFATGeometryDict[chamberSize][VFATN]['y'])
            
        VFAT_den = EfficiencyDictVFAT[endcapTag][chamber_ID][VFATN]['den'] 
        VFAT_num = EfficiencyDictVFAT[endcapTag][chamber_ID][VFATN]['num'] 
            
        h2p.SetBinContent(selected_bin,dict_content[chamber_ID][VFATN])

    ## respect proportions
    h2p.AddBin(4,shape_x,shape_y)
    h2p.GetXaxis().SetTitle("Loc x (cm)")
    h2p.GetYaxis().SetTitle("Loc y (cm)")


    return h2p

def styleVFAT_Plot(h2p,Name):
    h2p.SetMinimum(0)
    h2p.SetTitle(Name)
    h2p.SetName(Name)
    h2p.GetYaxis().SetTickLength(0.005)
    h2p.GetYaxis().SetTitleOffset(1.3)
    h2p.GetXaxis().SetTickLength(0.005)
    h2p.GetYaxis().SetLabelSize(0.03)
    h2p.GetXaxis().SetLabelSize(0.03)
    h2p.SetStats(False)
    return h2p


if __name__ == '__main__':
    ChamberVFAT_Content = {}
    canvas = ROOT.TCanvas("c1","c1",900,900)

    ## Filling the data
    for re,ly in [(1,1),(1,2),(-1,1),(-1,2)]:
        for ch in range(1,37):
            VFATs = dict.fromkeys(range(24),0)
            chamber_ID = ReChLa2chamberName(re,ch,ly)

            VFATs[21] = 13
            ChamberVFAT_Content[chamber_ID] = VFATs
    
    ## Plotting the data
    h2p = PlotGE11VFATWheel("ML1",ChamberVFAT_Content)
    h2p = styleVFAT_Plot(h2p,"ML1")
    h2p.Draw("COLZ TEXT")
    canvas.Modified()
    canvas.Update()
    raw_input()