
def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
details(name="John", age=30, city="New York")
details(location="Pakistan", ph="0300", prov = "Sindh", district="Sangarh")