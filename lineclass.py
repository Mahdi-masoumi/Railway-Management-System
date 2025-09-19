class Line:
    def __init__(self, name, start, stop, stations):
        self.name = name
        self.start = start
        self.stop = stop
        self.stations = stations

class Line_Manager:
    def __init__(self):
        self.lines = {}

    def add_line (self, name, start, stop, stations):
        if name in self.lines:
            print("Line Already Exists") 
        else:
            self.lines[name] = Line(name, start, stop, stations)
            print(f"Line {name} added successfully.")

    def update_line (self, name, new_start=None, new_stop=None, new_stations=None):
        if name not in self.lines:
            print("Line Not Found") 
            return
        line = self.lines[name]
        if new_start:
            line.start = new_start
        if new_stop:
            line.stop = new_stop
        if new_stations:
            line.stations = new_stations
        print(f"Line {name} updated successfully.")

    def delete_line (self, name):
        if name in self.line:
            del self.lines[name]
            print(f"Line {name} deleted successfully.")
        else:
             print("Line not found!")

    def list_lines (self,):
        if not self.line:
            print("No lines available.")
            return
        for line in self.lines.values():
            print(f"- {line.name}: {line.start} -> {line.stop} | Stations: {', '.join(line.stations)}")