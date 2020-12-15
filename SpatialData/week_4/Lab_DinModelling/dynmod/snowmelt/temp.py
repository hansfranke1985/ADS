from pcraster import *

from pcraster.framework import *
class MyFirstModel(DynamicModel):
  def __init__(self):
    DynamicModel.__init__(self)
    setclone('dem.map')
  def initial(self):
    dem = self.readmap('dem')
    elevationMeteoStation = 2058.1
    elevationAboveMeteoStation = dem - elevationMeteoStation
    temperatureLapseRate = 0.005
    self.temperatureCorrection = elevationAboveMeteoStation *    temperatureLapseRate
    self.report(self.temperatureCorrection,'tempCor')
  def dynamic(self):
    precipitation=timeinputscalar('precip.tss',1)
    self.report(precipitation,'pFromTss')
    temperatureObserved = timeinputscalar('temp.tss',1)
    self.report(temperatureObserved,'tempObs')
 
    temperature = temperatureObserved - self.temperatureCorrection
    self.report(temperature,'temp')
    freezing = temperature < 0.0
    self.report(freezing,'freez')
    snowFall = ifthenelse(freezing, precipitation, 0.0)
    rainFall = ifthenelse(pcrnot(freezing), precipitation, 0.0)
    self.report(snowFall,'snF')
    self.report(rainFall,'rF')
nrOfTimeSteps=181
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()
print('finished')

  




