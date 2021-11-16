#!/usr/bin/env python3
"""
Basic demo with joints!
source: https://mujoco.readthedocs.io/en/latest/overview.html
source: https://github.com/openai/mujoco-py/blob/master/examples/body_interaction.py
"""
from mujoco_py import load_model_from_xml, MjSim, MjViewer
import math
import os

MODEL_XML = """
<?xml version="1.0" ?>
<mujoco model="example">
    <compiler coordinate="global"/>
    <default>
        <geom rgba=".8 .6 .4 1"/>
    </default>
    <asset>
        <texture type="skybox" builtin="gradient" rgb1="1 1 1" rgb2=".6 .8 1"
                 width="256" height="256"/>
    </asset>
    <worldbody>
        <light pos="0 1 1" dir="0 -1 -1" diffuse="1 1 1"/>
        <body>
            <geom type="capsule" fromto="0 0 1  0 0 0.6" size="0.06"/>
            <joint type="ball" pos="0 0 1"/>
            <body>
                <geom type="capsule" fromto="0 0 0.6  0.3 0 0.6" size="0.04"/>
                <joint type="hinge" pos="0 0 0.6" axis="0 1 0"/>
                <joint type="hinge" pos="0 0 0.6" axis="1 0 0"/>
                <body>
                    <geom type="ellipsoid" pos="0.4 0 0.6" size="0.1 0.08 0.02"/>
                    <site name="end1" pos="0.5 0 0.6" type="sphere" size="0.01"/>
                    <joint type="hinge" pos="0.3 0 0.6" axis="0 1 0"/>
                    <joint type="hinge" pos="0.3 0 0.6" axis="0 0 1"/>
                </body>
            </body>
        </body>
        <body>
            <geom type="cylinder" fromto="0.5 0 0.2  0.5 0 0" size="0.07"/>
            <site name="end2" pos="0.5 0 0.2" type="sphere" size="0.01"/>
            <joint type="free"/>
        </body>
    </worldbody>
    <tendon>
        <spatial limited="true" range="0 0.6" width="0.005">
            <site site="end1"/>
            <site site="end2"/>
        </spatial>
    </tendon>
</mujoco>
"""

model = load_model_from_xml(MODEL_XML)
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    # sim.data.ctrl[0] = math.cos(t / 10.) * 0.01
    # sim.data.ctrl[1] = math.sin(t / 10.) * 0.01
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
