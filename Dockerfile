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
    && rm -rf /var/lib/apt/lists/*

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
COPY . src/vehicle_dashboard/
RUN chown -R root:root src/vehicle_dashboard/

# Default command
CMD ["bash"]
