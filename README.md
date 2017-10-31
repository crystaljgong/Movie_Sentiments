# Movie_Sentiments
fall 2017 cv project movie sentiments (update this later)

### To get the data
The data are not included in this repo for size reasons.
To generate training and valid data, clone the following github: https://github.com/Microsoft/FERPlus and follow instructions under "FER+ layout for Training".
1. Download the dataset from the kaggle website (https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data), which gives you the fer2013 folder containing fer2013.csv.
2. Run generate_training_data.py in `FERplus/src/` like so:
 
```python generate_training_data.py -d <dataset base folder> -fer <fer2013.csv path> -ferplus <fer2013new.csv path>```

This should produce a folder called `data` containing FER2013Test, Train, and Valid, with black and white images of faces inside each.
Next steps: Figure out how to correspond labels with faces, since the csv files do not show a 1 or 0 "yes or no", but rather 1-4 top possible emotions for each image.

### To get the VGG-Face model
This also can't be included in the github due to size reasons.
Download the Torch version of the model from here: http://www.robots.ox.ac.uk/~vgg/software/vgg_face/

The convert_torch_to_pytorch script is from here: https://github.com/clcarwin/convert_torch_to_pytorch. Use it to convert the .t7 model into  .py, .pyc and .pth files with ```python convert_torch.py -m vgg16.t7``

### The jupyter notebook
Contains preliminary code for finetuning VGG-Face on FER2013. We are currently encountering a roadblock in formatting the data to use it for training.

### Frames from videos
`./all-data/vids/imgs/` contains frames from several Youtube videos using VLC on command line, with the following command:

```vlc.exe "pathtovideo" --video-filter=scene --vout=dummy --start-time=300 --stop-time=600 --scene-ratio=250 --scene-path=”pathtosaveimages” vlc://quit```

Instructions from this page: https://www.raymond.cc/blog/extract-video-frames-to-images-using-vlc-media-player/

Again, the videos themselves are too big to be included in this github.