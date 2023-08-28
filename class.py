

class Driver:
    def __init__ (self, first_name, last_name , driving_license_no , phone_no, city):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license = driving_license_no
        self.phone_no = phone_no
        self.city = city
        
        self.nickname = ""
        self.availability = False
        self.location = None
        
        
    def add_nickname(self, value):
        self.nickname = value
        
    def accept_ride_request(self):
        pass
    
    
    def show_earnings(self):
        pass
    
    def change_availability(self):
        pass
        
    
    
        


driver1 = Driver("Abdul", "Hamza", "abcd1234", "0181111111", "Dhaka")
driver2 = Driver("James", "Morshed", "xyz0987", "01711111111", "Rajshahi")


print(driver1.nickname)

driver1.add_nickname("Hamza Mia")

print(driver1.nickname)

# print(driver2.first_name)
# print(driver2.last_name)