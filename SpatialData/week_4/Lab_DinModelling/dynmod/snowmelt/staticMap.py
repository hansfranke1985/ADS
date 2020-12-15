from pcraster import *
from pcraster.framework import *

class MyFirstModel(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('dem.map')

  def initial(self):
    print('running the initial')
    dem = self.readmap('dem')
    slopeOfDem = slope(dem)
    self.report(slopeOfDem,'gradient')

  def dynamic(self):
    timeStep = self.currentTimeStep()
    print('running the dynamic for time step: ', timeStep)
    
   
    
nrOfTimeSteps=10
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

  




