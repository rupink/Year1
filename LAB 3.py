def rotate_90_degrees(image_array, direction = 1):
    '''
    rotate_90_degrees([[1, 1, 0],[0, 0, 0],[0, 0, 1]], direction = 1)
    [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
    
    rotate_90_degrees([[1, 1, 0],[0, 0, 0],[0, 0, 1]], direction = -1)
    [[0, 0, 1], [0, 0, 0], [1, 1, 0]]
    
    (list) -> list
    
    Takes image and rotates about 90 degrees, counter or clockwise
    
    '''
    output_array=[]
    side=[]

    if direction==(1):
        for i in range(len(image_array)):
            for j in reversed(range(len(image_array))):
                side.append(image_array[j][i])
            output_array.append(side)
            print (side)
            side=[]

    elif direction==(-1):
        for j in reversed(range(len(image_array))):
            for i in range(len(image_array)):
                side.append(image_array[j][i])
                
            output_array.append(side)
            side=[]

    return output_array

def flip_image(image_array, axis = 0):
    '''
    flip_image([[1, 1, 0],[0, 0, 0],[0, 0, 1]], axis = 0)
    [[0, 1, 1], [0, 0, 0], [1, 0, 0]]
    
    flip_image([[1, 1, 0],[0, 0, 0],[0, 0, 1]], axis = -1)
    [[1, 0, 0], [0, 0, 0], [0, 1, 1]]
    
    (list) -> list
    
    Reflects the image across the x,y or x-y axis

    '''
    side=[]
    output_array=[]
    
    if axis==(0):
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                side.append(image_array[i][-(1+j)])
                
            output_array.append(side)
            side=[]

    elif axis==(1):
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                side.append(image_array[-(1+i)][j])
                
            output_array.append(side)
            side=[]
            
    elif axis==(-1):
        for i in range(len(image_array)):
            for j in range(len(image_array)):
                side.append(image_array[-(1+i)][-(1+j)])
                
            output_array.append(side)
            side=[]
           
    return output_array

def crop(image_array, direction, n_pixels):
    '''
    crop([[1, 1, 0],[0, 0, 0],[0, 0, 1]], 'left', 1)
    [[1, 0], [0, 0], [0, 1]]
    
    crop([[1, 1, 0],[0, 0, 0],[0, 0, 1]], 'right', 1)
    [[1, 1], [0, 0], [0, 0]]
    
    (list) -> list
    
    Crops the image by a certain amount of pixel by a given direction
    
    '''
    side=[]
    output_array=[]

    if direction == ('down'):
        for i in range (len(image_array)-n_pixels):
            for j in range(len(image_array)):
                side.append(image_array[i][j])
                
            output_array.append(side)
            side=[]

    elif direction == ('up'):
        for i in range(n_pixels,len(image_array)):
            for j in range(len(image_array)):
                side.append(image_array[i][j])
                
            output_array.append(side)
            side=[]
            
    elif direction == ('right'):
        for i in range(len(image_array)):
            for j in range(len(image_array)-n_pixels):
                side.append(image_array[i][j])
                
            output_array.append(side)
            side=[]
               
    elif direction == ('left'):
        for i in range(len(image_array)):
            for j in range(n_pixels,len(image_array)):
                side.append(image_array[i][j])
                
            output_array.append(side)
            side=[]

    return output_array

def rgb_to_grayscale(rgb_image_array):
    '''
    (list) -> list
    
    Makes the pixels convert to their greyscale values
    
    '''
    side=[]
    pix=0
    output_array=[]
    
    for i in range(len(rgb_image_array)):
        for j in range(len(rgb_image_array)):
            pix=(rgb_image_array[i][j][0]*0.2989)+(rgb_image_array[i][j][1]*0.5870)+(rgb_image_array[i][j][2])
            side.append(pix)
            
        output_array.append(side)
        side=[]

    return output_array
   
def invert_grayscale(image_array):
    '''
    invert_grayscale([[255, 10, 0],[200, 20, 5],[143, 0, 1]])
    [[0, 245, 255], [55, 235, 250], [112, 255, 254]]
    
    (list) -> list
    
    Inverts the vales of the grey scale
    
    '''
    side=[]
    output_array=[]
    
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            side.append(255-image_array[i][j])
            
        output_array.append(side)
        side=[]

    return output_array
   
def invert_rgb(image_array):
    '''
    (list) -> list
    
    Inverts of the values of the RGB
    
    '''
    side=[]
    pix=[]
    output_array=[] 
    
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            for z in range(3):
                pix.append(255-image_array[i][j][z])
                
            side.append(pix)
            pix=[]
            
        output_array.append(side)
        side=[]

    return output_array 