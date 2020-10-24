import time

def merge_sort(data,drawdata, timetick):
    merge_sort_algo(data,0,len(data)-1,drawdata,timetick)
    
def merge_sort_algo (data,left,right,drawdata,timetick):
    if left <right :
        middle =(left+right)//2
        merge_sort_algo (data,left,middle,drawdata,timetick)
        merge_sort_algo (data,middle+1,right,drawdata,timetick)
        merge (data,left,middle,right,drawdata,timetick)
        
def merge(data,left,middle,right,drawdata,timetick):
    
    drawdata(data, getcolorArray(len(data), left, middle, right))
    time.sleep(timetick)
    
    leftpart = data[left : middle+1]
    rightpart = data[middle+1 : right+1]
    
    leftidx=rightidx=0
    
    for dataidx in range(left,right+1):
        if leftidx< len(leftpart) and rightidx < len(rightpart):
            if leftpart[leftidx]<=rightpart[rightidx]:
                data[dataidx]=leftpart[leftidx]
                leftidx+=1
            else:
                data[dataidx]=rightpart[rightidx]
                rightidx+=1
        elif leftidx < len(leftpart) :
            data[dataidx]=leftpart[leftidx]
            leftidx+=1
        else:
            data[dataidx]=rightpart[rightidx]
            rightidx+=1

##data=[1,90,20,5,0,25,9]
##merge_sort(data, 0, 0)
##print(data)

def getcolorArray(length,left,middle,right):
    colorArray = []
    
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")

    return colorArray 
    