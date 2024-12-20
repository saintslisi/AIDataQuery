# AIDataQuery 📊🤖

**AIDataQuery** is an innovative program powered by GPT-4, designed to streamline interaction with MySQL databases. With a simple user input, the program generates and executes MySQL queries on a generic database and returns the query results in a refined and user-friendly format.

## How It Works
1. The user provides an input describing the desired database query in natural language.
2. The program leverages GPT-4 to interpret the input and generate an accurate MySQL query.
3. The query is executed on the connected database.
4. Results are retrieved, reformulated, and displayed in a polished, easy-to-read format.

## Tasks

1. **Generalize Database Operations**  
   Implement core MySQL operations (search, insert, update, and delete) based on dynamic user input, ensuring flexibility and adaptability.

2. **Support for Multiple Tables with Relationships**  
   Extend functionality to handle databases with multiple tables, including the ability to manage and respect relationships between them (e.g., foreign keys).

3. **Add Memory Functionality**  
   Integrate memory capabilities to retain context and improve interaction consistency over multiple queries or sessions.

## Results Obtained

Several types of tests were conducted, and from the results, it is clear that the project works, but it must be supported by a well-designed database where tables and fields are described in detail (with examples, if necessary) and contain a sufficient amount of data. This is because some queries that users may ask, despite being correctly generated by the model, may not return any results.

During the tests, the model generated between 90% and 95% of correct queries. Based on the user's inputs, it was able to perform multiple queries across different tables and return the expected results several times. It was also capable of generating more complex queries that required information from multiple tables or applying various filters, successfully extracting the correct parameters and relating them to the appropriate attributes.

### Examples of Tested Inputs (I), Generated Queries (Q), and Obtained Outputs (O):

<details><summary>1. Query to find one-way flights in December</summary>

   - **I** - "Tell me how many flights are departing from Catania this month and find the cheapest and fastest one."
   - **Q** - 
     ```sql
     SELECT COUNT(*)
     FROM voli
     WHERE partenza = 'CTA' AND MONTH(data) = 12 AND YEAR(data) = 2024;

     SELECT *
     FROM voli
     WHERE partenza = 'CTA' AND MONTH(data) = 12 AND YEAR(data) = 2024
     ORDER BY prezzo_biglietto ASC, durata ASC
     LIMIT 1;
     ```
   - **O** - 
     ```
     This month, there are 191 flights departing from Catania. The cheapest and fastest flight departs from Catania (CTA) at 01:10 on December 19, 2024, with destination Warsaw (WAW). The flight code is AZ103, and its duration is 20 minutes. However, the flight has been cancelled. The final ticket price would have been 21.51 euros.
     ```
</details>

<details><summary>2. Use of memory in relation to the previous query</summary>

   - **I** - "That's fine, now look for a return flight, preferably within 3 to 7 days."
   - **Q** - 
     ```sql
     SELECT *
     FROM voli
     WHERE partenza = 'WAW' AND destinazione = 'CTA'
     AND DATE(data) BETWEEN '2024-12-22' AND '2024-12-26'
     ORDER BY prezzo_biglietto ASC, durata ASC;
     ```
   - **O** - 
     ```
     I found two return flight options from Warsaw (WAW) to Catania (CTA) in the requested period:

     1. The first flight departs on December 23, 2024, at 02:10. The flight duration is 240 minutes, and the flight code is RY107. The final ticket price is 509.17 euros.
     2. The second flight departs on December 23, 2024, at 15:50. The flight duration is 60 minutes, and the flight code is FR102. The final ticket price is 570.16 euros.

     Choose based on your preferred time and cost.
     ```
</details>

<details><summary>3. Query to search for flights to Spain from Catania in December</summary>

   - **I** - "Find a flight to a city in Spain from Catania this month."
   - **Q** - 
     ```sql
     SELECT * 
     FROM voli
     WHERE partenza = 'CTA'
     AND destinazione IN (
         SELECT codice_IATA 
         FROM aeroporti 
         WHERE paese = 'Spagna'
     )
     AND DATE(data) BETWEEN '2024-12-01' AND '2024-12-31';        
     ```
   - **O** - 
     ```
     Here are the available flights from Catania to Spain in December 2024:
     1. **Catania (CTA) - Madrid (MAD)**
        - Date and Time: December 4, 2024, 04:40
        - Duration: 280 minutes
        - Flight Code: RY104
        - Status: Completed
        - Ticket Price: €241.23
     2. **Catania (CTA) - Madrid (MAD)**
        - Date and Time: December 27, 2024, 07:00
        - Duration: 150 minutes
        - Flight Code: RY110
        - Status: Scheduled
        - Ticket Price: €495.57
     3. **Catania (CTA) - Barcelona (BCN)**
        - Date and Time: December 26, 2024, 16:40
        - Duration: 110 minutes
        - Flight Code: RY107
        - Status: Delayed
        - Ticket Price: €186.69
     Note: Some flights may have been cancelled.
     ```
