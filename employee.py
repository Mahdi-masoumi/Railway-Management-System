class Employee:
    trains_list = []
    lines = {}

    def __init__(self):
        pass

        # Line Methods
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
                    print(
                        f"Station '{station.strip()}' is invalid. Stations must only contain letters.")
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
            print(
                f"{name}: {info['start']} -> {info['stop']} | Stations: {stations_str}")

    # Train Methods
    def add_train(self, name: str, train_line: str, avg_speed: float, delay: float, quality: float, ticket_price: float, capacity: int):
        if any(train['name'] == name for train in self.trains_list):
            print(f"Train with name {name} already exists.")
            return
        train = {
            "name": name,
            "train_line": train_line,
            "avg_speed": avg_speed,
            "delay": delay,
            "quality": quality,
            "ticket_price": ticket_price,
            "capacity": capacity
        }
        self.trains_list.append(train)
        print(f"Train {name} added successfully.")

    def view_trains(self):
        for train in self.trains_list:
            print(f"train name: {train['name']} | train line: {train['train_line']} | average speed: {train['avg_speed']} | delay: {train['delay']} | quality: {train['quality']} | ticket price: {train['ticket_price']} | capacity: {train['capacity']}")

    def update_train(self, name: str, **kwargs):
        for train in self.trains_list:
            if train['name'] == name:
                for key, value in kwargs.items():
                    if key not in train:
                        print(f"Invalid attribute: {key}")
                        return
                    train[key] = value
                print(f"Train {name} updated successfully.")
                return
        print(f"Train with name {name} not found.")

    def remove_train(self, name: str):
        for i, train in enumerate(self.trains_list):
            if train['name'] == name:
                del self.trains_list[i]
                print(f"Train {name} removed successfully.")
                return
        print(f"Train with name {name} not found.")
