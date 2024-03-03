# Creates a function to convert celsius to kelvin
def celsius_to_kelvin(temp):
      return temp + 273.15  
  
# Creates a function to convert kelvin to Celsius
def kelvin_to_celsius(temp):
      return temp-273.15  

try:
 temp = float(input('Enter the temperature:'))
 units_of_measurement=input('''What are the units of measurement?
                              Select the appropriate number below:
                              1.Degrees Celsius
                              2.Kelvin
                              ''')
 if units_of_measurement== '1':
    result=celsius_to_kelvin(temp)
 else:
    result=kelvin_to_celsius(temp)    
 print(f'Your Temperature converted is:{result}')
except Exception as e:
    print('Please enter a valid input')