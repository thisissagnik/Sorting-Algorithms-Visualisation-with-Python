import time

colorArray =[]

def bubblesort(data,drawdata,timetick):
    global colorArray
    for i in range(len(data)-1):
        for j in range(0,len(data)-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawdata(data, getcolorArray(data, j,i))
                time.sleep(timetick)
        if i!=len(data):
            colorArray[len(data)-i-1]='orange'
            drawdata(data,colorArray)
            time.sleep(timetick)   
         
                
def getcolorArray(data,idx,i):
    global colorArray
    colorArray =[]
    
    for  x in range(len(data)):
        if x==idx or x==idx+1 :
            colorArray.append("yellow")
        elif x>idx+1 or x<len(data)-i-1:
            colorArray.append("white")
        elif x<idx:
            colorArray.append("red")
        else :
            colorArray.append("orange")
    return colorArray
            
    