class Employee:

    trains_list = []
    lines = {}

    def __init__(self):
        pass

    def employee_panel(self):
        print("Welcome to the employee panel!\n enter where you wanna go:\n 1.add line\n 2.edit line\n 3.delete line\n 4.show lines\n 5.add train\n 6.edit train\n 7.delete train\n 8.show trains\n 9.exit")
        choice = input("Enter your choice (1-9): ")
        if choice not in [str(i) for i in range(1, 10)]:
            print("Invalid choice. Please enter a number between 1 and 9.")
            self.employee_panel()
            return
        if choice == "1":
            line_name = input("Enter unique line name: ")
            start_station = input("Enter start station: ")
            stop_station = input("Enter stop station: ")
            stations = input("Enter stations (comma-separated): ")
            self.add_line(line_name, start_station, stop_station, stations)
            self.employee_panel()
        elif choice == "2":
            line_name_to_update = input("Enter the line name to update: ")
            new_start = input("Enter the start point to update: ")
            new_end = input("Enter the end point to update: ")
            stations = input(
                "Enter the stations to update (comma-separated): ")
            self.update_line(line_name_to_update, new_start, new_end, stations)
            self.employee_panel()
        elif choice == "3":
            line_name_to_delete = input("Enter the line name to delete: ")
            self.delete_line(line_name_to_delete)
            self.employee_panel()
        elif choice == "4":
            self.view_lines()
            self.employee_panel()
        elif choice == "5":
            train_name = input("Enter train name: ")
            train_line = input("Enter train line: ")
            avg_speed = input("Enter average speed: ")
            delay = input("Enter delay: ")
            quality = input("Enter quality (1-5): ")
            ticket_price = input("Enter ticket price: ")
            capacity = input("Enter capacity: ")
            self.add_train(train_name, train_line, avg_speed,
                           delay, quality, ticket_price, capacity)
            self.employee_panel()
        elif choice == "6":
            train_name_to_update = input(
                "enter name of the train you wanna update: ")
            kwargs = input(
                "enter the data you would like to update(e.g. avg_speed=90): ")
            self.update_train(train_name_to_update, kwargs=kwargs)
            self.employee_panel()
        elif choice == "7":
            train_to_remove = input(
                "enter the name of the train you'd like to remove: ")
            self.remove_train(train_to_remove)
            self.employee_panel()
        elif choice == "8":
            self.view_trains()
            self.employee_panel()
    # TODO: choice == "9" ? => Exit to main panel

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

    def view_lines(self):
        if not self.lines:
            print("No lines available.")
            return
        for name, info in self.lines.items():
            stations_str = info['stations'].replace(",", "-").split(",")
            print(
                f"{name}: {info['start']} -> {info['stop']} | Stations: {stations_str}")

    # Train Methods
    def add_train(self, name: str, train_line: str, avg_speed: float, delay: float, quality: float, ticket_price: float, capacity):
        if any(train['name'] == name for train in self.trains_list):
            print(f"Train with name {name} already exists.")
            return
        if not avg_speed or not isinstance(avg_speed, float) or avg_speed <= 0:
            print(
                "average speed is not valid! enter a float greater than or equal to 0")
            return
        if not delay or not isinstance(delay, float) or delay < 0:
            print(
                "delay amount is not valid! enter a float greater than or equal to 0")
            return
        if not quality or isinstance(quality, float) or not (1 <= quality <= 5):
            print(
                "quality amount is not valid! enter a float gte 0 and lte 5")
            return
        if not ticket_price or isinstance(ticket_price, float) or ticket_price < 0:
            print(
                "ticket price is not valid! enter a float gte 0")
            return
        if not capacity or isinstance(capacity, int) or capacity <= 0:
            print(
                "capacity amount is not valid! enter a integer gt 0")
            return
        train = {
            "name": name,
            "train_line": train_line,
            "avg_speed": float(avg_speed),
            "delay": float(delay),
            "quality": float(quality),
            "ticket_price": float(ticket_price),
            "capacity": int(capacity)
        }
        self.trains_list.append(train)
        print(f"Train {name} added successfully.")

    def update_train(self, name: str, **kwargs):
        for train in self.trains_list:
            if train['name'] == name:
                train.update({k: v for k, v in kwargs.items() if k in train})
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

    def view_trains(self):
        for train in self.trains_list:
            print(f"train name: {train['name']} | train line: {train['train_line']} | average speed: {train['avg_speed']} | delay: {train['delay']} | quality: {train['quality']} | ticket price: {train['ticket_price']} | capacity: {train['capacity']}")


# Employee().employee_panel()
# Employee().add_train("Express 101", "North Line", 80.0, 5.0, 4, 500, 200)
