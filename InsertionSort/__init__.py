import time
colorArray=[]
def insertion_sort(data,drawdata,timetick):
    global colorArray
    
    for i in range(1,len(data)):
        CurrNumber=data[i]
        j = i-1
        while j >=0 and CurrNumber < data[j] : 
                data[j+1] = data[j]
                drawdata(data,GetColorArray(data,j))
                time.sleep(timetick)
                j -= 1
                
        data[j+1] = CurrNumber
        colorArray[j+1]='orange'
        drawdata(data,colorArray)
        time.sleep(timetick)
        


#data=[40,30,5,90,0,2]
#insertion_sort(data, 0, 0)
#print(data)

def GetColorArray(data,j1):
    global colorArray
    colorArray=[]
    
    for x in range(len(data)):
        colorArray.append('white')
        if x==j1 or x==j1+1:
            colorArray.append('yellow')
             
        
    return colorArray