#Bomi Oladimeji
#3164447
#CMPT-200-X04L
#Assignment2
#Collaborators: Lab instructor and https://stackoverflow.com/questions/73955513/python3-datetime-function-clarification-on-days-meaning
from datetime import date, datetime, timedelta
class AirLine:
    def __init__(self, name = 'Airalgorithmia', fleet = [], staff = [], trips = []):
        """
        purpose: Initialize a new instance with a name, fleet, staff, and trips.
        parameters: 
            name: The name of the organization (default 'Airalgorithmia').
            fleet: A list of vehicles or aircraft (default empty list).
            staff: A list of employees (default empty list).
            trips: A list of scheduled journeys (default empty list).
        throws: 
            TypeError: If name is not a string, or if fleet, staff, or trips are not lists.
            ValueError: If name is an empty string.
        pre: None.
        post: Object is initialized with valid name, fleet, staff, and trips.
        returns: None.
        """
        
        
        if not isinstance(name, str):
            raise TypeError('Must be a string')
        elif name == '':
            raise ValueError('Name cannot be empty')
        else:
            self.name = name
        
        
        
        if type(staff) != list:
            raise TypeError('Staff must be a list')
        else:
            self.staff = staff
            
            
        
        
        if type(fleet) != list:
            raise TypeError('Fleet must be a list')                
        else:
            self.fleet = fleet
            
            
            
        if type(trips) != list:
            raise TypeError('Trips must be a list')        
        else:
            self.trips = trips

        
        
    def get_name(self):
        """
        purpose: Get the name of the instance.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The name string.
        """
        
        return self.name
    
    def get_fleet(self):
        """
        purpose: Get the list of items in the fleet.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The fleet list.
        """
        return self.fleet
    
    def get_staff(self):
        """
        purpose: Get the list of staff members.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The staff list.
        """
        return self.staff
    
    def get_trips(self):
        """
        purpose: Get the list of scheduled trips.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The trips list.
        """
        
        return self.trips 

    def expand_fleet(self, fleet):
        """
        purpose: Add valid airplanes from a new fleet, extract their IDs, remove duplicates, and sort them numerically.
        parameters: 
            fleet: A list containing items to filter and add.
        throws: None.
        pre: Elements in the fleet parameter that are Airplanes must have a numeric ID (or numeric string ID).
        post: self.fleet is updated to contain a sorted list of unique airplane ID strings.
        returns: The updated, sorted list of airplane IDs.
        """
        
        temp_storage = self.fleet
        temp_storage2 = None
        for i in fleet:
            if isinstance(i, Airplane):
                temp_storage.append(i)
        temp_storage2 = []  
                
        for i in temp_storage:
            temp_storage2.append(i.id)
        temp_storage2 = list(set(temp_storage2))
        self.fleet = temp_storage2
        sorted = []

        while len(self.fleet) > 0:
            smallest = self.fleet[0]

            for i in self.fleet:
                if int(i) < int(smallest):
                    smallest = str(i)

            sorted.append(smallest)
            self.fleet.remove(smallest) 
        self.fleet = sorted
        return self.fleet


    def shrink_fleet(self,fleet):
        """
        purpose: Remove a matching airplane from the fleet list based on its ID.
        parameters: 
            fleet: A list containing items to check for removal.
        throws: None.
        pre: None.
        post: self.fleet has the matching Airplane object removed if it exists.
        returns: The updated fleet list.
        """
        
        is_object = False
        hold_object = None
        if type(fleet) != list:
            return self.fleet

        for i in fleet:
            if  isinstance(i, Airplane):
                is_object = True 
                hold_object = i 
                        
        for j in self.fleet:
            if isinstance(j, Airplane):
                is_object = True
                if hold_object is not None and j.id == hold_object.id: 
                    self.fleet.remove(j)
                    
        return self.fleet


    def expand_staff(self,staff):
        """
        purpose: Add valid crew members from a list, extract their IDs, remove duplicates, and sort them.
        parameters: 
            staff: A list containing items to filter and add.
        throws: None.
        pre: Elements in the staff parameter that are CrewMembers must have comparable IDs.
        post: self.staff is updated to contain a sorted list of unique crew member IDs.
        returns: The updated, sorted list of staff IDs.
        """
        
        temp_storage = self.staff
        temp_storage2 = None
        for i in staff:
            if isinstance(i, CrewMember):
                temp_storage.append(i)
                temp_storage2 = []  
                        
        for i in temp_storage:
            temp_storage2.append(i.id)
            temp_storage2 = list(set(temp_storage2))
            self.staff = temp_storage2

        sorted = []

        while len(self.staff) > 0:
                smallest = self.staff[0]
                for i in self.staff:
                    if (i) < (smallest):
                        smallest = str(i)
                sorted.append(smallest)
                self.staff.remove(smallest) 
        self.staff = sorted
        return self.staff


    def shrink_staff(self,staff):
        """
        purpose: Remove a matching crew member from the staff list based on their ID.
        parameters: 
            staff: A list containing items to check for removal.
        throws: None.
        pre: None.
        post: self.staff has the matching CrewMember object removed if it exists.
        returns: The updated staff list.
        """
        
        is_object = False
        hold_object = None
        if type(staff) != list:
            return self.staff

        for i in staff:
            if  isinstance(i, CrewMember):
                is_object = True 
                hold_object = i
                        
        for j in self.staff:
            if isinstance(j, CrewMember):
                is_object = True
                if hold_object is not None and j.id == hold_object.id: 
                    self.staff.remove(j)
        return self.staff 


    def add_trips(self, trips):
        """
        purpose: Add valid trips from a list, extract their IDs, remove duplicates, and sort them.
        parameters: 
            trips: A list containing items to filter and add.
        throws: None.
        pre: Elements in the trips parameter that are Trips must have comparable IDs.
        post: self.trips is updated to contain a sorted list of unique trip IDs.
        returns: The updated, sorted list of trip IDs.
        """
        
        temp_storage = self.trips
        temp_storage2 = None
        for i in trips:
            if isinstance(i, Trip):
                temp_storage.append(i)
                temp_storage2 = []  
                        
        for i in temp_storage:
            temp_storage2.append(i.id)
            temp_storage2 = list(set(temp_storage2))
            self.trips = temp_storage2
        sorted = []
        
        while len(self.trips) > 0:
            smallest = self.trips[0] 
            for i in self.trips:
                if (i) < (smallest):
                    smallest = str(i)
            sorted.append(smallest)
            self.trips.remove(smallest) 
        self.trips = sorted
        return self.trips 
    
    def cancel_trips(self, trips):
        """
        purpose: Remove a matching trip from the trips list based on its ID.
        parameters: 
            trips: A list containing items to check for removal.
        throws: None.
        pre: None.
        post: self.trips has the matching Trip object removed if it exists.
        returns: The updated trips list.
        """
       
        is_object = False
        hold_object = None
        if type(trips) != list:
            return self.trips

        for i in trips:
            if  isinstance(i, Trip):
                is_object = True 
                hold_object = i
                        
        for j in self.trips:
            if isinstance(j, Trip):
                is_object = True
                if hold_object is not None and j.id == hold_object.id: 
                    self.trips.remove(j)
        return self.trips  
        

    def shortest_layover(self):
        """
        purpose: Find and return the shortest layover duration across all trips.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The shortest layover duration found, or None if there are no layovers or trips.
        """
        
        if not self.trips:
            return None

        layover = None 
        
        
        for trip in self.trips:
            
            if isinstance(trip, str):
               
                continue 
                
            if len(trip.flights) <= 1:
                continue 
            
            previous_arrival = None 
            for flight in trip.flights:
                if previous_arrival is not None:
                    time_elapsed = flight.departure - previous_arrival
                    if layover is None or time_elapsed < layover:
                        layover = time_elapsed
                    
                previous_arrival = flight.arrival
                
        return layover


        
    def __str__(self):
        """
        purpose: Generate a string representation of the instance.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted string containing the name.
        """
        
        return f'{self.name} :\n'
    
