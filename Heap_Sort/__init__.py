import time

#To heapify subtree rooted at index i. 
# n is size of heap

#variable


def heapify(data,length,Idx,drawdata,timetick):
    
    largest=Idx
    
    left=2*Idx+1
    right=2*Idx+2

    
    # See if left child of root exists and is 
    # greater than root 
    if left < length and data[Idx] < data[left]:
        largest=left
        
    # See if right child of root exists and is 
    # greater than root    
    if right< length and data[largest] <data[right]:
        largest=right
        
    # swap root, if needed 
     
    if largest!=Idx:
        data[Idx],data[largest]=data[largest],data[Idx]
    
        # Heapify the root.    
        heapify(data, length, largest,drawdata,timetick)
        drawdata(data,getcolorArray(data, largest, Idx))
        time.sleep(timetick)
        
    
def heapsort(data,drawdata,timetick):

    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    
    for i in range (len(data)//2 -1,-1,-1):
        heapify(data,len(data),i,drawdata,timetick)
    
    # Extract elements
    for i in range(len(data)-1,0,-1):
        #Swap the root element to last
        data[i],data[0]=data[0],data[i]
        
        #colorArray[len(data)-1]='green'
        #drawdata(data,colorArray)
        
        #print(data)
        
        heapify(data, i ,0,drawdata,timetick)
        
        
        
        
#data=[30,40,1,0,20,35]
#heapsort(data,0,0)
#print(data)

def getcolorArray(data,largest,currentIdx):
    
    colorArray=[]
    
    for  x in range (len(data)):
        
        if x<=largest and x>=currentIdx:
            colorArray.append('grey')
        elif x>=largest:
            colorArray.append('orange')
        else :
            colorArray.append('white')
            
        if x== largest or x==currentIdx :
            colorArray[x]='yellow'

            
    return colorArray