class Celsius:
    def __init__(self):
        pass

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius()
c.temperature = -30
print(c.temperature)
c.to_fahrenheit = 30
print(c.to_fahrenheit)

# 출처: https://hamait.tistory.com/827 [HAMA 블로그]