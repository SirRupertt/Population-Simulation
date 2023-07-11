import random
import numpy as np

class City():
    def __init__(self):
        self.pop = 100
        self.popchange= 0
        self.BR = 0
        self.DR=0
        self.x = np.random.standard_normal(self.pop)
        self.y = 2 * np.random.standard_normal(self.pop) 
        
    
    def update(self, widgets):
        print("Updating")
        self.popchange = widgets.get('BR') - widgets.get('DR')
        self.pop += self.popchange
        
        #Positive Change 
        if self.popchange >= 0:
            ix = np.random.standard_normal(self.popchange) 
            iy = 2 * np.random.standard_normal(self.popchange) 
            #update plot
            self.x = np.append(self.x, ix)
            self.y = np.append(self.y, iy)
        
        #Negative change
        if(self.popchange < 0):
            if(self.pop > abs(self.popchange)):
                for i in range(abs(self.popchange)):
                    self.x =np.delete(self.x, -1, 0)
                    self.y = np.delete(self.y, -1, 0)   