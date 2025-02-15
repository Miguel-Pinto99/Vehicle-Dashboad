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

# Install Python 3.8
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.8 \
    python3.8-dev \
    python3.8-venv \
    && rm -rf /var/lib/apt/lists/*

# Update alternatives to use Python 3.8
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

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

RUN pip3 install kivy[base] kivy_examples kivymd kivy-garden kivy_garden.mapview
