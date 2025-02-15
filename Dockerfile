FROM osrf/ros:noetic-desktop-full-focal

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    python3-rosdep \
    python3-pip \
    python3-rosinstall \
    python3-vcstools \
    python3-tk \
    python3-can \
    && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install --no-install-recommends -y \
#     python3-kivy \
#     kivy-examples \
#     && rm -rf /var/lib/apt/lists/*

# install aditional dependencies
RUN apt-get update && apt-get install -y vim \
    ros-noetic-ros-numpy \
    ros-noetic-rviz-visual-tools

# Initialize rosdep
RUN rosdep init || true && rosdep update

# Define the ROS workspace
ENV ROS_WS=/root/catkin_ws

# Create workspace and set as working directory
WORKDIR $ROS_WS
RUN mkdir -p src

# Copy source code
COPY . src/
RUN chown -R root:root src/

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "export PATH=/opt/ros/noetic/bin:\$PATH" >> ~/.bashrc
RUN echo "export ROS_PACKAGE_PATH=/opt/ros/noetic/share:\$ROS_PACKAGE_PATH" >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
RUN /bin/bash -c "source ~/.bashrc"
RUN echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && catkin_make"

RUN chmod -R +x $ROS_WS/src
