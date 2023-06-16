from    dataclasses import  dataclass
from utilities import *
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
    allEvents   =   {}

    __slots__ = ["station", "direction", "scheduledTime", "actualTime", "passengersOn",
                 "passengersOff", "eVehicles", "operatingTime"]

    def __init__(self, station: str, direction: str, scheduledTime: datetime,
                 actualTime: datetime, passengersOn: int, passengersOff: int):

        self.station:       str             =   station
        self.direction:     str             =   direction
        self.passengersOn:  int             =   passengersOn
        self.passengersOff: int             =   passengersOff
        self.eVehicles:     List[eVehicle]  =   []

    # Checks if the instance is an arrival
    def isArrival(self):
        if self.direction == "Til":
            return True
        return False

    # Check if the instance is a departure
    def isDeparture(self):
        if self.isArrival():
            return False
        return True

    # Formats the timestamp into a datetime object if it were not allready
    @stringToDatetime
    def __formatTime(self):

        time = self.actualTime

        if isinstance(time, datetime.__class__):
            pass
        elif int(time[:2]) >= 24:
            return datetime()


    # Returns how many eVehicles can be assigned an instance based on how many passengers got on or off
    def __passengers_vs_eVehicles(self, nr_eVehicles: int):

        for eVehicle in range(1, nr_eVehicles + 1):

            if 0 < eVehicle <= self.passengersOn and self.passengersOn != 0:
                return eVehicle - 1

    # Returns a dictionary with all class instances that are arrivals in between two dates
    @classmethod
    def arrivalsFromTo(cls, startDate: datetime.date, endDate: datetime.date):

        filteredArrivals = {}

        for date in cls.arrivals.keys():

            if startDate <= date <= endDate:

                filteredArrivals[date] = cls.arrivals[date]

        return filteredArrivals

    # Returns a dictionary with all class instances that are departures in between two dates
    @classmethod
    def departuresFromTo(cls, startDate: datetime.date, endDate: datetime.date):

        filteredDepartures = {}

        for date in cls.departures.keys():

            if startDate <= date <= endDate:
                filteredDepartures[date] = cls.departures[date]

        return filteredDepartures

    # Returns a dictionary with all class instances in between two dates
    @classmethod
    def FromTo(cls, startDate: datetime.date, endDate: datetime.date):

        filteredEvents = {}

        for date in cls.allEvents.keys():

            if startDate <= date <= endDate:

                filteredEvents[date] = cls.allEvents[date]

        return filteredEvents

    # Deletes the class variables. Used only when a new dataset is loaded
    @classmethod
    def resetClassVariables(cls):

        cls.arrivals    =   {}
        cls.departures  =   {}

    # If comparing a SubwayEvent to a eVehicle it will check if the eVehicle can be counted as relevant to that SubwayEvent
    def __eq__(self, other):
        if type(other) == eVehicle:



