from pcraster import *
from pcraster.framework import *

class MyFirstModel(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('dem.map')

  def initial(self):
    print('running the initial')

  def dynamic(self):
    timeStep = self.currentTimeStep()
    print('running the dynamic for time step: ', timeStep)
    
    print(conversionValue)
    
nrOfTimeSteps=10
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

  




