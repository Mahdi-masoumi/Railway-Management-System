class Employee:
    def __init__(self):
        self.lines = {}
#Line Methods
        
    def add_line(self, name, start, stop, stations):
        if name in self.lines:
            print(f"Line '{name}' already exists.")
            return
        self.lines[name] = {
            "start": start,
            "stop": stop,
            "stations": stations
        }
        print(f"line '{name}' added.")


    def update_line(self, name, new_start=None, new_stop=None, new_stations=None):
        if name not in self.lines:
            print(f"Line '{name}' not found.")
            return
        if new_start:
            self.lines[name]["start"] = new_start
        if new_stop:
            self.lines[name]["stop"] = new_stop
        if new_stations:
            self.lines[name]["stations"] = new_stations
        print(f"Line '{name}' updated.")


    def delete_line(self, name):
        if name not in self.lines:
            print(f"Line'{name}' not found.")
            return
        del self.lines[name]
        print(f"Line '{name}' deleted.")


    def line_list(self):
        if not self.lines:
            print("Line was not available") 
            return
        for name, info in self.lines.items():
            print(f"{name}: {info['start']} -> {info['stop']} | Stations: {', '.join(info['stations'])}")