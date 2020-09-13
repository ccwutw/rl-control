# RL-Control

RL-Control is an example environment to simulate a network control system  with Reinforcement Learning algorithms

## Prerequisite
### Linux/Windows Machine:
Ubuntu 18.04 or later
Windows 7 or later

### Install SUMO v1.6.0:
```
sudo add-apt-repository ppa:sumo/stable
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
echo 'export SUMO_HOME="/usr/share/sumo"' >> ~/.bashrc
source ~/.bashrc
```
Test SUMO:
```
$ sumo --version
```

Output:
Eclipse SUMO Version 1.6.0
Build features: Linux-4.4.0-178-generic x86_64 GNU 7.5.0 None Proj GUI SWIG GDAL GL2PS Copyright (C) 2001-2020 German Aerospace Center (DLR) and others; https://sumo.dlr.de


### Install RL packages
```
pip install numpy
pip install tensorflow==1.13.1
```

## Run
```
python sumotest.py
```

