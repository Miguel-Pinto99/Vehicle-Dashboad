# Thesis project from Miguel Pinto 2022

## Description

Repository which contains all the work developed during my thesis. The project consists of a dynamic dashboard for an autonomous research vehicle of the University of Aveiro. The information relative to the car was present at the CAN-Bus of the vehicle. Therefore a ROS node was responsible for receiving and decrying it. Then the information was published to a topic which is then subscribed by the dashboard software. As the software feeds the dashboard with information, an interactive display kept the driver updated on the vehicle’s current state. 

Link to final document: http://lars.mec.ua.pt/public/LAR%20Projects/SystemDevelopment/2022_MiguelPinto/

https://github.com/user-attachments/assets/24c1fa54-379a-4160-af00-b8634bc3b058

## Context

A dashboard is a HMI. It consists of a panel that enables communication with amachine. On its screen, touch buttons are presented so the operator can easily navigate through its display. They are a considered passive ADAS since they are used mostly to check information and do not have a direct interference in the driving experience. It is important to dive into some aspects of this hardware to understand how it operates.

The ATLASCAR2 is commonly used by investigators worldwide for autonomous driving projects, and much work has been done in this field. The dashboard must be capable of reading the messages received from the automobile and processing them Most information will be related to the car’s original features, such
as autonomy and velocity As the software feeds the dashboard with information, an interactive display will keep the driver updated on the vehicle’s current state. The user must be capable of easily communicating with the machine by incorporating a user-friendly interface


## Deployment

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



