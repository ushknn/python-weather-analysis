import numpy as np
    
def load_sst():
    loadfile = './data/sst_OISST.npz'
    sst_dataset = np.load(loadfile)
    # sea surface temperature
    sst = sst_dataset['sst']
    
    #
    lon2 = sst_dataset['lon2']
    
    #
    lat2 = sst_dataset['lat2']
    
    # yaer
    y = sst_dataset['y']
    
    # month
    m = sst_dataset['m']

    return sst, lon2, lat2, y, m

def load_ssta():
    loadfile = './data/ssta_OISST.npz'
    ssta_dataset = np.load(loadfile)
    # sea surface temperature
    ssta = ssta_dataset['ssta']
    
    #
    lon2 = ssta_dataset['lon2']
    
    #
    lat2 = ssta_dataset['lat2']
    
    # yaer
    y = ssta_dataset['y']
    
    # month
    m = ssta_dataset['m']

    return ssta, lon2, lat2, y, m

def load_detrended_ssta():
    loadfile = './data/detrended_ssta_OISST.npz'
    ssta_dataset = np.load(loadfile)
    # sea surface temperature
    ssta = ssta_dataset['ssta']
    
    #
    lon2 = ssta_dataset['lon2']
    
    #
    lat2 = ssta_dataset['lat2']
    
    # yaer
    y = ssta_dataset['y']
    
    # month
    m = ssta_dataset['m']

    return ssta, lon2, lat2, y, m

def load_tokyo_temp():
    tokyo_temp = np.genfromtxt("data/Tokyo_temp.csv",
                              delimiter=",",
                              usecols=(0,1,2)
                             )
    y = tokyo_temp[:, 0]
    m = tokyo_temp[:, 1]
    temp = tokyo_temp[:, 2]

    return y, m, temp