region = {}
name = ""
avgAge = ""
avgDailyIncomeInUSD = ""
avgDailyIncomePopulation = ""
periodType = ""
timeToElapse = ""
reportedCases = ""
population = ""
totalHospitalBeds = ""

data = {
  region: {
  name: "Africa",
  avgAge: 19.7,
  avgDailyIncomeInUSD: 5,
  avgDailyIncomePopulation: 0.71
  },
  periodType: "days",
  timeToElapse: 58,
  reportedCases: 674,
  population: 66622705,
  totalHospitalBeds: 1380614
}

def covid19ImpactEstimator(data):
  # get currently infected cases
  currentlyInfected = data.reportedCases * 10
  return currentlyInfected

def estimator(data):
  return data

