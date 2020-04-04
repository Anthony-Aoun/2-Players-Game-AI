class Device:
	#Electronic devices class
	def __init__(self,brand,model,price):
		self.brand = brand
		self.model = model
		self.price = price

class PC(Device):
	#PC class
	def __init__(self,brand,model,price,CPU,RAM):
		super().__init__(brand,model,price)
		self.CPU = CPU
		self.RAM = RAM

	def specs(self):
		print("Brand : ",self.brand)
		print("Model : ",self.model)
		print("Price : ",self.price,"$")
		print("CPU : ",self.CPU)
		print("RAM : ",self.RAM)

	def discount(self,percentage):
		new_price = self.price - (percentage*self.price)/100
		print("The price went from ",self.price,"$ to ",new_price,"$ !")
		self.price = new_price

class Mobile(Device):
	#Mobile Phone class
	def __init__(self,brand,model,price,battery_percentage,password):
		super().__init__(brand,model,price)
		self.battery_percentage = battery_percentage
		self.__password = password

	def get_password(self):
		return self.__password

	def recharge_battery(self,added_percentage):
		self.battery_percentage += added_percentage
		print("The phone's battery is now : ",self.battery_percentage,"%")


if __name__ == '__main__':
	#This code runs when the file is executed
	my_computer = PC('Lenovo','E570',1000.0,'intel i7','20 GB')
	my_phone = Mobile('iPhone','6S+',600.0,74,'1234')
	print()
	print("**************** PC ****************")
	print("The specs are : ")
	my_computer.specs()
	print()
	print("After a discount of 10% : ")
	my_computer.discount(10)
	print()
	print("**************** MOBILE ****************")
	print("The phone's password is : ",my_phone.get_password())
	print()
	print("We add 25% to the phone battery life...")
	my_phone.recharge_battery(25)






