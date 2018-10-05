import requests
import h5py
import numpy as np
import zipfile
from tqdm import tqdm
import math

def file_download():
    print("LOADING DATASETS AND MODEL WEIGHTS")

#    title_abstract_2clusters = "title_abstract_2clusters.h5"
#    url = "https://zenodo.org/record/1442704/files/title_abstract_2clusters.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(title_abstract_2clusters, 'wb').write(r.content)

#   title_abstract_2clusters_weights = "title_abstract_2clusters_weights.h5"
#    url = "https://zenodo.org/record/1442704/files/title_abstract_2clusters_weights.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(title_abstract_2clusters_weights, 'wb').write(r.content)

    title_abstract_5class = "title_abstract_5class.h5"
    url = "https://zenodo.org/record/1442704/files/title_abstract_5class.h5"
    r = requests.get(url, allow_redirects=True)
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0 
    with open(title_abstract_5class, 'wb') as f:
    for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
        wrote = wrote  + len(data)
        f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong")  

    title_abstract_5class_weights = "title_abstract_5class_weights.h5"
    url = "https://zenodo.org/record/1442704/files/title_abstract_5class_weights.h5"
    r = requests.get(url, allow_redirects=True)
    open(title_abstract_5class_weights, 'wb').write(r.content)

    print("BASELINE DATA AND WEIGHTS LOADED") 

#   captions_2clusters = "captions_2clusters.h5"
#    url = "https://zenodo.org/record/1442704/files/captions_2clusters.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(captions_2clusters, 'wb').write(r.content)

#    captions_2clusters_weights = "captions_2clusters_weights.h5"
#    url = "https://zenodo.org/record/1442704/files/captions_2clusters_weights.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(captions_2clusters_weights, 'wb').write(r.content)

    captions_5class = "captions_5class.h5"
    url = "https://zenodo.org/record/1442704/files/captions_5class.h5"
    r = requests.get(url, allow_redirects=True)
    open(captions_5class, 'wb').write(r.content)

    captions_5class_weights = "captions_5class_weights.h5"
    url = "https://zenodo.org/record/1442704/files/captions_5class_weights.h5"
    r = requests.get(url, allow_redirects=True)
    open(captions_5class_weights, 'wb').write(r.content)

    print("EXPERIMENT #1 LOADED") 

#    figures_2clusters = "figures_2clusters.h5"
#    url = "https://zenodo.org/record/1442704/files/figures_2clusters.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(figures_2clusters, 'wb').write(r.content)

#    figures_2clusters_weights = "figures_2clusters_weights.h5"
#    url = "https://zenodo.org/record/1442704/files/figures_2clusters_weights.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(figures_2clusters_weights, 'wb').write(r.content)

    figures_5class = "figures_5class.h5"
    url = "https://zenodo.org/record/1442704/files/figures_5class.h5"
    r = requests.get(url, allow_redirects=True)
    open(figures_5class, 'wb').write(r.content)

    figures_5class_weights = "figures_5class_weights.h5"
    url = "https://zenodo.org/record/1442704/files/figures_5class_weights.h5"
    r = requests.get(url, allow_redirects=True)
    open(figures_5class_weights, 'wb').write(r.content)

    print("EXPERIMENT #2 LOADED") 

    cross = "cross.h5"
    url = "https://zenodo.org/record/1442704/files/cross.h5"
    r = requests.get(url, allow_redirects=True)
    open(cross, 'wb').write(r.content)

    cross_weights = "cross_weights.h5"
    url = "https://zenodo.org/record/1442704/files/cross_weights.h5"
    r = requests.get(url, allow_redirects=True)
    open(cross_weights, 'wb').write(r.content)

    print("EXPERIMENT #3 LOADED") 

#    captions_2clusters_cross = "captions_2clusters_cross.h5"
#    url = "https://zenodo.org/record/1442704/files/captions_2clusters_cross.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(captions_2clusters_cross, 'wb').write(r.content)
    
#    captions_2clusters_cross_weights = "captions_2clusters_cross_weights.h5"
#    url = "https://zenodo.org/record/1442704/files/captions_2clusters_cross_weights.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(captions_2clusters_cross_weights, 'wb').write(r.content)

    captions_5class_cross = "captions_5class_cross.h5"
    url = "https://zenodo.org/record/1442704/files/captions_5class_cross.h5"
    r = requests.get(url, allow_redirects=True)
    open(captions_5class_cross, 'wb').write(r.content)
    
    captions_5class_cross_weights = "captions_5class_cross_weights.h5"
    url = "https://zenodo.org/record/1442704/files/captions_5class_cross_weights.h5"
    r = requests.get(url, allow_redirects=True)
    open(captions_5class_cross_weights, 'wb').write(r.content)
	

