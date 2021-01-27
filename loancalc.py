salary = 0
interest = 0.22
year = 0
principal = 0
months = 0
periodicRate = 0
payments =0

def getPrincipleAmount():
    principal = int(input("Please enter your principal amount - "))
    return principal

def getPaybackPeriod():
    print("A year consists of 12 months")
    year = int(input("Please enter duration of loan in years - "))
    return year

def getPeriodicPayments(year):
    months = year*12
    return months

def periodicInterestRate(interest):
    periodicRate = float(interest/12)
    return periodicRate

def calculateDiscountFactor(months, periodicRate):
    discountFactor = float(((( 1 + periodicRate )**months) - 1)/ (periodicRate*(1+periodicRate)**months))
    return discountFactor

def calculateLoan():
    principal = getPrincipleAmount()
    year = getPaybackPeriod()
    months = getPeriodicPayments(year)
    periodicRate = periodicInterestRate(interest)
    payments = principal/calculateDiscountFactor(months,periodicRate)
    print("Your monthly payments will be", payments)
    print("Total amount to pay at the end of", round(year,2), "years will be", round(payments*months,2))
    print("Total Interest paid -", round((payments*months)-principal,2))

calculateLoan()