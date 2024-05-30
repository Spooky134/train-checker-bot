


class Train:
    def __init__(self, date=None, number=None, train_route=None, train_type=None, city_from=None, city_to=None,
                 departure=None, arrival=None, travel_time=None, places=None, link=None):
        self.date = date
        self.number = number
        self.train_route = train_route
        self.train_type = train_type
        self.city_from = city_from
        self.city_to = city_to
        self.departure = departure
        self.arrival = arrival
        self.travel_time = travel_time
        self.places = places
        self.link = link

    def get_place_info(self, place_type):
        return place_type + self.places[place_type]

    def get_all_place_info(self):
        items = []
        for key in self.places:
            items.append(self.get_place_info(key))
        return items

    def get_text(self):
        string = f'{self.number}\n{self.train_type}\n{self.city_from}\n{self.city_to}\n{self.departure}\n' \
                 f'{self.arrival}\n{self.travel_time}'
        return string