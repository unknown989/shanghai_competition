class Sensor:
    def __init__(self, name:str) -> None:
        self.name = name
        self.data = []
        self.is_active = False

    def read(self):
        pass

    def reload(self):
        pass
    
    def on(self):
        self.is_active = True

    def off(self):
        self.is_active = False

    def dump(self):
        return self.data
    
class IOThing:
    def __init__(self) -> None:
        pass

class Window:
    # The sensors used here in self.sensors idk what are they for so far, im just putting them there for future use (which idk what is it yet)
    def __init__(self) -> None:
        self.sensors = []
        self.is_closed = True
    
    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)
    

    
    def close(self) -> None:
        self.is_closed = True
    def open(self) -> None:
        self.is_closed = False

    def get_stat(self) -> bool:
        return self.is_closed

class Room:
    # The sensors used here in self.sensors usually means the sensor is inside the house and inside a room to be specific
    def __init__(self, type, width, height) -> None:
        self.type = type # closed or open which means whether the roof is open or not
        self.width = width
        self.height = height
        self.sensors = []
        self.windows = []
        
    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)

    def add_window(self, window:Window) -> None:
        self.windows.append(window)

class House:
    # The sensors used here in self.sensors usually means the sensor is outside the house
    def __init__(self, width, height,length) -> None:
        self.rooms = []
        self.width = width
        self.height = height
        self.length = length
        self.sensors = []

    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)

    
    def add_room(self, room: Room) -> None:
        self.rooms.append(room)


def main():
    # refer to here https://docs.google.com/document/d/16b-cCM2ZOKRPWepATTQWePb8dUBvRdrru5wfx9x4xdY/edit?usp=sharing
    # for the inner house diagram used here
    
    house = House(15,10,4) # in meters

    hall = Room("open",7,5)
    room_1 = Room("closed",3.5,10)
    room_2 = Room("closed",3.5,10)
    room_3 = Room("closed",7,2.5)
    room_4 = Room("closed",7,2.5)

    carbon_sensor = Sensor("Carbon Dioxide")
    room_1.add_sensor(carbon_sensor)

    wind_sensor = Sensor("Wind Direction Sensor")
    house.add_sensor(wind_sensor)

    light_n_sensor = Sensor("Light Sensor") # North
    light_w_sensor = Sensor("Light Sensor") # West
    light_e_sensor = Sensor("Light Sensor") # East
    light_s_sensor = Sensor("Light Sensor") # South
    house.add_sensor(light_n_sensor)
    house.add_sensor(light_w_sensor)
    house.add_sensor(light_e_sensor)
    house.add_sensor(light_s_sensor)

    noise_sensor_1 = Sensor("Noise Sensor")
    noise_sensor_2 = Sensor("Noise Sensor")
    noise_sensor_3 = Sensor("Noise Sensor")
    noise_sensor_4 = Sensor("Noise Sensor")
    noise_sensor_5 = Sensor("Noise Sensor")  
    hall.add_sensor(noise_sensor_1)
    room_1.add_sensor(noise_sensor_2)
    room_2.add_sensor(noise_sensor_3)
    room_3.add_sensor(noise_sensor_4)
    room_4.add_sensor(noise_sensor_5)


    temperature_sensor_1 = Sensor("Temperature Sensor")
    temperature_sensor_2 = Sensor("Temperature Sensor")
    temperature_sensor_3 = Sensor("Temperature Sensor")
    temperature_sensor_4 = Sensor("Temperature Sensor")
    temperature_sensor_5 = Sensor("Temperature Sensor")
    hall.add_sensor(temperature_sensor_1)
    room_1.add_sensor(temperature_sensor_2)
    room_2.add_sensor(temperature_sensor_3)
    room_3.add_sensor(temperature_sensor_4)
    room_4.add_sensor(temperature_sensor_5)


  
