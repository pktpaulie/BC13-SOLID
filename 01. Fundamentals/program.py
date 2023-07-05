from abc import ABC, abstractmethod


class User:
    """class to demonstrate singleton pattern"""
    __instance = None

    @staticmethod
    def login(username, password):
        """get the current instance of the class"""
        if User.__instance is None:
            return User(username, password)
        return User.__instance

    def __init__(self, username: str, password: str):
        """ initialise/ set the instance itself"""
        if User.__instance is None:
            User.__instance = self
            self.username = username
            self.password = password
        else:
            raise Exception("User logged in") #prevent creation of multiple objects
        
    @staticmethod
    def logout():
        """log out/ end session for current instance"""
        User.__instance = None

    def set_username(self, username: str):
        """set username"""
        self.username = username

    def set_password(self, password: str):
        """set the password"""
        self.password = password

    def get_username(self):
        """return the username"""
        return User.__instance.username # updated the getter for username
    
    def get_password(self):
        """return the username"""
        return User.__instance.password # updated the getter for username


class InputDevice(ABC):
    @abstractmethod
    def input(self, data):
        pass


class Keyboard(InputDevice):
    def input(self, data):
        print("------- Inputing data from keyboard ------------------")
        print("Step1: Listen to data from keyboard")
        print("Step2: Pick data from Keyboard")
        print("Step3: Locate current cursor position")
        print("Step4: Place data in the current cursor position")
        print("Step5: Start Listening to data from keyboard")
        print("")  # Empty Print statement at end of every method


class Mouse(InputDevice):
    def input(self, data):
        print("------- Inputing data from mouse ------------------")
        print("Step1: Listen to data from mouse")
        print("Step2: Pick data from mouse")
        print("Step3: Locate current cursor position")
        print("Step4: Place data in the current cursor position")
        print("Step5: Start Listening to data from mouse")
        print("")  # Empty Print statement at end of every method


class TouchScreen(InputDevice):
    def input(self, data):
        print("------- Input Process using Screen Touch ----------")
        print("Step1: Listen to data from Screen")
        print("Step2: Pick data from Screen")
        print("Step3: Locate current tourch position")
        print("Step4: Place data in the current tourch position")
        print("Step5: Start Listening to data from Screen")
        print("")  # Empty Print statement at end of every method


class ProcessorChip(ABC):
    @abstractmethod
    def process(self, data):
        pass


class Intel(ProcessorChip):
    def process(self, data):
        print("------ Processing using Intel Chip ---------------")
        print("")  


class AMD(ProcessorChip):
    def process(self, data):
        print("------ Processing using AMD Chip ------------------")
        print("")  


class Nvidia(ProcessorChip):
    def process(self, data):
        print("------- Processing using Nvidia ------------------\n")


class Memory(ABC):
    @abstractmethod
    def store(self, data):
        pass


class SSD(Memory):
    def store(self, data):
        print("------------Storing data on SSD------------------\n")


class InternalMemory(Memory):
    def store(self, data):
        print("-------------- Storage Process ------------------")
        print("Step1: Receive data to be stored")
        print("Step2: Open Internal memory where data is to stored")
        print("Step3: Prepare for data storage operation")
        print("Step4: Launch storage operation")
        print("Step5: Send back signal representing the state of the storage operation")
        print("")  


class OutputDevice(ABC):
    @abstractmethod
    def output(self, data):
        pass


class Monitor(OutputDevice):
    def output(self, data):
        print("----------- Outputing to Monitor ----------------")
        print("Step1: Receive data to be output")
        print("Step2: Open monitor where data is to displayed")
        print("Step3: Prepare for data output operation")
        print("Step4: Launch output operation")
        print("Step5: Send back signal representing the state of the output operation")
        print("")


class Projector(OutputDevice):
    def output(self, data):
        print("---------- Outputing to Projector ----------------")
        print("Step1: Receive data to be output")
        print("Step2: Open projector where data is to displayed")
        print("Step3: Prepare for data output operation")
        print("Step4: Launch output operation")
        print("Step5: Send back signal representing the state of the output operation")
        print("")


class Computer(ABC):
    def __init__(self, input_device, processor_chip, memory, output_device, user:User):
        # Fields
        self.brand = ""
        self.model = ""
        self.user = user
        self.price = 0
        self.input_device = input_device
        self.processor_chip = processor_chip
        self.memory = memory
        self.output_device = output_device

    #setters
    def set_input(self, input_device:str):
        self.input_device = input_device

    def set_processor_chip(self, processor_chip):
        self.processor_chip = processor_chip

    def set_memory(self, memory):
        self.memory = memory

    def set_output_device(self, output_device):
        self.output_device = output_device   

    #getters
    def get_input(self):
        return self.input_device

    def get_processor_chip(self):
        return self.processor_chip
    
    def get_memory(self):
        return self.memory
    
    def get_output_device(self):
        return self.output_device


    # Methods
    def input(self, data):
        self.input_device.input(data)

    def process(self, data):
        self.processor_chip.process(data)  # delegation of one method to another

    def store(self, data):
        self.memory.store(data)

    def output(self, data):
        self.output_device.output(data)

    # User Methods        
    def set_user(self, user):
        """ set the user"""
        self.user = user
    
    def get_user(self):
        """ return the user"""
        return self.user
        #return self.user.get_password , self.user.get_password
    
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_price(self, price):
        self.price = price

    @abstractmethod
    def get_price(self):
        pass