</details>

<details><summary>4. Query to continue the search for hotels in Madrid</summary>

   - **I** - "Okay, now give me a list of 10 hotels in Madrid."
   - **Q** - 
     ```sql
     SELECT * 
     FROM hotel
     WHERE luogo = 'Madrid'
     LIMIT 10;        
     ```
   - **O** - 
     ```
     Here are some hotels in Madrid for you to choose from:
     1. **Burnett, Miranda and Walker Hotel**
        - Stars: 3
        - Price Range: Luxury
        - Amenities: Gym, Pool
        - Phone: 95081188844814
        - Email: melissa16@example.net
     2. **Thompson-Stokes Hotel**
        - Stars: 4
        - Price Range: Luxury
        - Amenities: Breakfast Included, Gym
        - Phone: 42039939366966
        - Email: mary38@example.org
     3. **Hayes and Sons Hotel**
        - Stars: 1
        - Price Range: Medium
        - Amenities: Pool, Breakfast Included, Gym, Free Wi-Fi
        - Phone: 14039933323232
        - Email: xbarber@example.com
     4. **Casey PLC Hotel**
        - Stars: 2
        - Price Range: Medium
        - Amenities: Gym, Pool, Free Wi-Fi, Room Service, SPA
        - Phone: 76099999988888
        - Email: jamesellis@example.org
     If you need more information or a different type of hotel, let me know!
     ```
</details>

<details><summary>5. Query to check availability and prices for a specific hotel room</summary>

   - **I** - "Take the first hotel you found and check the availability and prices of rooms."
   - **Q** - 
     ```sql
     SELECT * 
     FROM stanze
     WHERE id_hotel = 70;
     ```
   - **O** - 
     ```
     Here is the availability and room prices for the "Burnett, Miranda and Walker Hotel":
     1. **Room 397**
        - Type: Double
        - Price per night: €95.91
        - Status: Available
        - View: City
     2. **Room 781**
        - Type: Suite
        - Price per night: €249.37
        - Status: Available
        - View: City

     Occupied or unavailable rooms have been excluded. If you need more information or wish to book a room, let me know!
     ```
</details>

<details><summary>6. Query to search for specific details about a trip</summary>

   - **I** - "I want to travel in December, departing from Catania to Paris, find the cheapest round-trip flights, a place to stay with available rooms that have a sea view, a pool, and a gym, an affordable electric vehicle, and 4 highly rated restaurants."
   - **Q** - 
     ```sql
     SELECT *
     FROM voli
     WHERE partenza = 'CTA' AND destinazione = 'CDG' AND MONTH(data) = 12
     ORDER BY prezzo_biglietto ASC
     LIMIT 1;

     SELECT *
     FROM voli
     WHERE partenza = 'CDG' AND destinazione = 'CTA' AND MONTH(data) = 12
     ORDER BY prezzo_biglietto ASC
     LIMIT 1;

     SELECT hotel.nome, stanze.*
     FROM hotel
     JOIN stanze ON hotel.id = stanze.id_hotel
     WHERE hotel.luogo = 'Parigi'
     AND stanze.vista = 'mare'
     AND stanze.stato = 'libera'
     AND hotel.servizi LIKE '%piscina%'
     AND hotel.servizi LIKE '%palestra%'
     LIMIT 1;

     SELECT *
     FROM veicoli_noleggio
     WHERE tipo = 'Auto' AND carburante = 'Elettrico' AND disponibilita = TRUE
     ORDER BY prezzo_giornaliero ASC
     LIMIT 1;

     SELECT *
     FROM ristoranti
     WHERE citta = 'Parigi'
     ORDER BY valutazione_media DESC
     LIMIT 4;         
     ```
   - **O** - 
     ```
     Here are the options found for your trip to Paris:
     **Cheapest Flights:**
     - Outbound: Flight FR100 from Catania (CTA) to Paris (CDG) on December 14, 2024, at 16:20. Price: €224.59.
     - Return: Flight AZ106 from Paris (CDG) to Catania (CTA) on December 26, 2024, at 21:20. Price: €246.91.
     **Hotel:**
     - Williams LLC Hotel in Paris. Room: Suite with Sea View.
     **Electric Vehicle:**
     - Model: BMW i3, Daily Price: €65.00.
     **Top Rated Restaurants in Paris:**
     1. Robinson, Sanchez and Baker Restaurant - Rating: 4.98
     2. Pierce, Martinez and George Restaurant - Rating: 4.97
     3. Pratt, Young and Duran Restaurant - Rating: 4.94
     4. Flores, Peters and Ruiz Restaurant - Rating: 4.93
     These are the best options found for your trip.
     ```
