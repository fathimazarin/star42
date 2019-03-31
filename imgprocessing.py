import cv2       
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    
    
    img = cv2.imread("minions.jpg", 1)  # importing image
  #  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    filtered = cv2.medianBlur(img,3,0)  # applying median blur
    filtered1 = cv2.subtract(img,filtered)   #subtracting to make it noise free

    
    k = np.array(np.ones((11, 11), np.float32))/121    #making a matrix for convolution with each element as 1
    
    k = np.array(([1, 0, 0,0,0,0], [0, 0, 0,0,0,0],[0, 0, 0,0,0,0],[0, 0, 0,0,0,0],[0, 0, 0,0,0,0],[0, 0, 0,0,0,-1] ), np.float32)   #changing the values of matrix, such the the convoluted image has approximately twice the variance
    
     
    output = cv2.filter2D(filtered1, -1, k)  #applying custom filter  
    
    
    plt.subplot(2, 2, 1)     
    plt.imshow(img,'gray')
    plt.title('Original Image')
    
 
    x,y=output.shape    # initializing by image size 

    square=0
    add=0
    for i in range(x):   #iterating it along every pixel 
        for j in range(y):
            add=add+int(output[i,j])     #calculating mean
            square=square + (int(output[i,j])*int(output[i,j]))   #calculating (xi)^2 for variance

    mean=add/(x*y)  # calculating mean and variance
    variance=(square/(x*y))-mean

    #print(mean,variance)   
    thresh= np.uint8(8*math.sqrt(variance))       # threshold of thresh to zero function
    ret, threshim=cv2.threshold(filtered1,thresh,255,cv2.THRESH_TOZERO)      
    plt.subplot(2, 2, 3)
    plt.imshow(threshim,'gray')
    plt.title('threshImage')
    plt.show()

    
    
    

if __name__ == "__main__":
    main()
        
