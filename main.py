class House:
    def __init__(self, price_per_kWh) -> None:
        self.price_per_kWh = price_per_kWh
        pass
    
    price_per_kWh: int
    
    avarage_kWh_per_day = 75
    avarage_free_space__square_meter = 150
    
    free_space__square_meter = 0
    energy_per_day_kWh = 0
    energy_per_year_kWh = 0 
    daily_cost = 0 
    yearly_cost = 0 
    
    def ask_user_energy(self): 
        result = input(f"* How much kWh energy your house use daily?\nThe avarage use is around {self.avarage_kWh_per_day}: ")
        if result.isdecimal():
            self.energy_per_day_kWh = int(result)
            self.energy_per_year_kWh = round(self.energy_per_day_kWh * 30 * 12, 3)
            self.daily_cost = round(self.energy_per_day_kWh * self.price_per_kWh, 3)
            self.yearly_cost = round(self.energy_per_year_kWh * self.price_per_kWh, 3)
        else:
            print("\n")
            print("* Wrong input, please select a number, no decimal.")
            self.ask_user_energy()
            
    def ask_user_space(self): 
        result = input(f"* How much square meter of free space you have?\nThe avarage free space is around {self.avarage_free_space__square_meter}: ")
        if result.isdecimal():
            self.free_space__square_meter = int(result)
        else:
            print("\n")
            print("* Wrong input, please select a number, no decimal.")
            self.ask_user_space()






class Solar_panel:
    def __init__(self, price_per_kWh: int, avarage_panal_size_square_meter: int, house_free_space_square_meter: int) -> None:
        self.price_per_kWh = price_per_kWh
    
        self.number_of_panals = house_free_space_square_meter / avarage_panal_size_square_meter
        
        pass
    
    number_of_panals: int
    price_per_kWh: int
    
    avarage_energy_per_day_kWh = 2
    avarage_cose_for_1_panal = 100
    avarage_batterie_cose = 4500
    
    batterie_cose = 0
    cose_for_1_panal = 0
    total_panal_cost = 0
    energy_per_day_kWh = 0 
    energy_per_year_kWh = 0 
    daily_saving = 0
    yearly_saving = 0
    
    
    def ask_user_energy(self): 
        result = input(f"* How much kWh energy the one soler panel provide daily?\nThe avarage providing is around {self.avarage_energy_per_day_kWh}: ")
        if result.isdecimal():
            self.energy_per_day_kWh = float(result)
            self.energy_per_year_kWh = round(self.energy_per_day_kWh * 30 * 12, 3)
            self.daily_saving = round(self.number_of_panals * self.energy_per_day_kWh * self.price_per_kWh, 3)
            self.yearly_saving = round(self.number_of_panals * self.energy_per_year_kWh * self.price_per_kWh, 3)
        else:
            print("\n")
            print("* Wrong input, please select a number, no decimal.")
            self.ask_user_energy()
            
    def ask_user_solar_panal_cost(self): 
        result = input(f"* What is the price in KWD for one solar panal?\nThe avarage price is around {self.avarage_cose_for_1_panal}: ")
        if result.isdecimal():
            self.cose_for_1_panal = int(result)
            self.total_panal_cost = self.cose_for_1_panal * self.number_of_panals
        else:
            print("\n")
            print("* Wrong input, please select a number, no decimal.")
            self.ask_user_solar_panal_cost()
            
    def ask_user_batterie_cost(self): 
        result = input(f"* What is the price in KWD of the batterie?\nThe avarage price is around {self.avarage_batterie_cose}: ")
        if result.isdecimal():
            self.batterie_cost = int(result)
        else:
            print("\n")
            print("* Wrong input, please select a number, no decimal.")
            self.ask_user_solar_panal_cost()

class Result:
    def __init__(self, house, solar_panel) -> None:
        self.house = house
        self.solar_panel = solar_panel
        pass
    house: House
    solar_panel: Solar_panel
    
    def show(self):
        print(f"+ * You can install {self.solar_panel.number_of_panals} panal based on your house free space.")
        print("+")
        print(f"+ * The total instalation cost is around {self.solar_panel.batterie_cose + self.solar_panel.total_panal_cost} KWD.")
        print("+")
        print(f"+ * Daily cose  : before {self.house.daily_cost} KWD, with soler panals you will saving: {round(self.solar_panel.daily_saving - self.house.daily_cost, 3)} KWD")
        print("+")
        print(f"+ * Yearly cose : before {self.house.yearly_cost} KWD, with soler panals you will saving: {round(self.solar_panel.yearly_saving- self.house.yearly_cost, 3)} KWD")
        print("+")
        print(f"+ * Your saving will pay off the solar panal instalation cost after {round((self.solar_panel.batterie_cose + self.solar_panel.total_panal_cost) / self.solar_panel.yearly_saving, 0)} years.")
        print("+")





price_per_kWh = 0.009

house       = House(price_per_kWh=price_per_kWh)
print("\n===============================\n")
house.ask_user_energy()
print("\n===============================\n")
house.ask_user_space()
print("\n===============================\n")

solar_panel = Solar_panel(price_per_kWh=price_per_kWh, avarage_panal_size_square_meter=2, house_free_space_square_meter=house.free_space__square_meter)
solar_panel.ask_user_energy()
print("\n===============================\n")
solar_panel.ask_user_solar_panal_cost()
print("\n===============================\n")
solar_panel.ask_user_batterie_cost()
print("\n+++  RESULT  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+")
result = Result(house, solar_panel)
result.show()
print("+")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
