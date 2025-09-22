class Employee:
    def __init__(self):
        self.lines = {}
#Line Methods
        
    def add_line(self, name, start, stop, stations):
        if not name or not start or not stop:
            print("Name, start, and stop cannot be empty.")
            return
        if not start.replace(" ", "").isalpha() or not stop.replace(" ", "").isalpha():
            print("start and stop must only contain letters.")
            return
        if not isinstance(stations, str):
            print("Stations must be a single string (e.g. 'Tehran,Qom,Isfahan').")
            return
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
            if not new_start.replace(" ", "").isalpha():
                print("Start must only contain letters.")
                return
            self.lines[name]["start"] = new_start

        if new_stop:
            if not new_stop.replace(" ", "").isalpha():
                print("Stop must only contain letters.")
                return
            self.lines[name]["stop"] = new_stop

        if new_stations:
            if not isinstance(new_stations, str):
                print("Stations must be a single string (e.g. 'Tehran,Qom,Isfahan').")
                return
            for station in new_stations.split(","):
                if not station.strip().replace(" ", "").isalpha():
                    print(f"Station '{station.strip()}' is invalid. Stations must only contain letters.")
                    return
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
            stations_str = info['stations'].replace(",", "-").split(",")
            print(f"{name}: {info['start']} -> {info['stop']} | Stations: {stations_str}")