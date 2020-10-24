import time


def  partition(data,head,tail,drawdata,timetick):
    border=head
    pivot= data[tail]
    
    drawdata (data,getColorArray(len(data), head, tail, border, border))
    time.sleep(timetick)
    
    for j in range(head,tail):
        
        if data[j]<pivot:
            drawdata (data,getColorArray(len(data), head, tail, border, j,True))
            time.sleep(timetick)
        
            data[j],data[border]=data[border],data[j]
            border+=1
    
    #swap pivot with border values
    
    drawdata (data,getColorArray(len(data), head, tail, border, tail,True))
    time.sleep(timetick)
    
    data[border],data[tail]=data[tail],data[border]
    
    return border

def quick_sort(data,head,tail,drawdata,timetick):
    
    if head<tail:
        partitionIdx= partition(data,head,tail,drawdata,timetick)
        
        #Left Partition
        quick_sort(data, head, partitionIdx-1, drawdata, timetick)
        
        #Right Partition
        quick_sort(data, partitionIdx+1, tail, drawdata, timetick)
        
    
#data=[24,30,1,0,5,45,6]
#quick_sort(data, 0, len(data)-1, 0, 0)
#print(data)

def getColorArray(dataLength, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for x in range(dataLength):
        #base coloring
        if x >= head and x <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if x == tail:
            colorArray[x] = 'blue' #Pivot
        elif x == border:
            colorArray[x] = 'red' #borderValue
        elif x == currIdx:
            colorArray[x] = 'yellow' #comparing index

        if isSwaping:
            if x == border or x == currIdx:
                colorArray[x] = 'green' #sorting done

    return colorArray