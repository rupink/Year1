# ESC180 Lab 1
# Connected Cows
# DO NOT modify any function or argument names

import math
def find_euclidean_distance(x1, y1, x2, y2):
    """
    find_euclidean_distance(3.0,3.0,2.0,5.0)
    2.24
    find_euclidean_distance(5.0,2.0,4.0,2.0)
    1.0
    (float)->float
    Finds the distance between two points
    """
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    distance=round(distance,2)
    return distance


def is_cow_within_bounds(cow_position, boundary_points):
    """
    is_cow_within_bounds([3, 3], [[2, 5], [5, 5], [5, 1], [2, 1]])
    1
    is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]])
    0
    (list,list)->int
    Tells if the cow is within boundaries
    """
    x=cow_position[0]
    y=cow_position[1]
    x1=boundary_points[0][0]
    y1=boundary_points[0][1]
    x2=boundary_points[2][0]
    y2=boundary_points[2][1]
    if x1<x and x2>x and y>y2 and y<y1:
        print ("1")
    else:
        print ("0")

def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    find_cow_distance_to_boundary([3, 3], [2, 5])
    2.24
    find_cow_distance_to_boundary([2, 2], [0, 1])
    2.24
    (list)->float
    Tells distance between boundary point and the cow's position
    """
    x=cow_position[0]
    y=cow_position[1]
    x1=boundary_point[0]
    y1=boundary_point[1]
    distance=math.sqrt((x-x1)**2+(y-y1)**2)
    distance=round (distance,2)
    return distance
    
def find_time_to_escape(cow_speed, cow_distance):
    """
    find_time_to_escape(2.0, 8.0)
    4.0
    find_time_to_escape(9.0, 111.0)
    12.33
    (float)->float
    Tells the time it takes for the cow to reach the boundary
    """
    if cow_speed==0:
        return -1
    else:
        time=cow_distance/cow_speed
        time= round(time,2)
        print (time)
    
def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):    
    """
    report_cow_status([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]])
    7.09
    report_cow_status([0, 0], [3, 7], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]])
    2.94
    report_cow_status([0, 0], [3, 3], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]])
    -1
    report_cow_status([3, 3], [3, 6], 10.0, [[2, 5], [5, 5], [5, 1], [2,0]])
    0
    (list,list,float,list)->float,int
    Tells if the cow is entering or exiting the boundary. Tells if cows are within bounds and how long it would take to a boundary point.
    """
    #case 1
    cow_position1_x=cow_position1[0]
    cow_position1_y=cow_position1[1]
    cow_position2_x=cow_position2[0]
    cow_position2_y=cow_position2[1]
    x1=boundary_points[0][0]
    y1=boundary_points[0][1]
    x2=boundary_points[2][0]
    y2=boundary_points[2][1]

    if (cow_position1_x>x1 and cow_position1_y>y2 and cow_position1_x<x2 and cow_position1_y<y1) and (cow_position2_x>x1 and cow_position2_y>y2 and cow_position2_x<x2 and cow_position2_y<y1):
        left=abs(cow_position2_x-x1)
        right=abs(cow_position2_x-x2)
        up=abs(cow_position2_y-y1)
        down=abs(cow_position2_y-y2)
        ways=[left,right,up,down]
        closest=min(ways)
        travel=math.sqrt((cow_position1_x-cow_position2_x)**2+(cow_position1_y-cow_position2_y)**2)
        velocity=travel/delta_t
        time=closest/velocity
        time=round(time,2)
        print (time)

       #case 2
    elif not(cow_position1_x>x1 and cow_position1_y>y2 and cow_position1_x<x2 and cow_position1_y<y1) and not (cow_position2_x>x1 and cow_position2_y>y2 and cow_position2_x<x2 and cow_position2_y<y1):
        travel=math.sqrt((cow_position1_x-cow_position2_x)**2+(cow_position1_y-cow_position2_y)**2)
        distance=math.sqrt((x1-cow_position2_x)**2+(y1-cow_position2_y)**2)
        velocity=travel/delta_t
        time=distance/velocity
        time=round(time,2)
        print (time)


        #case 3
    elif (not(cow_position1_x>x1 and cow_position1_y>y2 and cow_position1_x<x2 and cow_position1_y<y1)) and (cow_position2_x>x1 and cow_position2_y>y2 and cow_position2_x<x2 and cow_position2_y<y1):
        print ("-1")

        #case 4
    elif (cow_position1_x>x1 and cow_position1_y>y2 and cow_position1_x<x2 and cow_position1_y<y1) and (not(cow_position2_x>x1 and cow_position2_y>y2 and cow_position2_x<x2 and cow_position2_y<y1)):
        print ("0")

if __name__ == '__main__':
    # Test your code by running your functions here, and printing the
    # results to the terminal.
    # This code will not be marked
    print('Testing functions...')
    # test_distance = find_euclidian_distance(3.0, 3.0, 2.0, 5.0)
    # print(test_distance)
    # test_distance should be 2.24    