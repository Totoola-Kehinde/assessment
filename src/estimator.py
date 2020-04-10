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
          'name' : name, #Continent
          'avgAge' : avgAge,
          'avgDailyIncomeInUSD' : avgDailyIncomeInUSD,
          'avgDailyIncomePopulation' : avgDailyIncomePopulation
        },
        'periodType' : periodType,
        'timeToElapse' : timeToElapse,
        'population' : population,
        'totalHospitalBeds' : totalHospitalBeds
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
    #Updating estimate output data by copy previous and adding new dict items
    self.impact = self.impact.copy()
    self.impact['infectionsByRequestedTime'] = infectionsByRequestedTime['impactFor28Days']
    self.severeImpact = self.severeImpact.copy()
    self.severeImpact['infectionsByRequestedTime'] = infectionsByRequestedTime['impactFor28Days']

    print(infectionsByRequestedTime['impactFor28Days'])
    print(infectionsByRequestedTime['severeImpactFor28Days'])

  def severeCasesByRequestedTime(self):
    #Determine 15% of infectionsByRequestedTime.
    severeCasesByRequestedTime = (15 / 100) * self.severeImpact['infectionsByRequestedTime']
    #Update Estimate Output
    self.severeImpact = self.severeImpact.copy()
    self.severeImpact['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    print('Here is severeCasesByRequestedTime :')
    print(severeCasesByRequestedTime)
    #determine the number of available beds.
    #65% of hospital beds been occupied
    occupied_beds = (65 / 100) * self.severeImpact['totalHospitalBeds']
    #capacity of patients by hospital 95%
    capacity = (95 / 100) *self.severeImpact['totalHospitalBeds']
    #35% bed availability in hospitals for severe COVID-19 positive patients.
    #capacity of beds minus occupied beds will give available beds
    available_beds = int(capacity) - int(occupied_beds)
    #percentage availabilty of beds
    percentageOfBedAvailable = (available_beds / capacity) * 100
    #hospitalBedsByRequestedTime
    hospitalBedsByRequestedTime = available_beds
    #Update Estimate Data
    self.severeImpact = self.severeImpact.copy()
    self.severeImpact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
    print('Percentage availablity of beds :')
    print(percentageOfBedAvailable)
    print('Available Beds :')
    print(available_beds)

  def casesForICUByRequestedTime(self):
    #estimated number of severe positive cases that will require ICU care
    casesForICUByRequestedTime = (5 / 100) * self.severeImpact['infectionsByRequestedTime']
    #Update Estimate Data For SevereImpact Outputs
    self.severeImpact = self.severeImpact.copy()
    self.severeImpact['casesForICUByRequestedTime'] = casesForICUByRequestedTime
    #determine 2% of infectionsByRequestedTime
    #estimated number of severe positive cases that will require ventilators
    casesForVentilatorsByRequestedTime = (2 / 100) * self.severeImpact['infectionsByRequestedTime']
    #Update Estimate Data For SevereImpact Outputs
    self.severeImpact = self.severeImpact.copy()
    self.severeImpact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
  
  def moneyLossInTheEconomy(self):
    #estimate how much money the economy is likely to lose over the said period
    #65% average daily income of the region assumed to be $5
    #30 days to be the said period
    dollarsInFlight = self.severeImpact['infectionsByRequestedTime'] * (0.65 * 5 * 30)
    self.severeImpact = self.severeImpact.copy()
    self.severeImpact['dollarsInFlight'] = dollarsInFlight

def estimator(data):
  return data

impacts = estimate()
reportedCases = 20
impacts.covid19ImpactEstimator(reportedCases)    #output estimates {impact and severeImpact}
impacts.estimateFor28Days(reportedCases)         #estimate for 28 days {impact and SevereImpact}
print(impacts.impact)

#Determine 15% of infectionsByRequestedTime to get 'severeCasesByRequestedTime' and figure out hospitalBedsByRequestedTime
impacts.severeCasesByRequestedTime()
print(impacts.severeImpact)
impacts.moneyLossInTheEconomy()

#This completely outputs the severeImpact result with all required parameters and info
print(impacts.severeImpact)