#    figures_2clusters_cross = "figures_2clusters_cross.h5"
#    url = "https://zenodo.org/record/1442704/files/figures_2clusters_cross.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(figures_2clusters_cross, 'wb').write(r.content)
    
#    figures_2clusters_cross_weights = "figures_2clusters_cross_weights.h5"
#    url = "https://zenodo.org/record/1442704/files/figures_2clusters_cross_weights.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(figures_2clusters_cross_weights, 'wb').write(r.content)

    figures_5class_cross = "figures_5class_cross.h5"
    url = "https://zenodo.org/record/1442704/files/figures_5class_cross.h5"
    r = requests.get(url, allow_redirects=True)
    open(figures_5class_cross, 'wb').write(r.content)
    
    figures_5class_cross_weights = "figures_5class_cross_weights.h5"
    url = "https://zenodo.org/record/1442704/files/figures_5class_cross_weights.h5"
    r = requests.get(url, allow_redirects=True)
    open(figures_5class_cross_weights, 'wb').write(r.content)
    
    print("EXPERIMENT #4 LOADED")
	
#    quality2clusters = "quality2clusters.h5"
#    url = "https://zenodo.org/record/1442704/files/quality2clusters.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(quality2clusters, 'wb').write(r.content)
	
    quality5class = "quality5class.h5"
    url = "https://zenodo.org/record/1442704/files/quality5class.h5"
    r = requests.get(url, allow_redirects=True)
    open(quality5class, 'wb').write(r.content)
    
#    qualityMix2clusters = "qualityMix2clusters.h5"
#    url = "https://zenodo.org/record/1442704/files/qualityMix2clusters.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(qualityMix2clusters, 'wb').write(r.content)
	
    qualityMix5class = "qualityMix5class.h5"
    url = "https://zenodo.org/record/1442704/files/qualityMix5class.h5"
    r = requests.get(url, allow_redirects=True)
    open(qualityMix5class, 'wb').write(r.content)
	
#    qualityUni2clusters = "qualityUni2clusters.h5"
#    url = "https://zenodo.org/record/1442704/files/qualityUni2clusters.h5"
#    r = requests.get(url, allow_redirects=True)
#    open(qualityUni2clusters, 'wb').write(r.content)
	
    qualityUni5class = "qualityUni5class.h5"
    url = "https://zenodo.org/record/1442704/files/qualityUni5class.h5"
    r = requests.get(url, allow_redirects=True)
    open(qualityUni5class, 'wb').write(r.content)
    imageshq = "5class.zip"
    url = "https://zenodo.org/record/1442708/files/5class.zip"
    r = requests.get(url, allow_redirects=True)
    open(imageshq, 'wb').write(r.content)
    zip_ref = zipfile.ZipFile(imageshq, 'r')
    zip_ref.extractall(".")
    zip_ref.close()
		
    print("EXPERIMENT #5 LOADED")

def gen_text (h5path, indices,batchSize, shuffle): 
  db = h5py.File(h5path, "r")
  while True:
    if shuffle:
        np.random.shuffle(indices)
    for i in range(0, len(indices), batchSize):
        batch_indices = indices[i:i+batchSize]
        batch_indices.sort()
        
        bx = db["text"][batch_indices,:]
        by = db["labels"][batch_indices,:]

        yield (bx, by)

def gen_images (h5path, indices,batchSize, shuffle):
  db = h5py.File(h5path, "r")
  while True:
    if shuffle:
        np.random.shuffle(indices)
    for i in range(0, len(indices), batchSize):
        batch_indices = indices[i:i+batchSize]
        batch_indices.sort()
        
        bx = db["images"][batch_indices,:,:,:]
        by = db["labels"][batch_indices,:]

        yield (bx, by)

def gen_cross (h5path, indices,batchSize,shuffle):
  db = h5py.File(h5path, "r")
  while True:
    if shuffle:
        np.random.shuffle(indices)
    for i in range(0, len(indices), batchSize):
        batch_indices = indices[i:i+batchSize]
        batch_indices.sort()
        
        bx1 = db["text"][batch_indices,:]
        bx2 = db["images"][batch_indices,:,:,:]
        by = db["labels"][batch_indices,:]

        yield ([bx1, bx2], by)

