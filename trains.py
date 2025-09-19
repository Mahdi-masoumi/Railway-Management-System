class Train:
    trains_list = []
    trains_names = []

    def __init__(self, name: str, train_line: str, avg_speed: float, delay: float, quality: float, ticket_price: float, capacity: int):
        self.name = name
        self.train_line = train_line
        self.avg_speed = avg_speed
        self.delay = delay
        self.quality = quality
        self.ticket_price = ticket_price
        self.capacity = capacity

    @classmethod
    def add_train(cls, name, train_line, avg_speed, delay, quality, ticket_price, capacity):
        if name in cls.trains_names:
            print(
                f"Train '{name}' already exists. Please choose a different name.")
            return
        new_train = Train(name, train_line, avg_speed, delay,
                          quality, ticket_price, capacity)
        cls.trains_list.append(new_train)
        cls.trains_names.append(name)
        print(f"Train '{name}' added successfully.")

    @classmethod
    def delete_train(cls, name):
        for t in cls.trains_list:
            if t.name == name:
                cls.trains_list.remove(t)
                cls.trains_names.remove(name)
                print(f"Train {name} deleted.")
                return
            print(f"No train named '{name}' found.")

    @classmethod
    def view_trains(cls):
        if not cls.trains_list:
            print("No trains.")
            return
        for t in cls.trains_list:
            # option 1
            # for k, v in vars(t).items():
            #     print(f"{k}: {v}")
            # option 2
            print(
                f"{t.name} | line: {t.train_line} | cap: {t.capacity} | price: {t.ticket_price}")

    # TODO: implement update_train method


Train.add_train("Express 1", "Line A", 80.0, 5.0, 4.5, 50.0, 200)
Train.add_train("Express 2", "Line A", 80.0, 5.0, 4.5, 50.0, 200)
Train.add_train("Express 3", "Line A", 80.0, 5.0, 4.5, 50.0, 200)
Train.add_train("Express 4", "Line A", 80.0, 5.0, 4.5, 50.0, 200)
Train.view_trains()
Train.delete_train("Express 1")
Train.view_trains()
