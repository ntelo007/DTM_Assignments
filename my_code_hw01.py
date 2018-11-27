#-- my_code_hw01.py
#-- hw01 GEO1015/2018
#-- [YOUR NAME]
#-- [YOUR STUDENT NUMBER] 
#-- [YOUR NAME]
#-- [YOUR STUDENT NUMBER] 


import math
import scipy.spatial
import numpy as np

def nn_interpolation(list_pts_3d, j_nn):
    """
    !!! TO BE COMPLETED !!!`
     
    Function that writes the output raster with nearest neighbour interpolation
     
    Input:
        list_pts_3d: the list of the input points (in 3D)
        j_nn:        the parameters of the input for "nn"
    Output:
        returns the value of the area
    #-- to speed up the nearest neighbour us a kd-tree
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html#scipy.spatial.KDTree.query
    
    """  


    #empty list to append middle-points of grid
    middle_pts = []                                         
    
    #list of x,y coordinates without z value
    list_pts2d = list_pts_3d[:]
    for i in list_pts2d:
        i.pop()
    
    #convert list of points into an array
    list_pts2d = np.array(list_pts2d)
    
    #bounding box coordinates
    xmin = np.min(list_pts2d[:,0])
    xmax = np.max(list_pts2d[:,0])
    ymin = np.min(list_pts2d[:,1])
    ymax = np.max(list_pts2d[:,1])
    
    #append middle_points to list middle_pts
    for i in range(1,int(ymax-ymin)):
        for j in range(1,int(xmax-xmin)):
            middle_pts.append([xmin+j-0.5,ymin+i-0.5])
            
    #query for nearest middle_points to points from list_pts
    kd = scipy.spatial.KDTree(list_pts2d)
    d, i = kd.query(middle_pts, k=1)

    
    print (d,i)
    print("=== Nearest neighbour interpolation ===")
    print("cellsize:", j_nn['cellsize'])
    print("File written to", j_nn['output-file'])



def idw_interpolation(list_pts_3d, j_idw):
    """
    !!! TO BE COMPLETED !!!
     
    Function that writes the output raster with IDW
     
    Input:
        list_pts_3d: the list of the input points (in 3D)
        j_idw:       the parameters of the input for "idw"
    Output:
        returns the value of the area
 
    """  
    print("=== IDW interpolation ===")

    # print("cellsize:", j_idw['cellsize'])
    # print("radius:", j_idw['radius'])

    #-- to speed up the nearest neighbour us a kd-tree
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html#scipy.spatial.KDTree.query
    # kd = scipy.spatial.KDTree(list_pts)
    # i = kd.query_ball_point(p, radius)
    
    print("File written to", j_idw['output-file'])


def tin_interpolation(list_pts_3d, j_tin):
    """
    !!! TO BE COMPLETED !!!
     
    Function that writes the output raster with linear in TIN interpolation
     
    Input:
        list_pts_3d: the list of the input points (in 3D)
        j_tin:       the parameters of the input for "tin"
    Output:
        returns the value of the area
 
    """  
    print("=== TIN interpolation ===")

    #-- example to construct the DT
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html#scipy.spatial.Delaunay
    # dt = scipy.spatial.Delaunay([])
    
    print("File written to", j_tin['output-file'])


def kriging_interpolation(list_pts_3d, j_kriging):
    """
    !!! TO BE COMPLETED !!!
     
    Function that writes the output raster with ordinary kriging interpolation
     
    Input:
        list_pts_3d: the list of the input points (in 3D)
        j_kriging:       the parameters of the input for "kriging"
    Output:
        returns the value of the area
 
    """  
    print("=== Ordinary kriging interpolation ===")

    
    
    print("File written to", j_kriging['output-file'])
