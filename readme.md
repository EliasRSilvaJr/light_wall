# Light Wall

Use this project to make custom messages on a light wall, like on stranger things. 

| H | E | L | L | O |
|---|---|---|---|---|
| ![H](images/h.png) | ![E](images/e.png) | ![L](images/l.png) | ![L](images/l.png) | ![O](images/o.png) |

This project produces a video displaying the message choosed.

To generate the video, execute:
```python
python main.py
    --message=<message to be displayed>
    --path_to_images=<path to image folder>
    --save_video_at=<file path to save resulting video>
    --letter_duration=<duration of lighted letter>
    --interval_duration=<duration between letters>
```

For instance:
```python
python main.py
    --message='00heLLo0'
    --path_to_images='images/'
    --save_video_at='videos/hello.avi'
    --letter_duration=1.25
    --interval_duration=0.75
```

The program will print:
  * A message indicating the start of video writing:
  ```
  Writing video at: videos/hello.avi
  ``` 
  * A message indicating the video was successfully written:
  ```
  Video was saved!!
  ```