class Airplane:
    
    def __init__(self, id):
        """
        purpose: Initialize a new instance with an ID and an empty list of flights.
        parameters: 
            id: A unique identifier string.
        throws: 
            TypeError: If id is not a string.
            ValueError: If id is an empty string.
        pre: None.
        post: Object is initialized with a valid ID and an empty flights list.
        returns: None.
        """
        
        if type(id) != str:
            raise TypeError('Must be a string')
        elif id == '':
            raise ValueError('ID cannot be empty')
        
        else:
            self.id = id
            self.flights = []
            
            
    def get_flights(self):
        """
        purpose: Get the list of flights associated with this instance.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The flights list.
        """
        
        return self.flights
    
    def get_id(self):
        """
        purpose: Get the unique identifier string.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The id string.
        """
        
        return self.id
    
    def __str__(self):
        """
        purpose: Generate a string representation of the airplane, showing its ID and scheduled flights.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted string summary of the airplane.
        """
        
        result = f'\nAirplane: {self.id} \nScheduled flights:{self.flights}\n'
        
        return result
    
    def __eq__(self,other):
        """
        purpose: Generate a string representation of the airplane, showing its ID and scheduled flights.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted string summary of the airplane.
        """
        
        if not isinstance(other, Airplane):
            return False
        return self.id == other.id 
    
    

            
            
    
    
