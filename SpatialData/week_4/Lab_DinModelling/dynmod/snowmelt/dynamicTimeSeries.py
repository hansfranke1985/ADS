from pcraster import *
from pcraster.framework import *

class MyFirstModel(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('dem.map')

  def initial(self):
    print('running the initial')


  def dynamic(self):
    precipitation=timeinputscalar('precip.tss',1)
    self.report(precipitation, 'precipi')
   
    
nrOfTimeSteps=181
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

  




