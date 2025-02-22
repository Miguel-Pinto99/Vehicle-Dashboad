# Thesis project from Miguel Pinto 2022

## Context

Repository which contains all the work developed during my masters thesis. The project consisted on a dynamic dashboard for an autonomous research vehicle of the University of Aveiro.

https://github.com/user-attachments/assets/24c1fa54-379a-4160-af00-b8634bc3b058

## Requirements

- [Docker](https://docs.docker.com/): To containerize the application and manage dependencies.

## Launch

To start the application:

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
1. Navigate to the main directory:
    ```sh
    cd Vehicle-Dashboard
    ```
1. Run the following command in the terminal:
    ```sh
    docker-compose up
    ```

1. To play with the variables in real-time, navigate to the `/can_messages` topic in the rqt window (It will open automatically), tick the box next to `/can_messages`, and change the variables.
## Description

The dashboard served as a display that enabled communication between the ATLASCAR2 and the driver, updating the driver in real-time with all data related to the vehicle on a dynamic screen, thereby enhancing the driver’s situational awareness.

|                                                ATLASCAR2                                                |                                                   Field test                                                   |
| :-----------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------: |
| ![Final-ATLASCAR2-setup](https://github.com/user-attachments/assets/dc30f2cb-7cc8-4a2e-a729-0749d2315579) | ![Screenshot 2024-10-19 165427](https://github.com/user-attachments/assets/fc2b7229-ccbb-4928-85af-0701fa53b4e5) |


The information relative to the car was present at the CAN-Bus of the vehicle. Therefore a ROS network was created with several nodes and topics. A node was responsabile for receiving and decrying the messages using a OBD-II port connection and then the data would be published into a topic.  Other node creates warnings by analysing info such as doors or the charger state. Finnaly a third node would be responsable for the front-end logic. The display for the project was developed using Kivy, a Python library for developing multitouch applications. Most information was related to the car’s original features, such as autonomy and velocity. Warnings and notifications were also added.

![Screenshot 2024-10-19 172207](https://github.com/user-attachments/assets/da0671ca-cc1f-41d9-a417-de4d67e222a9)

Link to final document: http://lars.mec.ua.pt/public/LAR%20Projects/SystemDevelopment/2022_MiguelPinto/