class CrewMember:
    def __init__(self, id):
        """
        purpose: Initialize a new instance with an ID and an empty list of flights.
        parameters: 
            id: A unique identifier string.
        throws: 
            TypeError: If id is not a string.
            ValueError: If id is an empty string.
        pre: None.
        post: Object is initialized with a valid ID and an empty flights list.
        returns: None.
        """
        
        if not isinstance(id, str):
            raise TypeError('ID must be a string')
        
        elif id == '':
            raise ValueError('String cannot be empty')
        else:
            self.id = id
            self.flights = []
            
    def get_flights(self):
        """
        purpose: Get the list of flights associated with this instance.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The flights list.
        """
        
        return self.flights
    
    def get_id(self):
        """
        purpose: Get the unique identifier string.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The id string.
        """
        
        return self.id
    
    def __str__(self):
        """
        purpose: Generate a string representation of the crew member, showing their ID.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted string summary of the crew member.
        """
        
        return f"Crew Member: {self.id}\nScheduled flights:\n"

    def __eq__(self,other):
        """
        purpose: Check if this crew member is equal to another object based on their IDs.
        parameters: 
            other: The object to compare with this instance.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: True if the other object is a CrewMember with the same ID, False otherwise.
        """
        
        if not isinstance(other, CrewMember):
            return False
        return self.id == other.id
    
    def __repr__(self):
        """
        purpose: Generate an official string representation of the instance, showing its ID.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The id string.
        """
        
        return f'{self.id}'
    
    
    
