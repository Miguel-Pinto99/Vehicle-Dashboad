# Thesis project from Miguel Pinto 2022

## Description

Repository which contains all the work developed during my thesis. The project consists of a dynamic dashboard for an autonomous research vehicle of the University of Aveiro. The information relative to the car was present at the CAN-Bus of the vehicle. Therefore a ROS node was responsible for receiving and decrying it. Then the information was published to a topic which is then subscribed by the dashboard software. As the software feeds the dashboard with information, an interactive display kept the driver updated on the vehicle’s current state. 

Link to final document: http://lars.mec.ua.pt/public/LAR%20Projects/SystemDevelopment/2022_MiguelPinto/

https://github.com/user-attachments/assets/24c1fa54-379a-4160-af00-b8634bc3b058

## Deployment

https://github.com/user-attachments/assets/799038b2-bb0b-4702-9081-312c209ba202



To run the application, the following software/libraries are needed

```
1- ROS - Robotic Operating System (Communication protocol)
2- can-utils (To get the data from the CAN bus)
3- Kivy (To launch the front-end)
```

## Launch

Run the package in the termal using the launch file:

```
roslaunch dashboard dashboard.launch
```



