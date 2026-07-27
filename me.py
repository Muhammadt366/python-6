class CSStudent:
    stream = 'cse'
    
    def __init__(self, roll):
        self.roll = roll

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

# Driver Code
add = CSStudent(101)
add.setAddress("Pak, taxila")
print(add.getAddress())
print(CSStudent.stream)  # prints "cse"