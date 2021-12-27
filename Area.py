def TriangleArea(x, y):
    
    area=0.5*( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1])) )
    
    if area <= 0 :
        return int(area * -1)
    
    else:
        return int(area)