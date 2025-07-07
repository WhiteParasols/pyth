from driver import Driver
from car import Car

driver=Driver('Bob',40,'1종보통')
driver.drive(30)
car=Car('tesla','model s')
driver.assign_car(car)

driver.drive(40)
driver.drive(100)

car.update_odometer(100)
car.update_odometer(200) #올리는건 가능
car.read_odometer()

car2=Car('Hyundai','k5')
driver2=Driver('david',30,'2종보통',car2)
driver2.drive(500)