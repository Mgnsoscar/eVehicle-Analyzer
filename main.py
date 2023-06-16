from    dataclasses import  dataclass
from    datetime    import  datetime
from    typing      import  List
import  pandas      as      pd
@dataclass
class eVehicle:

    type:       str
    start:      datetime
    stop:       datetime
    duration:   datetime
    newUser:    bool
    toStation:  bool

class SubwayEvent:

    arrivals    =   {}
    departures  =   {}

    __slots__ = ["station", "direction", "scheduledTime", "actualTime", "passengersOn",
                 "passengersOff", "eVehicles", "operatingTime"]

    def __init__(self, station: str, direction: str, scheduledTime: datetime,
                 actualTime: datetime, passengersOn: int, passengersOff: int):

        self.station:       str             =   station
        self.direction:     str             =   direction
        self.passengersOn:  int             =   passengersOn
        self.passengersOff: int             =   passengersOff
        self.eVehicles:     List[eVehicle]  =   []

        if self.isArrival():
            SubwayEvent.arrivals[self.actualTime]

    # Checks if the SubwayEvent is a departure or an arrival
    def isArrival(self):
        if self.direction == "Til":
            return True
        return False

    def isDeparture(self):
        if self.isArrival():
            return False
        return True

    # Checks if how many passengers are boarding the subway vs how many eVehicles were
    def passengers_vs_eVehicles(self, nr_eVehicles: int):

        for eVehicle in range(1, nr_eVehicles + 1):

            if 0 < eVehicle <= self.passengersOn and self.passengersOn != 0:
                return eVehicle - 1

    @classmethod
    def arrivalsFromTo(cls, startDate: datetime.date, endDate: datetime.date):

        filteredArrivals = {}

        for date in cls.arrivals.keys():

            if startDate <= date <= endDate:

                filteredArrivals[date] = cls.arrivals[date]

        return filteredArrivals

    @classmethod
    def departuresFromTo(cls, startDate: datetime.date, endDate: datetime.date):

        filteredDepartures = {}

        for date in cls.departures.keys():

            if startDate <= date <= endDate:
                filteredDepartures[date] = cls.departures[date]

        return filteredDepartures

    # Deletes the class variables. Used only when a new dataset is loaded
    @classmethod
    def resetClass(cls):

        cls.arrivals    =   {}
        cls.departures  =   {}

    # If comparing a SubwayEvent to a eVehicle it will check if the eVehicle can be counted as relevant to that SubwayEvent
    def __eq__(self, other):
        if type(other) == eVehicle:



