import City
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import seaborn as sns
import time

fig, ax = plt.subplots()
#Check for start button
def setup():
    #Making sure variables apply everywhere
    global running, cities, x, y, widgets, fig, ax, axcbar
    running = True
    x = np.array([])
    y = np.array([])
    cities = []
    
    #Create figure and axis
    #fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    axstart = fig.add_axes([0.7, 0.05, 0.1, 0.075])
    axstop = fig.add_axes([0.81, 0.05, 0.1, 0.075])
    axbirth = fig.add_axes([0.3, 0.07, 0.2, 0.075])
    axdeath = fig.add_axes([0.3, 0.02, 0.2, 0.075])
    axcbar = fig.add_axes([0.93,0.2, 0.05, 0.65])
    ax.set(xlim=(-10,10), ylim=(-10,10))
    ax.set_title('Simulation Simulation')
    
    #Create first city
    city1 = City.City()
    x= np.append(x, city1.x)
    y =np.append(y, city1.y)
    cities.append(city1)
    
    #Create widgets (These stay static but values accessed many times)
    
    global startButton, stopButton, birthRateSlider, deathRateSlider
    startButton = widgets.Button(axstart, label='Start')
    stopButton = widgets.Button(axstop, label='Stop')
    birthRateSlider = widgets.Slider(axbirth, label="Birth Rate", valmin=0, valmax=1000, valinit=500, valstep=50)
    deathRateSlider = widgets.Slider(axdeath, label="Death Rate", valmin=0, valmax=1000, valinit=500, valstep=50)
    widgets = [startButton, startButton, birthRateSlider, deathRateSlider]

    startButton.on_clicked(run)
    stopButton.on_clicked(kill)
    #plt.ion()
    plt.show(block=True)
    #plt.pause(3) #Need to change to wait for button presses
    
    
def run(event): #Main running starts
    global fig, ax, x, y, running, axcbar
    #Check if quit
    print('RUN')
    iter=0
    while running:
        iter+=1
        print(iter)
    #Ploting 
        #Clear Axis
        ax.clear()
        
        #Get Data and plot
        ax.set_title('Simulation Simulation')
        kde = sns.kdeplot(x=x, y=y, fill=True, cmap='flare', ax=ax, cbar=True, cbar_ax=axcbar)
        plt.show()
        plt.pause(0.5)
        
        #Display
        #plt.show()
        #fig.canvas.draw_idle()
        plt.draw()
        
    #Update
        x = np.array([])
        y = np.array([])
        #each city update
        for city in cities:
            #Grab widget values and send into
            BRVal = birthRateSlider.val
            DRVal = deathRateSlider.val
            city.update({'BR' : BRVal, 'DR': DRVal})
            #Create updated x,y 
            x= np.append(x, city.x)
            y= np.append(y, city.y)
            
    #Sleep 1.5s
        time.sleep(0.5)
        
    if not running:
        return()

def kill(event):
    print("KILL")
    global running
    running = False
    plt.close()
    return()

#run setup
setup()