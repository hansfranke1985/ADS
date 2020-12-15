from pcraster import *
from pcraster.framework import *

class Fire(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('clone.map')

  def initial(self):
    self.fire=self.readmap('start')

  def dynamic(self):
    nrOfBurningNeighbours=window4total(scalar(self.fire))
    neighbourBurns=nrOfBurningNeighbours > 0
    self.report(neighbourBurns,'nb')
    potentialNewFire=pcrand(neighbourBurns,pcrnot(self.fire))
    self.report(potentialNewFire,'pnf')

    realization=uniform(1) < 0.1
    self.report(realization,'real')

    newFire=pcrand(potentialNewFire,realization)
    self.report(newFire,'nf')

    self.fire=pcror(self.fire,newFire)
    self.report(self.fire,'fire')

nrOfTimeSteps=20
myModel = Fire()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()