class Trip:
    def __init__(self, id):
        """
        purpose: Initialize a new instance with an ID and an empty list of flights.
        parameters: 
            id: A unique identifier string.
        throws: 
            TypeError: If id is not a string.
            ValueError: If id is an empty string.
        pre: None.
        post: Object is initialized with a valid ID and an empty flights list.
        returns: None.
        """
        
        self.flights = []
        if type(id) != str:
            raise TypeError('Must be a string')
        elif id == '':
            raise ValueError('ID cannot be empty')
        else:
            self.id = id
            self.flights = []
            
    def get_flights(self):
        """
        purpose: Get the total number of flights associated with this instance.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The integer count of flights.
        """
        
        return len(self.flights)
    
    def get_id(self):
        """
        purpose: Get the unique identifier string.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The id string.
        """
        
        return self.id
            
        
    def add_flight(self,flight): 
        """
        purpose: Add a flight to the list if it is a valid Flight instance.
        parameters: 
            flight: The flight object to be added.
        throws: None.
        pre: None.
        post: self.flights has the new Flight object appended if it is valid.
        returns: An empty list if the input is not a valid Flight instance, otherwise None.
        """
        
        if not isinstance(flight, Flight):
            return []
         
        for existing_flight in self.flights:
            if flight.id != existing_flight.id:
                pass 
            
        self.flights.append(flight)
        
    def remove_flight(self, flight):
        """
        purpose: Remove a flight from the flights list if it matches an existing flight's ID.
        parameters: 
            flight: The flight object to be removed.
        throws: None.
        pre: None.
        post: self.flights has the matching Flight object removed if it is found.
        returns: The current flight count if the input is invalid, otherwise the updated flights list.
        """
        
        if not isinstance(flight, Flight):
            return self.get_flights()
        
        for existing_flight in self.flights:
            if flight.id == existing_flight.id:
                self.flights.remove(flight)
        return self.flights
    
    def duration(self):
        """
        purpose: Calculate the total flight duration by summing up the elapsed time of all flights.
        parameters: None.
        throws: None.
        pre: Each flight object in self.flights must have valid arrival and departure attributes that support subtraction.
        post: Object state is unmodified.
        returns: A timedelta object representing the cumulative flight duration.
        """
       
        time_elapsed = 0
        time_duration = timedelta(0)
        for flight in self.flights:
            time_elapsed = flight.arrival - flight.departure
            time_duration += time_elapsed            
           
        return time_duration
    
            
    def num_stops(self):   
        """
        purpose: Get the number of stops by counting the total flights.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The integer count of flights.
        """
        
        return len(self.flights)
    
    def __str__(self):
        """
        purpose: Generate a string representation of the trip, showing its ID and number of flights.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted string summary of the trip.
        """

       
        return f'Trip:{self.id} has {self.num_stops()} flights.'
    
    
    def __eq__(self,other):
        """
        purpose: Check if this instance is equal to another object based on their IDs.
        parameters: 
            other: The object to compare with this instance.
        throws: None.
        pre: The other object must have an id attribute.
        post: Object state is unmodified.
        returns: True if both objects have matching IDs, False otherwise.
        """
        
        return self.id == other.id
            
        
        
