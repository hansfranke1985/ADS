from pcraster import *
from pcraster.framework import *

class MyFirstModel(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('dem.map')

  def initial(self):
    self.conversionValue = 3.0
    self.reservoir = 30.0 / self.conversionValue
    print('initial reservoir is: ', self.reservoir)
    self.inflow = 0.5

  def dynamic(self):
    
    outflow = 0.1 * self.reservoir 
    self.reservoir = self.reservoir - outflow + self.inflow
    print("reservoir", self.reservoir)
    print("conversion value", self.conversionValue)
    print("Inflor", self.inflow)

nrOfTimeSteps=10000
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

  




