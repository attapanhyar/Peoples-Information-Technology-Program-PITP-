# def KelvinToFahrenheit(Temperature):
#     assert (Temperature >= 0),"Colder than absolute zero!"
#     return ((Temperature-273)*1.8)+32
# print (KelvinToFahrenheit(273))
# print (int(KelvinToFahrenheit(505.78)))
# print (KelvinToFahrenheit(-5))

input1 = input("Enter a number: ")

if input1.isdigit():
    input1 = int(input1)
    assert (input1>0),"The number is not positive!"
    print("The number is positive.")