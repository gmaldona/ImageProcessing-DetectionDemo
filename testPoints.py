from random import randint
import random
import cv2
import math
import translationPrediction

frameWidth, frameHeight = 1280, 720

def newFrame(objectsAdded=0):
    # (x, y) & area
    
    frame = cv2.imread('image-asset.jpeg')

    standard_x_Distance = 150  
    standard_y_Distance = 400

    currentObjects = []

    for i in range(1, objectsAdded + 1):
        
        random_x = randint(0, frameWidth - standard_x_Distance)
        random_y = randint(0, frameHeight - standard_y_Distance)
        random_multiplier = random.uniform(0.5, 1)
        random_x_distance = int(standard_x_Distance * random_multiplier)
        random_y_distance = int (standard_y_Distance * random_multiplier )
        
        
        if currentObjects != None:
            for obj in currentObjects:
                if random_x + random_x_distance > obj[0][0] and random_x + random_x_distance < obj[1][0]:
                    if random_y > obj[0][1] and random_y < obj[1][1]:
                        i = i - 1
                        continue
                    
                if random_x > obj[0][0] and random_x < obj[1][0]:
                    if random_y > obj[0][1] and random_y < obj[1][1]:
                        i = i - 1
                        continue
                
                if random_y + random_y_distance > obj[0][1] and random_y + random_y_distance < obj[1][1]:
                    if random_x + random_x_distance > obj[0][0] and random_x + random_x_distance < obj[1][0]:
                        i = i - 1
                        continue
                    
                if random_y + random_y_distance > obj[0][1] and random_y + random_y_distance < obj[1][1]:
                    if random_x > obj[0][0] and random_x < obj[1][1]:
                        i = i - 1
                        continue
        
        centroid = ( int( random_x + ( random_x_distance / 2 )) , int (random_y + ( random_y_distance / 2 )) )

        
        topLeft = (random_x, random_y)
        bottomRight = (random_x + int((standard_x_Distance * random_multiplier)), random_y + int((standard_y_Distance * random_multiplier)))
        currentObjects.append([topLeft, bottomRight])
        
        
        color = (0, 255, 0)

        frame = cv2.rectangle(frame, topLeft, bottomRight, color)
        
        frame = cv2.circle(frame, centroid, 10, (0, 255, 0), 1)        
        
    while True:
            cv2.imshow('Frame', frame)
            
            key = cv2.waitKey(1)
            if key == ord('q'):
               break
           
    return currentObjects
 
def nextFrame(previousObjects: [(int, int), (int, int)], objectsAdded=0):
    
    frame = cv2.imread('image-asset.jpeg')
    
    standard_x_Distance = 150  
    standard_y_Distance = 400
    
    currentObjects = []
    
    for obj in previousObjects:
        random_multiplier = random.uniform(0.9, 1.1)
        velocity = 100
        random_sign = random.randint(0, 1)
        if random_sign == 0 and velocity > 0:
            velocity = velocity * -1
        elif random_sign == 1 and velocity < 0:
            velocity = velocity * -1
            
        currentObjects.append([(obj[0][0] + velocity, obj[0][1]), (obj[0][0] + int (random_multiplier * ( obj[1][0] - obj[0][0] ) ) + velocity , obj[0][1] + int (random_multiplier * (obj[1][1] - obj[0][1]) )) ])
        
    for i in range(1, objectsAdded + 1):
        
        random_x = 1280 - 200
        random_y = randint(0, frameHeight - standard_y_Distance)
        random_multiplier = random.uniform(0.5, 1)
        random_x_distance = int (standard_x_Distance * random_multiplier )
        random_y_distance = int (standard_y_Distance * random_multiplier )
        
        if previousObjects != None:
            for obj in previousObjects:
                if random_x + random_x_distance > obj[0][0] and random_x + random_x_distance < obj[1][0]:
                    if random_y > obj[0][1] and random_y < obj[1][1]:
                        i = i - 1
                        continue
                    
                if random_x > obj[0][0] and random_x < obj[1][0]:
                    if random_y > obj[0][1] and random_y < obj[1][1]:
                        i = i - 1
                        continue
                
                if random_y + random_y_distance > obj[0][1] and random_y + random_y_distance < obj[1][1]:
                    if random_x + random_x_distance > obj[0][0] and random_x + random_x_distance < obj[1][0]:
                        i = i - 1
                        continue
                    
                if random_y + random_y_distance > obj[0][1] and random_y + random_y_distance < obj[1][1]:
                    if random_x > obj[0][0] and random_x < obj[1][1]:
                        i = i - 1
                        continue
        
        topLeft = (random_x, random_y)
        bottomRight = (random_x + int((standard_x_Distance * random_multiplier)), random_y + int((standard_y_Distance * random_multiplier)))
        currentObjects.append([topLeft, bottomRight])           
    
    for obj in currentObjects:
        topLeft = obj[0]
        bottomRight = obj[1]
        centroid = ( obj[0][0] + int((bottomRight[0] - topLeft[0]) / 2), obj[0][1] + int((bottomRight[1] - topLeft[1]) / 2 ))
        
        color = (153,50,204)
        
        frame = cv2.rectangle(frame, topLeft, bottomRight, color)
        
        frame = cv2.circle(frame, centroid, 10, color)   
              
    while True:
        cv2.imshow('Frame', frame)            
        key = cv2.waitKey(1)
        if key == ord('q'):
           break   
       
    return currentObjects       
        

