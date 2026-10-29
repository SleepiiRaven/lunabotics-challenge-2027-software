#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$SCRIPT_DIR/ros2"

cd "$WORKSPACE_DIR"
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install --build-base build_modular --install-base install_modular
source install_modular/setup.bash

ros2 launch lunabotics_sim gazebo_model.launch.py &
SIM_PID=$!

cleanup() {
    if kill -0 "$SIM_PID" 2>/dev/null; then
        kill -INT "$SIM_PID" 2>/dev/null || true
        wait "$SIM_PID" || true
    fi
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

echo "Waiting for the robot to publish joint states..."
if ! timeout 60s ros2 topic echo --once /joint_states >/dev/null; then
    echo "No joint states received; check the Gazebo and spawn messages above."
    kill -INT "$SIM_PID" 2>/dev/null || true
    wait "$SIM_PID" || true
    exit 1
fi

echo "Running wheel_test.py..."
python3 "$WORKSPACE_DIR/wheel_test.py"

echo "Wheel test finished. Gazebo is still running; press Ctrl+C to exit."
wait "$SIM_PID"
