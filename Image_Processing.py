import cv2       
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    
    
    img = cv2.imread("image.jpeg",0)  # importing image
    filtered = cv2.medianBlur(img,5,0)  # applying median blur
    flattened = cv2.subtract(img,filtered)   #subtracting to make it noise free

    
    k = np.array(np.ones((11, 11), np.float32))/121    #making a matrix for convolution with each element as 1
    
    k = np.array(([1, 0, 0,0,0,0], [0, 0, 0,0,0,0],[0, 0, 0,0,0,0],[0, 0, 0,0,0,0],[0, 0, 0,0,0,0],[0, 0, 0,0,0,-1] ), np.float32)   #changing the values of matrix, such the the convoluted image has approximately twice the variance
    
     
    output = cv2.filter2D(flattened, -1, k)  #applying custom filter  
    
    
    
 
    x,y=output.shape  # initializing by image size

    square=0
    add=0
    for i in range(x):   #iterating it along every pixel 
        for j in range(y):
            add=add+int(output[i,j])     #calculating mean
            square=square + (int(output[i,j])*int(output[i,j]))   #calculating (xi)^2 for variance

    mean=add/(x*y)  # calculating mean and variance
    variance=(square/(x*y))-mean
    variance = variance/2
    sigma =np.uint8(math.sqrt(variance))

    #print(mean,variance)   
    thresh= np.uint8(8*math.sqrt(variance))       
    initial_list = []
    x1,y1 =img.shape
    for i in range(x1):
        for j in range(y1):
            if flattened[i,j] > thresh :
                initial_list.append([i,j])

    maxi =np.uint8(0)
    x_max,y_max =0,0
    for i in range(x1):
        for j in range(y1):
            if flattened[i,j] >= maxi :
                x_max,y_max = i,j
                maxi = flattened[i,j] 
    

    new_list = []
    new_thresh = maxi - (3*sigma)
    for z in initial_list :
        x,y = z
        if new_thresh <=  flattened[x,y]  or (0.99)*maxi <= flattened[x,y]:
            new_list.append([x,y])

    centroids = []
    dummy = flattened
    for x in range(x1):
        for y in range(y1):
            z = [x,y]
            if z in new_list:
                dummy[x,y] = np.uint8(255)
            else :
                dummy[x,y] = np.uint8(0)
    edges = cv2.Canny(dummy,100,200)
    contours , hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for t in contours:
        M = cv2.moments(t)
        if M['m00'] !=0:
            cx = int(M['m01']/M['m00'])
            cy = int(M['m10']/M['m00'])
        else :
            cx,cy = 0,0
            
        if cx!=0 and cy!=0 :
            centroids.append([cx,cy])

    print(centroids)
        

        

if __name__ == "__main__":
    main()
        
