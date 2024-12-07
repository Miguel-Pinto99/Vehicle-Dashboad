# Use an official ROS base image
FROM osrf/ros:noetic-desktop-full

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_VERSION=noetic
ENV ROS_DISTRO=noetic

# Update and install basic dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    python3 \
    python3-pip \
    python3-colcon-common-extensions \
    ros-$ROS_DISTRO-catkin \
    && rm -rf /var/lib/apt/lists/*

# Install rospy and other Python dependencies
RUN apt-get update && apt-get install -y \
    python3-rospy \
    && rm -rf /var/lib/apt/lists/*

# Install python-can
RUN pip3 install python-can

# Set up ROS workspace
WORKDIR /root
RUN mkdir -p catkin_ws/src
WORKDIR /root/catkin_ws
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && catkin_make"

# Source ROS setup in bashrc
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
RUN echo "source /root/catkin_ws/devel/setup.bash" >> ~/.bashrc

# Expose ROS master port
EXPOSE 1131
COPY . /root/catkin_ws/src/
# RUN chmod +x /root/catkin_ws/src/can_publisher.py
# RUN chmod +x /root/catkin_ws/src/can_publisher.py
# RUN chmod +x /root/catkin_ws/src/can_publisher.py

# Start roscore on container startup
CMD ["bash", "-c", "source /opt/ros/noetic/setup.bash && source /root/catkin_ws/devel/setup.bash && roscore"]
