def add_train(self, name: str, train_line: str, avg_speed: float, delay: float,
              quality: float, ticket_price: float, capacity,
              distance: float, start_time: str, stop_time: float):
    if any(train['name'] == name for train in self.trains_list):
        print(f"Train with name {name} already exists.")
        return

    try:
        avg_speed = float(avg_speed)
        delay = float(delay)
        quality = float(quality)
        ticket_price = float(ticket_price)
        capacity = int(capacity)
        distance = float(distance)
        stop_time = float(stop_time)
    except ValueError:
        print("Invalid numeric value for train attributes.")
        return

    try:
        start_dt = datetime.strptime(start_time, "%H:%M")
    except ValueError:
        print("Start time must be in HH:MM format (e.g. 08:05).")
        return

    travel_minutes = (distance / avg_speed) * 60
    arrival_dt = start_dt + timedelta(minutes=travel_minutes + delay)
    departure_dt = arrival_dt + timedelta(minutes=stop_time)

    for train in self.trains_list:
        if train["train_line"] == train_line:
            if "arrival" in train and "departure" in train:
                other_arrival = train["arrival"]
                other_departure = train["departure"]

                if arrival_dt <= other_departure and departure_dt >= other_arrival:
                    print(f"Collision detected with train {train['name']}! Cannot add this train.")
                    return

    train = {
        "name": name,
        "train_line": train_line,
        "avg_speed": avg_speed,
        "delay": delay,
        "quality": quality,
        "ticket_price": ticket_price,
        "capacity": capacity,
        "distance": distance,
        "start_time": start_time,
        "stop_time": stop_time,
        "arrival": arrival_dt,
        "departure": departure_dt
    }
    self.trains_list.append(train)
    print(f"Train {name} added successfully.")
