# Video-To-Image
This is a tool to save images from certain video using OpenCV.

## How To Use
You can use the code like this:
```
python3 main.py \
  --video_path='<path to video>' \
  --image_format='<output image extension>' \
  --frame_interval='<interval between saves>'
```
For example:
```
python3 main.py \
  --video_path='video.mp4' \
  --image_format='png' \
  --frame_interval=60
```

## Result
![alt text](https://github.com/jefflgaol/Video-To-Image/blob/master/test.gif)