class Flight:
    def __init__(self, id, start, to, departure, arrival):
        """
        purpose: Initialize a flight instance with an ID, origin, destination, and schedule.
        parameters: 
            id: A unique flight identification string.
            start: A 3-character string representing the origin airport code.
            to: A 3-character string representing the destination airport code.
            departure: A datetime object for the departure time.
            arrival: A datetime object for the arrival time.
        throws: 
            TypeError: If id, start, or to are incorrect types, or if departure/arrival are not datetime objects.
            ValueError: If id is empty, airport codes are not 3 characters, or arrival is before departure.
        pre: None.
        post: Object is initialized with valid route details, timestamps, and empty tracking lists.
        returns: None.
        """
        
        if type(id) != str:
            raise TypeError('ID must be a string')
        elif id == '':
            raise ValueError('ID must not be an empty string')
        else:
            self.id = id
            
            
        
        if type(start) == list:
            raise TypeError('Data type must not be a list')
        elif len(start) != 3:
            raise ValueError('Start must be 3 characters')
             
        else:
            self.start = start
            
            
        if type(to) == list:
            raise TypeError('Data type musn\'t be a list')
        elif len(to) != 3:
            raise ValueError('To must be 3 characters')
        else:
            self.to = to
            
            
        
        if type(departure) is not datetime :
            raise TypeError('Departure must be datetime object')
        else:
            self.departure = departure
            
        
        if type(arrival) is not datetime:
            raise TypeError('Arrival must be  datetime object')
        elif departure > arrival:
            raise ValueError('Arrival time must be before departure')
        else:
            self.arrival = arrival
        self.crew = []
        self.plane = []
        self.seat_number = []
        self.airplane = None
        
            
    def get_crew(self):
        """
        purpose: Get the list of crew members assigned to this flight.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The crew list.
        """
        
        return self.crew
    
    def get_plane(self):
        """
        purpose: Get the airplane assigned to this flight if one exists.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: The first element in the plane list, or None if the list is empty.
        """
        
        if len(self.plane) == 0:
            return None
        else:
            return self.plane[0]

    
    def allocate_plane(self,plane):
        """
        purpose: Assign a plane to this flight if there are no scheduling conflicts.
        parameters: 
            plane: The Airplane object to allocate to this flight.
        throws: None.
        pre: The plane object must have a valid flights list and a working conflict check method.
        post: Both the flight's plane list and the airplane's flights list are updated to reference each other.
        returns: None, or None explicitly if validation or conflict checks fail.
        """
        
        if not isinstance(plane, Airplane):
            return None
        
        
           
        for flight in plane.flights:
            if self._flight_conflict(flight) == True:
                return None
            
        
        
        self.plane.append(plane) 
        plane.flights.append(self) 
        
   
            
        
    def _flight_conflict(self,other):
        """
        purpose: Check if this flight's schedule overlaps with another flight.
        parameters: 
            other: The other Flight object to compare schedules against.
        throws: None.
        pre: Both flight objects must have valid departure and arrival datetime attributes.
        post: Object state is unmodified.
        returns: True if a time conflict exists, False if the schedules do not overlap.
        """
        
        if self.departure >= other.arrival or self.arrival <= other.departure:
            return False
        else:
            return True
        
    def allocate_crew(self,crew):
        """
        purpose: Assign a list of crew members to this flight, ensuring each member has no scheduling conflicts.
        parameters: 
            crew: A list of CrewMember objects to be assigned.
        throws: None.
        pre: Each item in the crew list must have a working flights collection that works with conflict checks.
        post: Available crew members are added to the flight's crew list, and the flight is added to their records.
        returns: An empty list if the input parameter is not a list, otherwise None.
        """
       
        if not isinstance(crew, list): 
            return []
        
        
        for member in crew: 
            is_free = True
            for i in member.flights:
                if self._flight_conflict(i) == True:
                    is_free = False
                    
            if is_free == True:
                self.crew.append(member)
                member.flights.append(self)            
                    
    def assign_seat(self, seat_number):
        """
        purpose: Assign a valid seat number to the flight if it is not already taken.
        parameters: 
            seat_number: The seat number integer to assign.
        throws: None.
        pre: None.
        post: self.seat_number list contains the new seat integer if the assignment succeeds.
        returns: True if the seat is valid and successfully assigned, False otherwise.
        """
        
        if not isinstance(seat_number, int):
            return False
        
        if seat_number in self.seat_number: 
            return False 
        
        if self.seat_number != seat_number:
        
            if seat_number > 0 and seat_number <= 100:
                self.seat_number.append(seat_number)
                return True
            else:
                return False
            
    def seat_map(self):
        """
        purpose: Generate a visual string representation of the seat layout showing open and occupied seats.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted text string representing the 25-row, 4-column seat map.
        """
        
        string = ('------------\n|A||B||C||D|\n------------')
        current_seat = 1
        for column in range(1,26): #rows
            string += f'{column}'
            for row in range(4): #columns
                if current_seat in self.seat_number:
                    string += 'X'
                else:
                    string += '| |'
                current_seat += 1
            string += '\n' 
        string += (' ------------')
        return string
    
    def __str__(self):
        """
        purpose: Generate a string representation of the flight including its route, schedule, and assigned plane.
        parameters: None.
        throws: None.
        pre: None.
        post: Object state is unmodified.
        returns: A formatted string summary of the flight details.
        """
        
        if self.airplane:
            plane_display = self.airplane.id
        else:
            plane_display = 'None'
        
        return f'Flight#: {self.id}\nFrom: {self.start} at {self.departure}\nTo: {self.to} at {self.arrival}\nAirplane: {plane_display}' 
    
    def __eq__(self,other):
        """
        purpose: Check if this flight is equal to another object based on their IDs.
        parameters: 
            other: The object to compare with this instance.
        throws: None.
        pre: The other object must have an id attribute.
        post: Object state is unmodified.
        returns: True if both objects have matching IDs, False otherwise.
        """
        
        return self.id == other.id
    
                
        
 
 
        