# Decorator Design Pattern
class AccessoryDecorator(Computer):
    """Accessory Decorator"""
    def __init__(self, computer:Computer):
        self.computer = computer

    def get_price(self):
        return self.computer.get_price()

    def get_name(self):
        return self.computer.get_name()
 
class HDMIDecorator(Computer):
    """Wireless Wrapper/Decorator Class"""
    def __init__(self, computer:Computer):
        self.computer = computer

    def set_price(self, price):
        self.price = self.computer.price + price

    def get_price(self):
        #print(f"Price: {self.computer.get_price() + 90000}")
        return self.computer.get_price() + 90000

    def get_name(self):
        #print(f"HDMI Enabled {self.computer.get_name()}")
        return "HDMI Enabled " + self.computer.get_name()
    
class TypeCDecorator(Computer):
    """Wireless Wrapper/Decorator Class"""
    def __init__(self, computer:Computer):
        self.computer = computer

    def get_price(self):
        #print(f"Price: {self.computer.get_price() + 100000}")
        return self.computer.get_price() + 100000
    
    def set_price(self, price):
        self.price = self.computer.price + price

    def get_name(self):
        #print(f"TypeC Enabled {self.computer.get_name()}")
        return "TypeC Enabled " + self.computer.get_name()

class BacklightDecorator(Computer):
    """ Backlight Decorator Feature Wrapper/Decorator Class"""
    def __init__(self, computer:Computer):
        self.computer = computer
 
    def get_price(self):
        price = 0
        price = self.computer.get_price()
        price = price + 250000
        #print(f"Price: {price}")
        return self.computer.get_price() + 250000
    
    def set_price(self, price):
        self.price = self.computer.price + price

    def get_name(self):
        #print(f"Backlit {self.computer.get_name()}")
        return "Backlit" + self.computer.get_name()


# Inheritance: Desktop is inheriting from Computer
class Desktop(Computer):
    # Fields
    pass
    # Methods
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return 3000000
    
    def get_name(self):
        return "Desktop \n"

# Inheritance: Laptop is inheriting from Computer
class Laptop(Computer):
    # Fields
    pass

    # Methods
    def fold(self):
        print("-----------Folding Process ----------")
        print("Step1: Folding")
        print("")
    
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return 2000000
    
    def get_name(self):
        return "Laptop \n"

# Inheritance: Walltop is inheriting from Computer
class Walltop(Computer):
    # Fields
    # = 1500000
    def set_price(self, new_price):
        self.price = new_price
        
    def get_price(self):
        return 1500000
    
    def get_name(self):
        return "Walltop \n"


computer = Desktop(Keyboard(), Nvidia(), InternalMemory(), Projector(),User.login("Franco", "123"))
print(computer.user.get_username(), computer.user.get_password())
computer.set_input(TouchScreen())
computer.input("blah")
computer.set_memory(SSD())
computer.process("see")
computer.store("1")
computer.output("12")
computer.user.logout() # logout first user

# Using decorator pattern
desktop_with_hdmi = HDMIDecorator(computer)
print(desktop_with_hdmi.get_name())
print(desktop_with_hdmi.get_price())

computer = Laptop(Mouse(), AMD(), SSD(), Projector(),User.login("Pauline", "pkt"))
print(computer.user.get_username(), computer.user.get_password())
computer.input("soo")
computer.process("ts")
computer.store("2")
computer.set_output_device(Monitor())
computer.output("12")
#computer.user.logout() # logout second user

# Using decorator pattern
laptop_with_backlight = BacklightDecorator(computer)
print(laptop_with_backlight.get_name())
print(laptop_with_backlight.get_price())


computer = Walltop(Keyboard(), Intel(), SSD(), Monitor(), User.login("Oliver", "pasd"))
print(computer.user.get_username(), computer.user.get_password())
computer.set_processor_chip(Nvidia())
computer.process("s")
computer.set_memory(InternalMemory())
computer.store("3")
computer.set_input(TouchScreen())
computer.input("simsim")
computer.output("abs")

# Using decorator pattern
walltop_with_typeC =  TypeCDecorator(computer)
print(walltop_with_typeC.get_name())
print(walltop_with_typeC.get_price())
walltop_with_typeC.set_price(2000000)
print(walltop_with_typeC.get_price()) # returns old value


# my_laptop = Laptop()
# my_laptop.input()
# my_laptop.process(12, "hop")
# my_laptop.store("one")
# my_laptop.output()
# my_laptop.fold()
