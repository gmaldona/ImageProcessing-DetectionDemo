# Image Processing & Detection Demo

### OpenCV is required to run the following demo: https://pypi.org/project/opencv-python/

When using openCV, you can place a bounding box around a region of interest:

![Object Detection](https://github.com/gmaldona/ImageProcessing-DetectionDemo/blob/main/Demo%20Images/openCV%20Camera.png)

In the case of the final project, the object detected will be a full length body walking. We can simulate this in the demo by just drawing the bounding box that represents where a person would be detected in a frame:

![Frame 1](https://github.com/gmaldona/ImageProcessing-DetectionDemo/blob/main/Demo%20Images/Frame%201.png)

In the next frame, that detected person would walk in a direction and show up at a different (x, y, z) position:

![Frame 2](https://github.com/gmaldona/ImageProcessing-DetectionDemo/blob/main/Demo%20Images/Frame%202.png)

The computer doesn't know where each point in frame 1 translated to, all it sees are bounding boxes at different locations:

![Centroids](https://github.com/gmaldona/ImageProcessing-DetectionDemo/blob/main/Demo%20Images/Centroids.png)

We can calculate the most probable translation that each point undergoes by calculating the distance between each centroid in frame 2 and all of the centroids in frame 1 and comparing all of the areas.


All of the vector analysis and equations are with in translationPrediction.py:

```python3
def most_likely_translation(current_object: ((float, float), float), previous_objects: ([(float, float)], [float])) -> (float, float):
```

![Distance](https://github.com/gmaldona/ImageProcessing-DetectionDemo/blob/main/Demo%20Images/distance%20Between%20Centroids.png)

The method takes in two parameters: one centroid from frame 2 and all of the centroids in frame 1. The method returns a single centroid that is in frame 1 that the parameter centroid in frame 2 most like translated from: 

![Translation](https://github.com/gmaldona/ImageProcessing-DetectionDemo/blob/main/Demo%20Images/points%20Translated.png)
