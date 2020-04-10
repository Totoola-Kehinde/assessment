#global variables
currentlyInfected = 0

class estimate():
  #OUTPUTS
  data = {}
  impact = {}
  severeImpact = {}

  def get_data(self, name,avgAge, avgDailyIncomeInUSD, avgDailyIncomePopulation, periodType, timeToElapse,reportedCases, population, totalHospitalBeds):
      self.data = {
        'region': {
          name : name, #Continent
          avgAge : avgAge,
          avgDailyIncomeInUSD : avgDailyIncomeInUSD,
          avgDailyIncomePopulation : avgDailyIncomePopulation
        },
        periodType : periodType,
        timeToElapse : timeToElapse,
        population : population,
        totalHospitalBeds : totalHospitalBeds
      }

  #Impact Estimator to get the value of currently Infected
  def covid19ImpactEstimator(self, reportedCases):
    self.currentlyInfected = {
      'impact': reportedCases * 10,
      'severeImpact': reportedCases * 50
    }
    #Insert data 
    self.get_data('Africa', 19.5, 5, 0.71, 'days', 58, 674, 66622705, 1380614)

    #make copy of data to create impact result
    self.impact = self.data.copy()
    self.impact['currentlyInfected'] = self.currentlyInfected['impact']

    #make copy of data to create severeImpact result
    self.severeImpact = self.data.copy()
    self.severeImpact['currentlyInfected'] = self.currentlyInfected['severeImpact']

    print(self.impact)
    print(self.severeImpact)

  def estimateFor28Days(self, reportedCases):
    self.currentlyInfected = {
      'impact': reportedCases * 10,
      'severeImpact': reportedCases * 50
    }
    #estimate for 28 days
    infectionsByRequestedTime = {
      'impactFor28Days': self.currentlyInfected['impact'] * 512,
      'severeImpactFor28Days': self.currentlyInfected['severeImpact'] * 512
    } 
    print(infectionsByRequestedTime['impactFor28Days'])
    print(infectionsByRequestedTime['severeImpactFor28Days'])

def estimator(data):
  return data

impacts = estimate()
reportedCases = 20
impacts.covid19ImpactEstimator(reportedCases)    #output estimates {impact and severeImpact}
impacts.estimateFor28Days(reportedCases)         #estimate for 28 days {impact and SevereImpact}
