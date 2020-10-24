from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubblesort
from Merge_Sort import merge_sort
from QuickSort import quick_sort
from Heap_Sort import heapsort
from InsertionSort import insertion_sort



root = Tk()

root.title('Visualize Sorting Algorithm')
root.maxsize(900, 600)
root.config(bg='black')


#variables
selected_alg = StringVar()
data =[]

#Functions

#Draw Data as Bar Graph

def drawdata(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text =str(data[i]))
        
        root.update_idletasks()
        


#Generate Array function

def Generate():
    global data
    
    ##print('Algorithm Selected: ' + selected_alg.get())
    
    minValue= minEntry.get()
    maxValue=maxEntry.get()
    size=sizeEntry.get()
    
    data=[]
    
    for _ in range(size):
        data.append(random.randrange(minValue,maxValue+1))
    
    drawdata(data, ['red' for _ in range(len(data))]) ##['red','red',.....'red']
    
def StartAlgorithm():
    global data
    speed = speedScale.get()
    
    if algomenu.get()=='Bubble Sort':
        bubblesort(data,drawdata,speed)
    elif algomenu.get()=='Merge Sort':
        merge_sort(data,drawdata,speed)
    elif  algomenu.get()=='Quick Sort':
        quick_sort(data, 0, len(data)-1,drawdata,speed)
    elif algomenu.get()=='Heap Sort':
        heapsort(data,drawdata,speed)
    elif algomenu.get()=='Insertion Sort':
        insertion_sort(data,drawdata,speed)

    drawdata(data,['green' for _ in range(len(data))])

#Frame/Base Layout

UI_Frame= Frame(root, width=600, height =200,bg='grey')
#UI_Frame.grid(row =0 , column =0 , padx=10, pady=5)
UI_Frame.pack(fill=BOTH, expand=YES)

canvas =Canvas(root, width =600, height=380, bg='white')
#canvas.grid(row=1, column=0, padx=10, pady=5)
canvas.pack(fill=BOTH , expand= YES)

#User Interface Area
#Row[0]

label= Label(UI_Frame,text ='Algorithm :' ,bg='grey')
label.grid(row=0, column=0, padx=5 ,pady=5 , sticky=W )

#Select Algorithm from drop down

algomenu = ttk.Combobox(UI_Frame,state='readonly',textvariable= selected_alg,values=['Bubble Sort','Merge Sort','Quick Sort','Heap Sort','Insertion Sort'])
algomenu.grid(row=0, column=1, padx=5,pady=5)
algomenu.current(0)

#Speed Scale

speedScale = Scale(UI_Frame, from_=0.01, to=1.0, length=100, digits=3, resolution=0.01, orient=HORIZONTAL, label="Select Speed [sec]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

#Start Algorithm Button

Button(UI_Frame, text="Start Algorithm", command=StartAlgorithm, bg='white').grid(row=0, column=3, padx=5, pady=5)


#Row[1]

#Enter the min max and size of array

sizeEntry = Scale(UI_Frame,from_=3, to =30, orient=HORIZONTAL,label='Array Size')
sizeEntry.grid(row=1 ,column=0 ,padx=5 ,pady=5)

minEntry = Scale(UI_Frame,from_=0, to =10, orient=HORIZONTAL,label='Minimum Entry')
minEntry.grid(row=1 ,column=1 ,padx=5 ,pady=5)

maxEntry = Scale(UI_Frame,from_=10, to =100, orient=HORIZONTAL,label='Maximum Entry')
maxEntry.grid(row=1 ,column=2 ,padx=5 ,pady=5)

#Generate  Array Button

button = Button(UI_Frame, text='Generate Array', command=Generate, bg='white')
button.grid(row =1, column =3, padx=5,pady=5)


root.mainloop()


