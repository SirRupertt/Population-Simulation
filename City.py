import random
import numpy as np
from sklearn.datasets import make_blobs
from pandas import DataFrame

class City():
    def __init__(self, loc):
        self.pop = 100
        self.popchange= 0
        self.BR = 0
        self.DR=0
        self.loc=(random.randint(-10,10),random.randint(-10,10))
        self.x, self.y = make_blobs(n_samples=self.pop, centers=[self.loc], n_features=2)
        self.df = DataFrame(dict(x=self.x[:,0], y=self.x[:,1], label=self.y))
        #print(self.df.loc[:,"x"])  
    
    def update(self, widgets):
        print("Updating")
        self.popchange = widgets.get('BR') - widgets.get('DR')
        self.pop += self.popchange
        
        self.x, self.y = make_blobs(n_samples=self.pop, centers=[self.loc], n_features=2)
        self.df = DataFrame(dict(x=self.x[:,0], y=self.x[:,1], label=self.y))
        #Positive Change 
        #if self.popchange >= 0:
        #    ix = np.random.standard_normal(self.popchange) 
        #    iy = 2 * np.random.standard_normal(self.popchange) 
        #    #update plot
        #    self.x = np.append(self.x, ix)
        #    self.y = np.append(self.y, iy)
        
        #Negative change
        #if(self.popchange < 0):
        #    if(self.pop > abs(self.popchange)):
        #        for i in range(abs(self.popchange)):
        #            self.x =np.delete(self.x, -1, 0)
        #            self.y = np.delete(self.y, -1, 0)   