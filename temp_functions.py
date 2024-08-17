"""The temp_functions script contains two functions that perform actions on the incoming value 
temperatures:

Function fahr_to_celsius - converts temperature from Fahrenheit to Celsius. 
The temperature at the entrance is in Fahrenheit. The result of the function will be the temperature in 
degrees Celsius.

The temp_classifier function classifies temperatures in Celsius into integer values.
The input temperature is in Celsius. The result of the function will be a class from 0 to 3, 
to which this temperature belongs according to the classification criteria.

"""


def fahr_to_celsius(temp_fahrenheit):
    """Function to convert temperature from Fahrenheit to Celsius

    The function fahr_to_celsius converts the input temperature from 
    degrees Fahrenheit to degrees Celsius.
    """
    converted_temp = (temp_fahrenheit - 32)/1.8
    return converted_temp



def temp_classifier(temp_celsius):
    
    """Function to classify temperature in Celsius into integer values ​​0-3

    The temp_classifier function, based on specified criteria, classifies the temperature into 
    Celsius in integer values ​​0-3, returning the value of the class it belongs to
    temperature input value.

    Classification criteria:
    class 0 - temperature below -2 degrees Celsius
    class 1 - temperature equal to or warmer than -2, but less than +2 degrees Celsius
    class 2 - temperature equal to or warmer than +2, but less than +15 degrees Celsius
	class 3 - temperature equal to or warmer than +15 degrees Celsius
    """
    
    if temp_celsius < -2:
        classifier = 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        classifier = 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        classifier = 2
    else: classifier = 3
    return classifier
