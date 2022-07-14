import subprocess
import pandas as pd
import tqdm as tqdm


openimage_o_image_list = 'datalists/openimage_o.txt'
with open(openimage_o_image_list, 'r') as f:
    openimage_o_image_list = f.read()
openimage_o_image_list = openimage_o_image_list.splitlines()

df = pd.read_csv('data/openimage_o/test/images.csv')
download_script = []
for image in tqdm.tqdm(openimage_o_image_list):
    image_name = image[:-len('.jpg')]
    index = df[df['ImageID'] == image_name].OriginalURL.index.item()
    image_url = df[df['ImageID'] == image_name].OriginalURL[index]
    download_script.append(f"wget {image_url}")

cd /home/amir/research/datasets/OpenImage-O/images_2017_11/2017_11/test/images
failed_to_download = []
for url_to_download, imagename in tqdm.tqdm(
        zip(download_script, openimage_o_image_list)):
    try:
        subprocess.run(url_to_download, shell=True, check=True)
    except:
        failed_to_download.append((url_to_download, imagename))

