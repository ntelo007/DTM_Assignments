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

    #convert list of points into an array
    list_pts_3d = np.array(list_pts_3d)

    #bounding box coordinates
    xmin = np.min(list_pts_3d[:,0])
    xmax = np.max(list_pts_3d[:,0])
    ymin = np.min(list_pts_3d[:,1])
    ymax = np.max(list_pts_3d[:,1])

    #append middle_points
    for i in range(1,int(ymax-ymin+1)):
        for j in range(1,int(xmax-xmin+1)):
            middle_pts.append([xmin+j-0.5,ymin+i-0.5])
            
    #check if middle_points are in the convex hull
    list2d = []
    for k in list_pts_3d:
        list2d.append([k[0],k[1]])
    tri = scipy.spatial.Delaunay(list2d)
    checklist = tri.find_simplex(middle_pts)
    
    #query for nearest middle_points to points from list_pts
    kd = scipy.spatial.KDTree(list_pts_3d[:,(0,1)])
    d, i = kd.query(middle_pts, k=1)

    #append z value to middle points
    for n in range(len(middle_pts)):
        middle_pts[n].append(list_pts_3d[i[n]][2])
    for n in range(len(middle_pts)):
        if checklist[n] == -1:
            middle_pts[n][2] = -9999

    #create ASCI file
    ncols = (xmax-xmin)/int(j_nn['cellsize'])
    nrows = (ymax-ymin)/int(j_nn['cellsize'])
    xll = xmin
    yll = ymin
    nodata = -9999
    
    nn = open(j_nn['output-file'],"w+")
    nn.write("NCOLS {0}\n".format(ncols))
    nn.write("NROWS {0}\n".format(nrows))
    nn.write("XLLCORNER {0}\n".format(xll))
    nn.write("YLLCORNER {0}\n".format(yll))
    nn.write("CELLSIZE {0}\n".format(j_nn['cellsize']))
    nn.write("NODATA_VALUE {0}\n".format(nodata))
    nn.write("{0}\n".format(nodata))
    a = int(len(middle_pts)-ncols)
    b = int(len(middle_pts))
    while a>0:
        for i in range(a,b):
            nn.write("{0} ".format(middle_pts[i][2]))
        nn.write('\n')
        a = a - int(ncols)
        b = b - int(ncols)
    nn.close()

    
    """
    NCOLS 3
    NROWS 3
    XLLCORNER 0
    YLLCORNER 0
    CELLSIZE 10
    NODATA_VALUE -9999
    1.0 2.0 3.0
    4.0 5.0 6.0
    7.0 8.0 9.0
    """
    
    
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
