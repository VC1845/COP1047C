'''
Request
The customer requests a program that computes a person’s income tax.

Analysis
Analysis often requires the programmer to learn some things about the problem domain, in this case, the relevant tax law. For the sake of simplicity, let’s assume the following tax laws:

All taxpayers are charged a flat tax rate of 20%
All taxpayers are allowed a $10,000 standard deduction
For each dependent, a taxpayer is allowed an additional $3,000 deduction
Gross income must be entered to the nearest penny
The income tax is expressed as a decimal number
'''

# inputs : gross income and number of dependents
# output : person's income tax

# taxRate = 20%
# indDeduction = 10000
# depDeduction = 3000
# IncomeTax = (Gross Income - individual deduction - dependent deduction) * Tax Rate

#user input
grossIncome = int(input('Enter the gross income: '))
numDependents = int(input('Enter the number of dependents: '))

#calculations
indDeduction = 10000
depDeduction = 3000 * numDependents
taxRate = 0.2
incomeTax = (grossIncome - indDeduction - depDeduction)*taxRate

#output
print(f'The income tax is ${incomeTax:.1f}')