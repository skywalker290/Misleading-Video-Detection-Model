# pip install pytube tqdm

from pytube import YouTube
from tqdm import tqdm
import pandas as pd
import requests

def download_video(video_url, save_path='.'):
    try:
        yt = YouTube(video_url)

        # Choose the 720p stream (modify as needed)
        # for i in yt.streams:
        #     print(i)

        video = yt.streams.filter(res='360p', progressive=True, file_extension='mp4').first()

        print(f"Downloading: {yt.title}")

        # Get the video stream as a readable stream
        video_stream = requests.get(video.url, stream=True)
        total_size = int(video_stream.headers.get('content-length', 0))

        # Use tqdm for progress bar
        with open(f"{save_path}/{yt.title}.mp4", 'wb') as file, tqdm(
                desc=yt.title,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                dynamic_ncols=True,
                ) as bar:

            for data in video_stream.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))

        print("Download complete!")

    except Exception as e:
        print(f"Error: {str(e)}")


# video_url="www.youtube.com/something/something"
# download_video(video_url)



## Downloading MVD Dataset
MVD=pd.read_csv('Datasets/MVD_DATASET.csv')
print(MVD.columns)

MVD_FAKE=MVD[MVD['LABEL']=='FAKE']
MVD_REAL=MVD[MVD['LABEL']=='ORIGINAL']

urls="https://www.youtube.com/watch?v="

for i in MVD_FAKE['video_id']:
    download_video(urls+i,'Datasets/MVD/FAKE/')







