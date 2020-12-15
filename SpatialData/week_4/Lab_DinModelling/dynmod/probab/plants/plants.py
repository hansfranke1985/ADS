from pcraster import *
from pcraster.framework import *

class Plants(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('clone.map')

  def initial(self):
    pass

  def dynamic(self):
    pass

    
nrOfTimeSteps=50
myModel = Plants()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

