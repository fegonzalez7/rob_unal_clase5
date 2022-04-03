# The phantom revenge
## Requirements

## The all mighty RTB for python 

We have used the Matlab RTB, but you know Matlab, so lets install the python version.

Open a terminal and run:

```sh
sudo apt install python3-pip
pip3 install roboticstoolbox-python
pip install simpy
```

Check the following sources:
 - [**RTB Python repo**](https://github.com/petercorke/robotics-toolbox-python)
 - [**RTB Python help**](https://petercorke.github.io/robotics-toolbox-python/index.html) 
 - [**Spatial math repo**](https://github.com/petercorke/spatialmath-python)
 - [**Spatial math help**](https://petercorke.github.io/spatialmath-python/)

Definitely *Peter Corke is so pro*, I printed a poster of him :laughing:.

## Python RTB usage

Let's create a python script:

```python
import roboticstoolbox as rtb
from spatialmath import SE3

robot = rtb.DHRobot([rtb.RevoluteDH(a=1),rtb.RevoluteDH(a=1)],name="2R")
print(robot)
robot.plot([0.75,0.26])
input()
```

[![Screenshot-from-2022-04-03-00-57-57.png](https://i.postimg.cc/4dbmg5Qz/Screenshot-from-2022-04-03-00-57-57.png)](https://postimg.cc/phr2QK7T)

Run the *px_rtb.py* script and check if you obtain the a real PhantomX model.

**Activity:** Create a notebook and follow the same pipeline presented in *px_rtb.py*. What does happen with the figures? :grimacing:

------------

`<Lab guide>` : soon
------------

**Acknowledgments:**

 - Jose Manuel Fajardo
 - Sebastian Realpe 

This repo has taken a lot of effort, so consider to leave a star, [follow me](https://felipeg17.github.io/index.html), and if you feel generous I have [Paypal](https://paypal.me/fegonzalez17?country.x=CO&locale.x=en_US) (just kidding).