#TESTING AIRLINE INIT
#airline = AirLine()
#airline = AirLine(name = 1)
#airline = AirLine(name = '')
#airline = AirLine(staff = None)
#airline = AirLine(fleet = set())
#airline = AirLine(trips = True)
#airline = AirLine(staff=[], fleet=[], trips=[])
#airline = AirLine(trips = [1,True,'MyTrip']) 

#TESTING AIRLINE EXPAND FLEET
#airline = AirLine()
#airline.expand_fleet([1,2,3])
#airline.expand_fleet([Airplane("1"),Airplane("1"),Airplane("1")])
#airline.expand_fleet([Airplane("1"),Airplane("2"),Airplane("3")])
#print(airline.get_fleet())

#TESTING AIRLINE SHRINK FLEET
#airline = AirLine()
#airline = AirLine(fleet=[Airplane("1"),Airplane("2"),Airplane("3")])
#airline.shrink_fleet( Airplane("1") )
#airline.shrink_fleet( [Airplane("1")] )
#airline.shrink_fleet( [Airplane("4")] )
#airline.shrink_fleet( [] )
#print(airline.get_fleet())

#TESTING AIRLINE EXPAND STAFF
#airline = AirLine()
#airline.expand_staff(["pilot1","copilot55",3])
#airline.expand_staff([CrewMember("cm1"),CrewMember("cm1"),CrewMember("cm1")])
#airline.expand_staff([CrewMember("cm1"),CrewMember("cm2"),CrewMember("cm3")])
#print(airline.get_staff())

#TESTING AIRLINE SHRINK STAFF
#airline = AirLine()
#airline = AirLine(staff=[CrewMember("cm1"), CrewMember("cm2"), CrewMember("cm3")])
#airline.shrink_staff( ["cm1","cm2","cm3"] )
#airline.shrink_staff( CrewMember("cm1") )
#airline.shrink_staff( [CrewMember("cm1")] )
#airline.shrink_staff( [CrewMember("cm4")] )
#print(airline.get_staff())


#TESTING AIRLINE ADD TRIPS
#airline = AirLine()
#airline.add_trips([1,"t2",False])
#airline.add_trips([Trip("t1"),Trip("t1"),Trip("t1")])
#airline.add_trips([Trip("t1"),Trip("t2"),Trip("t3")])
#print(airline.get_trips())

#TESTING AIRLINE CANCEL TRIPS
#airline = AirLine()
#airline = AirLine(trips=[Trip("t1"), Trip("t2"), Trip("t3")])
#airline.cancel_trips( ["t1","t2","t3"] )
#airline.cancel_trips( Trip("t1") )
#airline.cancel_trips( [ Trip("t1")] )
#print(airline.get_trips())

#TESTING AIRLINE SHORTEST LAYOVER
#airline = AirLine()
#print(airline.shortest_layover())
#airline.trips = ["invalid_trip_string"]
#print(airline.shortest_layover())
#t1 = Trip("t1")
#f1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,14,0,0))
#t1.add_flight(f1)
#airline.trips = [t1]
#print(airline.shortest_layover())
#f2 = Flight("f2","BBB","CCC",datetime(2026,10,1,15,30,0),datetime(2026,10,1,18,0,0))
#t1.add_flight(f2)
#print(airline.shortest_layover())

#TESTING AIRLINE STR
#airline = AirLine(name='Airalgorithmia')
#print(str(airline))


#TESTING AIRPLANE GET FLIGHTS
#plane = Airplane("A320")
#print(plane.get_flights())

#TESTING AIRPLANE GET ID
#plane = Airplane("B737")
#print(plane.get_id())

#TESTING AIRPLANE STR
#plane = Airplane("A380")
#print(str(plane))

#TESTING AIRPLANE EQ
#plane1 = Airplane("A320")
#plane2 = Airplane("A320")
#plane3 = Airplane("B737")
#print(plane1 == plane2)
#print(plane1 == plane3)
#print(plane1 == "NotAnAirplaneObject")


