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
    self.temperatureCorrection = elevationAboveMeteoStation *      temperatureLapseRate
    self.report(self.temperatureCorrection,'tempCor')
    self.snow = 0.0
    
  def dynamic(self):
    precipitation = timeinputscalar('precip.tss',1)
    temperatureObserved = timeinputscalar('temp.tss',1)
    self.report(precipitation,'pFromTss')
    self.report(temperatureObserved,'tempObs')
    temperature = temperatureObserved - self.temperatureCorrection
    self.report(temperature,'temp')
    freezing = temperature < 0.0
    self.report(freezing,'fr')
    snowFall = ifthenelse(freezing, precipitation, 0.0)
    rainFall = ifthenelse(pcrnot(freezing), precipitation, 0.0)
    self.report(snowFall,'snF')
    self.report(rainFall,'rF')
    self.snow = self.snow + snowFall
    potentialMelt = ifthenelse(pcrnot(freezing),temperature*0.01,0)
    actualMelt = min(self.snow,potentialMelt)
    self.report(actualMelt, 'amelt')
    self.snow = self.snow - actualMelt
    self.report(self.snow,'snow')
    runoff = actualMelt + rainFall
    self.report(runoff, "runoff")
  
    
    
nrOfTimeSteps=181
myModel = MyFirstModel()
dynamicModel = DynamicFramework(myModel,nrOfTimeSteps)
dynamicModel.run()


