# Base class
class SmartDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._battery_level = 100  # Encapsulated attribute

    def show_info(self):
        return f"{self.brand} {self.model} - Battery: {self._battery_level}%"

    def charge(self):
        self._battery_level = 100
        print("🔋 Device fully charged.")

    def use_battery(self, amount):
        self._battery_level = max(0, self._battery_level - amount)
        print(f"⚡ Used {amount}% battery. Remaining: {self._battery_level}%")

# Child class
class Smartphone(SmartDevice):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
        self.installed_apps = []

    def show_info(self):
        # Polymorphism: overriding base method
        info = super().show_info()
        return f"{info} | OS: {self.os} | Storage: {self.storage}GB"

    def install_app(self, app_name):
        if self.storage > 0:
            self.installed_apps.append(app_name)
            self.storage -= 1  # simple simulation
            print(f"📱 Installed {app_name}. Remaining storage: {self.storage}GB")
        else:
            print("❌ Not enough storage to install new app.")

# Example usage
my_phone = Smartphone("Apple", "iPhone 14", "iOS", 5)
print(my_phone.show_info())
my_phone.install_app("Instagram")
my_phone.install_app("Spotify")
my_phone.use_battery(30)
my_phone.charge()
print(my_phone.show_info())