#TESTING CREWMEMBER GET FLIGHTS
#crew = CrewMember("cm1")
#print(crew.get_flights())

#TESTING CREWMEMBER GET ID
#crew = CrewMember("cm55")
#print(crew.get_id())

#TESTING CREWMEMBER STR
#crew = CrewMember("pilot1")
#print(str(crew))

#TESTING CREWMEMBER EQ
#crew1 = CrewMember("cm1")
#crew2 = CrewMember("cm1")
#crew3 = CrewMember("cm2")
#print(crew1 == crew2)
#print(crew1 == crew3)
#print(crew1 == "NotACrewMemberObject")

#TESTING CREWMEMBER REPR
#crew = CrewMember("cm99")
#print(repr(crew))


#TESTING TRIP INIT
#trip = Trip("t1")
#trip = Trip(123)
#trip = Trip("")

#TESTING TRIP GET FLIGHTS
#trip = Trip("t1")
#print(trip.get_flights())

#TESTING TRIP GET ID
#trip = Trip("t55")
#print(trip.get_id())

#TESTING TRIP ADD FLIGHT
#trip = Trip("t1")
#print(trip.add_flight("NotAFlightInstance"))
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#trip.add_flight(flight1)
#print(trip.get_flights())

#TESTING TRIP REMOVE FLIGHT
#trip = Trip("t1")
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(trip.remove_flight("NotAFlightInstance"))
#trip.add_flight(flight1)
#print(trip.remove_flight(flight1))

#TESTING TRIP DURATION
#trip = Trip("t1")
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#trip.add_flight(flight1)
#print(trip.duration())

#TESTING TRIP NUM STOPS
#trip = Trip("t1")
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#trip.add_flight(flight1)
#print(trip.num_stops())

#TESTING TRIP STR
#trip = Trip("t1")
#print(str(trip))

#TESTING TRIP EQ
#trip1 = Trip("t1")
#trip2 = Trip("t1")
#trip3 = Trip("t2")
#print(trip1 == trip2)
#print(trip1 == trip3)


#TESTING FLIGHT GET CREW
#flight = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight.get_crew())

#TESTING FLIGHT GET PLANE
#flight = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight.get_plane())

#TESTING FLIGHT ALLOCATE PLANE
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight1.allocate_plane("NotAPlaneObject"))
#plane = Airplane("A320")
#flight1.allocate_plane(plane)
#print(flight1.get_plane())
#flight2 = Flight("f2","BBB","CCC",datetime(2026,10,1,13,0,0),datetime(2026,10,1,16,0,0))
#print(flight2.allocate_plane(plane))

#TESTING FLIGHT FLIGHT CONFLICT
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#flight2 = Flight("f2","BBB","CCC",datetime(2026,10,1,14,0,0),datetime(2026,10,1,16,0,0))
#flight3 = Flight("f3","CCC","DDD",datetime(2026,10,1,16,0,0),datetime(2026,10,1,18,0,0))
#print(flight1._flight_conflict(flight2))
#print(flight1._flight_conflict(flight3))

#TESTING FLIGHT ALLOCATE CREW
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight1.allocate_crew("NotAList"))
#cm1 = CrewMember("cm1")
#flight1.allocate_crew([cm1])
#print(flight1.get_crew())

#TESTING FLIGHT ASSIGN SEAT
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight1.assign_seat("Seat1"))
#print(flight1.assign_seat(0))
#print(flight1.assign_seat(101))
#print(flight1.assign_seat(25))
#print(flight1.assign_seat(25))

#TESTING FLIGHT SEAT MAP
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight1.seat_map())

#TESTING FLIGHT STR
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(str(flight1))

#TESTING FLIGHT EQ
#flight1 = Flight("f1","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#flight2 = Flight("f1","XXX","YYY",datetime(2026,11,1,10,0,0),datetime(2026,11,1,12,0,0))
#flight3 = Flight("f2","AAA","BBB",datetime(2026,10,1,12,0,0),datetime(2026,10,1,15,0,0))
#print(flight1 == flight2)
#print(flight1 == flight3)
