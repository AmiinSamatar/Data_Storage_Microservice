# Data Storage Microservice


## Description: 
The microservice we have implemented is a vehicle data storage and retrieval system. Its primary purpose is to electronically document and manage information related to vehicles. The microservice provides two main functionalities: adding a new vehicle to the database and retrieving a list of all vehicles stored in the system.

Communication Contract for Requesting and Receiving Data from the Microservice:

### 1.Timely Communication:
-We will initiate dialog as early as possible to discuss the requirements of the microservice and any potential challenges.
-Efficient and straight-to-the-point discussions will be encouraged to make decisions effectively.

### 2.Detailed Discussions:
-We will have more detailed discussions about the microservice implementation, including its functionalities and endpoints.
-This will help ensure a clear understanding of each other's tasks and avoid any confusion or misunderstandings.

### 3.Sharing Workload:
-We will openly discuss any concerns about the complexity of the microservice and find ways to support each other.
-If needed, we can distribute the workload more effectively based on individual expertise and availability.

### 4.Requesting Data from the Microservice:
-The requester will programmatically send a request to the microservice using Python's requests library.
-The request will be made to the appropriate endpoint of the microservice, such as ```LINK/add_vehicle or /get_vehicles.```.
Necessary data and parameters, such as vehicle details for adding or retrieving, will be included in the request.

### 5.Receiving Data from the Microservice:
-The requester will handle the response received from the microservice programmatically.
-After sending a request, the requester will use Python's requests library to receive the response from the microservice.
-If successful, the response will contain the requested data, which can be extracted and used by the requester.

## UML:
![image](https://github.com/AmiinSamatar/Data_Storage_Microservice/assets/138237129/fd744c33-f742-4113-8860-d400c9a633c1)

In the diagram, the client sends a POST request to the /add_vehicle endpoint with the vehicle data in JSON format. The microservice processes the request, adds the new vehicle to the database, and responds with a status code 201 (Created) if the addition is successful.

Similarly, the client sends a GET request to the /get_vehicles endpoint to retrieve the list of all vehicles. The microservice processes the request, fetches the data from the database, and responds with a status code 200 (OK) along with the list of vehicles in JSON format.