def demo():    
    first_frame_objects = newFrame(2)
    second_frame_objects = nextFrame(first_frame_objects)

    previousCentroids = []
    previousAreas = []

    for obj in first_frame_objects:
        previousCentroids.append( ( obj[0][0] + ( ( obj[1][0] - obj[0][0]) / 2 ) , obj[0][1] + ( (obj[1][1] - obj[0][1]) / 2 ) ) )
        previousAreas.append( (obj[1][0] - obj[0][0]) * (obj[1][1] - obj[0][1]) )
        
    currentCentroids = []
    currentAreas = []

    for obj in second_frame_objects:
        currentCentroids.append( (obj[0][0] + ( ( obj[1][0] - obj[0][0] ) / 2 ), obj[0][1] + ( ( obj[1][1] - obj[0][1] ) / 2 ) ) )
        currentAreas.append( (obj[1][0] - obj[0][0]) * (obj[1][1] - obj[0][1]) )
        
    previousObjects = [previousCentroids, previousAreas]
    currentObjects = [currentCentroids, currentAreas]

    mapped_points = {}

    frame = cv2.imread('image-asset.jpeg')

    for centroid in previousCentroids:
        centroid = tuple(map(lambda x : int(x), centroid))
        frame = cv2.circle(frame, centroid, 10, (0, 255, 0), 1)
        
    for centroid in currentObjects[0]:
        centroid = tuple(map(lambda x : int(x), centroid))
        frame = cv2.circle(frame, centroid, 10, (153,50,204), 1)

    while True:
        
        cv2.imshow('Frame', frame)            
        key = cv2.waitKey(1)
        if key == ord('q'):
            break 

    tempPreviousObjects = previousObjects.copy()
    tempPreviousObjects[0] = previousObjects[0].copy()
    tempPreviousObjects[1] = previousObjects[1].copy()

    for i in range(0, len(currentObjects)):
        currentObject = (currentCentroids[i], currentAreas[i])
        currentCentroids[i] = tuple(map(lambda x : int(x), currentCentroids[i]))
        if previousObjects != None:
            mapped_point = translationPrediction.most_likely_translation(currentObject, tempPreviousObjects)
            index = tempPreviousObjects[0].index(mapped_point)
            mapped_point = tuple(map( lambda x : int(x), mapped_point ))
            mapped_points[currentCentroids[i]] = mapped_point
            tempPreviousObjects[0].pop(index)
            tempPreviousObjects[1].pop(index)
            
    for i in range(0, len(currentCentroids)):
        currentCentroids[i] = tuple(map(lambda x : int(x), currentCentroids[i]))
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = (red, green, blue)
        for j in range(0, len(previousCentroids)):
            previousCentroids[j] = tuple(map(lambda x : int(x), previousCentroids[j]))
            frame = cv2.line(frame, currentCentroids[i], previousCentroids[j], color, 1)        
            
    while True:
        
        cv2.imshow('Frame', frame)            
        key = cv2.waitKey(1)
        if key == ord('q'):
            break     

    frame = cv2.imread('image-asset.jpeg')
    
    for centroid in currentCentroids:
        color = (0, 255, 0)
        
        frame = cv2.circle(frame, centroid, 10, color, 1)
        frame = cv2.circle(frame, mapped_points.get(centroid), 10, color, 1)
        frame = cv2.arrowedLine(frame, mapped_points.get(centroid), centroid, color, 1)
        
    while True:
        
        cv2.imshow('Frame', frame)            
        key = cv2.waitKey(1)
        if key == ord('q'):
            break   
    

