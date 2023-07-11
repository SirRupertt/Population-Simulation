import City
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import seaborn as sns
import time

#Create figure and axis
fig, ax = plt.subplots()
#Check for start button
def setup():
    #Making sure variables apply everywhere
    global running, cities, x, y, widgets, fig, ax, axcbar, citycount
    running = True
    #Creating placeholder variables to add to later
    x = np.array([])
    y = np.array([])
    cities = []
    
    #Adjusting figure where sliders, labels, graph is, ect.
    fig.subplots_adjust(bottom=0.2)
    axstart = fig.add_axes([0.7, 0.05, 0.1, 0.075])
    axstop = fig.add_axes([0.81, 0.05, 0.1, 0.075])
    axbirth = fig.add_axes([0.3, 0.07, 0.2, 0.075])
    axdeath = fig.add_axes([0.3, 0.02, 0.2, 0.075])
    axcbar = fig.add_axes([0.93,0.2, 0.05, 0.65])
    ax.set(xlim=(-10,10), ylim=(-10,10))
    ax.set_title('Simulation Simulation')
    
    #Create first city
    citycount = 1
    city1 = City.City([-10,10])
    #add city pop to global arrays
    x= np.append(x, city1.df.loc[:,"x"])
    y =np.append(y, city1.df.loc[:,"y"])
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
    plt.show(block=True)
    #Need to change to wait for button presses
    
    
def run(event): #Main running starts
    global fig, ax, x, y, running, axcbar, citycount
    #Check if quit
    print('RUN')
    #Count variable for what iteration
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
        plt.pause(0.5) #Pause so can be seen
        
        #Display
        plt.draw()
        
    #Update
        x = np.array([])
        y = np.array([])
        
        #If iterator is multiple of 5 add another city (TEMP)
        if(iter%5 ==0):
            citycount+=1
            #NEED DICTIONARY IF WANT UNIQUE NAMES
            cityname = "city" + str(citycount)
            cityname = City.City([10, 20])
            cities.append(cityname)
            
        
        #each city update
        for city in cities:
            #Grab widget values and send into
            BRVal = birthRateSlider.val
            DRVal = deathRateSlider.val
            city.update({'BR' : BRVal, 'DR': DRVal})
            #Create updated x,y 
            x= np.append(x, city.df.loc[:,"x"])
            y =np.append(y, city.df.loc[:,"y"])
            
    #Sleep 1.5s
        time.sleep(0.5)
    
    #If stop button pressed, exit function
    if not running:
        return()

#Stop button command that stops main loop and closes figure
def kill(event):
    print("KILL")
    global running
    running = False
    plt.close()
    return()

#run setup
setup()