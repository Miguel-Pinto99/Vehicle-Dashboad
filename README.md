# Thesis project from Miguel Pinto 2022

## Context

Repository which contains all the work developed during my masters thesis. The project consisted on a dynamic dashboard for an autonomous research vehicle of the University of Aveiro.

https://github.com/user-attachments/assets/24c1fa54-379a-4160-af00-b8634bc3b058

The dashboard was a display which enabled communication between the ATLASCAR2 and the driver who was updated live with all data related to the vehicle on a dynamic screen, enhancing the driver’s sense of security and joy while. In general, they are a considered passive ADAS since they are used mostly to check information and therefore they do not have a direct interference in the driving experience.

The information relative to the car was present at the CAN-Bus of the vehicle. Therefore a ROS node was created in order to receiving and decrying the messages in it. Then the information was published to a ROS topic which is then subscribed by the dashboard software.

Most information was related to the car’s original features, such as autonomy and velocity. Warnings and notifications were also added.

Link to final document: http://lars.mec.ua.pt/public/LAR%20Projects/SystemDevelopment/2022_MiguelPinto/

ATLASCAR2             |  Field test
:-------------------------:|:-------------------------:
![Final-ATLASCAR2-setup](https://github.com/user-attachments/assets/dc30f2cb-7cc8-4a2e-a729-0749d2315579)  |  ![Screenshot 2024-10-19 165427](https://github.com/user-attachments/assets/fc2b7229-ccbb-4928-85af-0701fa53b4e5)

## Deployment

To run the application, the following software/libraries are needed:

```
1- ROS (Communication protocol)
2- can-utils (To get the data from the CAN bus)
3- Kivy (To launch the front-end)
```

## Launch

Run the package in the termal using the launch file:

```
roslaunch dashboard dashboard.launch
```

## ROS Network
The network is composed of three nodes and two topics. The can node is responsible for reading and processing the CAN messages. Therefore, it is a vital structure since it feeds information 
to the network. The node publishes data in a topic named can messages which uses a custom message named can msgs, created to facilitate communication between the different modules. The topic is then subscribed by two nodes: warning node and dashboard node. The first is responsible for generating the dashboard alerts. Their state is available in a separate topic called warning messages, which also uses a custom message named warning msgs. Finally, the dashboard node subscribes at the same time the can messages and warning messages topics. It is responsible for gathering all parameters from the network and displaying them in a dynamic layout created with the Kivy library. The custom messages were constructed according to the sent parameters in each node. If a node sends twenty variables, the custom message has the same number of fields, each designed for a specific variable.

![Screenshot 2024-10-19 172207](https://github.com/user-attachments/assets/da0671ca-cc1f-41d9-a417-de4d67e222a9)





