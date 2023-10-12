# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]

insurance_data = zip(names, insurance_costs)
print(insurance_data)

insurance_data = list(zip(names, insurance_costs))

estimated_insurance_data = []

estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

print("Here is the actual insurance cost data: " + str(insurance_data))

print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

#Extras
maria_insurance_cost_difference = 4222 - 4150
rohan_insurance_cost_difference = 5442 - 5320
valentina_insurance_cost_difference = 36368 - 35210
akira_insurance_cost_difference = 2149 - 2149

insurance_cost_difference = [maria_insurance_cost_difference, rohan_insurance_cost_difference, valentina_insurance_cost_difference, akira_insurance_cost_difference]

print(insurance_cost_difference)

names_insurance_cost_difference = zip(names, insurance_cost_difference)

list_names_insurance_cost_difference = list(names_insurance_cost_difference)

print("Here is the difference between the estimated and actual insurance cost for each individual: " + str(list_names_insurance_cost_difference))
