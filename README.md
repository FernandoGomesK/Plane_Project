# Flight Management Simulator ✈️

This project is a Python-based command-line application that simulates the management of airline flights. It handles the creation of flights, assignment of crew and passengers, and generation of flight manifests.

# Core Features

    Dynamic Flight Creation: Generates multiple flights with a specified number of seats.

    Unique IDs: Assigns a unique, randomly generated ID to each flight using uuid.

    Crew Assignment: Populates each flight with a pilot, copilot, and cabin crew with randomly generated names using Faker.

    Passenger Boarding: Assigns passengers to available seats until the flight is full.

    Flight Manifest: Displays a detailed manifest for each flight, including crew details and a random sample of 10 boarded passengers.

# Code Structure

    main.py: The main entry point to run the simulation.

    flight.py: Contains the Flight class, which manages a single flight's data and operations.

    flightmanager.py: Contains the FlightManager class, responsible for creating and managing a list of all flights.

    person.py: Defines the abstract base class Person and the inherited classes Passenger and FlightCrew, which contains Pilot, Copilot and CabinCrew

    seat.py: Contains the Seat class, which handles seat status and passenger assignment.

    planemodel.py: contains all the models of plane available at the moment.
# Libraries and Modules

This project uses a combination of one external library and several built-in Python modules.

# External Library

    Faker: Utilized to generate random names for crew and passengers.

# Built-in Modules

    random: Used to sample 10 random passengers for the manifest display, and to select the plane model in the test run

    uuid: Used to generate unique IDs for each flight.

    typing: Used for type hinting to improve code clarity and maintainability.

    abc: Utilized to create abstract classes (Person) and abstract methods.