</details>

<details><summary>7. Insert Data into the Database</summary>

   - **I** - "The flight BA573 departs from Milan Malpensa (MXP) and arrives at London Heathrow (LHR). The departure is scheduled for December 21, 2024, at 09:00, and the flight duration is 120 minutes. The flight is scheduled for the morning and currently has 0 passengers. The flight is scheduled, with gate B3 for departure and gate C7 for destination. The plane used is a Boeing 737. The base price of the flight is 150.00 euros, and the final ticket price is 200.00 euros."
   - **Q** - 
     ```sql
     INSERT INTO voli (partenza, destinazione, data, durata, codice_volo, fascia_oraria, num_passeggeri, stato_volo, gate_partenza, gate_destinazione, aereo_id, prezzo_base, prezzo_biglietto)
     VALUES ('MXP', 'LHR', '2024-12-21 09:00:00', 120, 'BA573', 'Mattina', 0, 'Programmato', 'B3', 'C7', 1, 150.00, 200.00);
     ```
   - **O** - 
     ```
     Query executed without returning rows
     ```
</details>

## Test Tables of the Database

The Test Database simulates a travel platform database.  
It includes several tables with realistic fields.  
Currently, approximately 25,000 test data entries have been inserted into the DB using a data generation program.  
The data is realistic, although some entries may have inconsistencies.  

The following **test tables** have been used in the database:

1. **Planes:**  
   Used to store information about specific planes and their associated airlines.

2. **Flights** *(Relation to Planes):*  
   Contains flight-related data such as:  
   - Departure  
   - Destination  
   - Duration  
   - Price  
   - Flight Code  
   - Departure Date  

3. **Airports** *(Relation to Flights):*  
   Includes data such as:  
   - Airport IATA Code  
   - City  
   - Country  
   - Continent  

4. **Hotels:**  
   Stores hotel information, including:  
   - Name  
   - Location  
   - Number of Stars  
   - Phone Number  
   - Price Range  
   - Amenities  

5. **Rooms** *(Relation to Hotels):*  
   This table contains information about the rooms available in the hotels listed in the previous table, including:  
   - Hotel ID  
   - Room Number  
   - Type (e.g., single, double, etc.)  
   - Price  
   - Status  

6. **Rental Vehicles:**  
   Stores details about vehicles available for rent, such as:  
   - Model  
   - Brand  
   - License Plate  
   - Fuel Type  
   - Type (e.g., car, van, etc.)  
   - Daily Price  

7. **Restaurants:**  
   Provides information about a list of restaurants, including:  
   - Name  
   - Address  
   - Rating  
   - Operating Hours Information  
   - Price Range  

## Issues and Solutions

### Issues

1. **Multi-query SELECT**  
   When performing searches that involve multiple tables, the system generates multiple queries.  

2. **Insertion with Records Containing Foreign Keys**  
   During data insertion, the process must handle records with foreign keys and verify relationships between tables.  

3. **Memory Management**  
   Initial memory handling caused performance issues due to the storage of static messages and excessive data.  

4. **Table and Field Descriptions**  
   For optimal functionality, the database requires detailed descriptions of tables and fields.  

---

### Solutions

1. **Multi-query SELECT**  
   - The issue was resolved by modifying the function to manage multi-queries efficiently.  
   - The generated queries are executed by the database, and their results are stored in a list.  
   - This list is then passed to the model for processing.  

2. **Insertion with Foreign Key Records**  
   - Unlike other operations, insertion requires verifying that all non-NULL data is present and that foreign key relationships are valid.  
   - This was resolved by:  
     - Extracting all related tables.  
     - Generating auxiliary SELECT queries using the LLM to find the correct foreign keys.  
     - Passing these results to the LLM to generate and execute the final INSERT query.  

3. **Improved Memory Management**  
   - Initially, memory was overloaded with static messages embedded in the code.  
   - The solution involved:  
     - Storing only the user's initial input and the LLM's final output in memory.  
     - Implementing a fixed sliding window with a LIFO structure for managing requests.  

4. **Detailed Table and Field Descriptions**  
   - The program now requires a well-designed MySQL database where every table and field is thoroughly commented.  
   - Adding detailed descriptions ensures that every element is well-documented, improving both functionality and usability.  

---
## Python Libraries Used

The following Python libraries were used in this project:

| Library                | Version  |
|------------------------|----------|
| **mysql-connector**    | 2.2.9    |
| **mysql-connector-python** | 8.1.0 |
| **openai**             | 1.57.2   |
| **pip**                | 24.3.1   |
| **python-dotenv**      | 1.0.1    |
| **requests**           | 2.32.3   |

