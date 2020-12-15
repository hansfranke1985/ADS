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
    precip = self.readmap("precip")
    #Add a statement converting from m/day to mm/day
    precip = precip * 1000
    self.report(precip, "pmm")
    #try to make an animation of maps that shows where precipitation is above 0.01 m/day
    high = precip > 0.01
    self.report(high, 'hp')
    
   
    
nrOfTimeSteps=181
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

  




