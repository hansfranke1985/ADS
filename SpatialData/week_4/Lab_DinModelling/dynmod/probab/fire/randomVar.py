from pcraster import *
from pcraster.framework import *

class RandomModel(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('clone.map')

  def initial(self):
    pass

  def dynamic(self):
    pass

nrOfTimeSteps=10
myModel = RandomModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

