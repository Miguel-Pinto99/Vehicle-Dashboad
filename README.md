# Thesis project from Miguel Pinto 2022

## Context

Repository which contains all the work developed during my masters thesis. The project consisted on a dynamic dashboard for an autonomous research vehicle of the University of Aveiro.

https://github.com/user-attachments/assets/24c1fa54-379a-4160-af00-b8634bc3b058

The dashboard served as a display that enabled communication between the ATLASCAR2 and the driver, updating the driver in real-time with all data related to the vehicle on a dynamic screen, thereby enhancing the driver’s situational awareness.

The information relative to the car was present at the CAN-Bus of the vehicle. Therefore a ROS network was created with 3 nodes and 2 topics. A node was responsabile for receiving and decrying the messages using a OBD-II port connection and then the data would be published into a topic.  Other node creates warnings by analysing info such as doors or the charger state. Finnaly a third node would be responsable for the front-end logic. The display for the project was developed using Kivy, a Python library for developing multitouch applications.

Most information was related to the car’s original features, such as autonomy and velocity. Warnings and notifications were also added.

Link to final document: http://lars.mec.ua.pt/public/LAR%20Projects/SystemDevelopment/2022_MiguelPinto/

|                                                ATLASCAR2                                                |                                                   Field test                                                   |
| :-----------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------: |
| ![Final-ATLASCAR2-setup](https://github.com/user-attachments/assets/dc30f2cb-7cc8-4a2e-a729-0749d2315579) | ![Screenshot 2024-10-19 165427](https://github.com/user-attachments/assets/fc2b7229-ccbb-4928-85af-0701fa53b4e5) |

## ROS Network

The network is composed of three nodes and two topics. The can node is responsible for reading and processing the CAN messages. Therefore, it is a vital structure since it feeds information
to the network. The node publishes data in a topic named can messages which uses a custom message named can msgs, created to facilitate communication between the different modules. The topic is then subscribed by two nodes: warning node and dashboard node. The first is responsible for generating the dashboard alerts. Their state is available in a separate topic called warning messages, which also uses a custom message named warning msgs. Finally, the dashboard node subscribes at the same time the can messages and warning messages topics. It is responsible for gathering all parameters from the network and displaying them in a dynamic layout created with the Kivy library. The custom messages were constructed according to the sent parameters in each node. If a node sends twenty variables, the custom message has the same number of fields, each designed for a specific variable.

![Screenshot 2024-10-19 172207](https://github.com/user-attachments/assets/da0671ca-cc1f-41d9-a417-de4d67e222a9)

## Requirements

```
- Python 3.x
- ROS (Communication protocol)
- can-utils (To get the data from the CAN bus)
- Kivy (To launch the front-end)
```

## Launch

Run the package in the termal using the launch file:

```
roslaunch dashboard dashboard.launch
```
