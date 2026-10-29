# Autonomous LiDAR-Based Construction Robot Software

A capstone project for the 2026–2027 NASA Lunabotics Challenge.

**Course:** COMP/IT 491 — Capstone Preparation  
**University:** California State University Channel Islands  
**Department:** Computer Science & Mechatronics  
**Advisors:** Dr. Reza Abdolee & Dr. Vida Vakilian

## Team Members

- Joaquin Gutierrez
- Emma Schwartz
- Salam Khalaf
- David Persoon

## Vocabulary Overview

- **Regolith:** Loose surface material, including dust, soil, and rock fragments. The competition uses a lunar regolith simulant.
- **Berm:** A long mound of material that acts as a barrier.

## Project Overview and Problem Statement

Our team plans to build a robot that digs up regolith, carries it across an obstacle field, and places it in a specific zone to construct a berm. The project is being developed for **NASA's Lunabotics Challenge**.

The robot will need to operate on loose terrain while avoiding rocks and craters. Our main software challenge is to use LiDAR and other sensors to let the robot locate itself, choose a safe route, dig up regolith, and construct a berm with it. Accurate position tracking is especially important because the robot needs to travel between designated excavation and construction zones and place material within the berm's target area.

## Goals and Objectives

1. Develop Mission Control software to send commands and display the robot's status (position, battery level, faults) and camera feed.
2. Automate regolith placement at the berm.
3. Automate digging and regolith collection.
4. Automate navigation using LiDAR and sensor data.
5. Integrate these functions so the robot can complete repeated construction cycles autonomously.

We will use unit tests to check individual software components and integration tests to check how they work together. Repeated simulation and physical testing will help us evaluate reliability.

## Proposed Features and System Components

- Motors, wheels, and motor controllers
- Excavation system
- Regolith storage and dumping system
- LiDAR sensor for obstacle detection, mapping, and navigation
- Wheel encoders for measuring wheel rotation; infrared sensors are also being evaluated for wheel sensing. Slip detection will require comparing wheel movement with an independent estimate of robot movement.
- Onboard computer for sensor data processing, navigation, and mission logic
- Microcontroller for reading sensors, controlling motors through motor drivers, and exchanging commands and feedback with the onboard computer
- Mission state machine to track the current task and coordinate digging, travel, dumping, and returning
- Mission Control interface and wireless link
- Battery, power distribution, and emergency stop

Hardware models, sensor placement, and mechanical designs are still being evaluated. A Raspberry Pi 5 is under consideration for the onboard computer; the final choice will depend on the sensor workload and performance tests.

## Planned Technologies and Tools

| Technology or tool | Planned use |
| --- | --- |
| ROS 2 | Connect sensor processing, navigation, mission logic, and robot control. |
| Gazebo | Simulate the robot, LiDAR, terrain, and obstacles before physical integration. |
| Nav2 | Evaluate existing tools for route planning, obstacle avoidance, and navigation control. |
| Python and C++ | Develop ROS 2 nodes, mission logic, hardware interfaces, and supporting tools. |
| Git and GitHub | Manage source code, track issues, and maintain project documentation. |

## Initial Implementation Plan and Timeline

We will develop the mechanical hardware and software in parallel. Simulation will allow software progress to continue while physical components are being selected and assembled.

| Period | Planned work | Status |
| --- | --- | --- |
| October 2026 | Review requirements, complete initial planning, and establish a ROS 2/Gazebo LiDAR simulation. | Completed |
| November 2026 | Select the preliminary robot design and prepare the Preliminary Design Review Report. | Planned |
| December 2026 | Build and test mechanical prototypes for driving, digging, and dumping. | Planned |
| January 2027 | Integrate electronics, motor control, sensors, and Mission Control. | Planned |
| February 2027 | Demonstrate a complete construction cycle under remote control and begin task automation. | Planned |
| March 2027 | Develop automated dumping, digging, and navigation; connect them through the mission state machine. | Planned |
| April 2027 | Run repeated tests, address failures, and complete competition documentation. | Planned |
| May 2027 | Perform final checks and prepare for competition participation, subject to selection and readiness. | Planned |
