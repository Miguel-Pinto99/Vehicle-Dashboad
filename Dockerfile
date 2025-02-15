FROM osrf/ros:noetic-desktop-full-focal

# Install bootstrap tools
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

# Install additional dependencies
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

# Setup environment
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc && \
    echo "export PATH=/opt/ros/noetic/bin:\$PATH" >> ~/.bashrc && \
    echo "export ROS_PACKAGE_PATH=/opt/ros/noetic/share:\$ROS_PACKAGE_PATH" >> ~/.bashrc && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    /bin/bash -c "source /opt/ros/noetic/setup.bash && catkin_make"

RUN chmod -R +x $ROS_WS/src

# Install additional Python packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    python3-setuptools \
    python3-virtualenv \
    python3-dev \
    build-essential \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libgstreamer1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-libav \
    gstreamer1.0-doc \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# Install Kivy for Python 3.8
RUN pip3 install kivy[base] kivy_examples \
    https://github.com/kivymd/KivyMD/archive/master.zip \
    kivy-garden \
    kivy-garden --user
