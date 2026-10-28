# Airline-Managment-System
# Airline Management System

A Python-based system designed to manage airline operations, fleets, crew scheduling, and flight tracking.

## Overview

This project models an airline network through an object-oriented architecture. It handles logistics across five core classes: AirLine, Airplane, CrewMember, Trip, and Flight. The system supports automatic ID sorting, fleet and staff updates, and schedule conflict detection.

## Key Features

- **Fleet and Staff Management:** Automatically filters, removes duplicates, and numerically sorts IDs when expanding or shrinking fleets and staff lists.
- **Conflict Detection:** Validates flight schedules to prevent overlapping assignments for both aircraft and crew members.
- **Seat Mapping:** Generates a text-based seat layout grid to track available and occupied seats.
- **Academic Documentation:** Includes PEP 8 compliant docstrings detailing parameters, exceptions, pre-conditions, and return values for all methods.

## Quick Start Example

```python
from datetime import datetime
from airtravel import AirLine, Airplane, Flight

# Initialize the airline
airline = AirLine(name="Airalgorithmia")

# Add an airplane to the fleet
plane = Airplane("A320")
airline.expand_fleet([plane])

# Create a scheduled flight
flight = Flight("F101", "YEG", "YYZ", datetime(2026, 10, 1, 12, 0), datetime(2026, 10, 1, 16, 0))

# Allocate the plane to the flight
flight.allocate_plane(plane)

# Assign a seat
flight.assign_seat(15)
print(flight.seat_map())
