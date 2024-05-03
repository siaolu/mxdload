#!/bin/bash
# buildrun.sh
# Version 5.0

IMAGE_NAME="mxdload"
CONTAINER_NAME="mxdload_contain"
LOG_FILE="buildrun.log"

function log_execution_time() {
    local function_name=$1
    local start_time=$2
    local end_time=$(date +%s)
    local execution_time=$((end_time - start_time))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Function: $function_name, Execution Time: $execution_time seconds" >> $LOG_FILE
}

function build_and_run() {
    local start_time=$(date +%s)
    echo "Building Docker image..."
    docker build -t $IMAGE_NAME . || { echo "Docker build failed, exiting."; exit 1; }
    echo "Docker image built successfully."
    echo "Running Docker container..."
    docker run -d --name $CONTAINER_NAME -p 80:80 -v $(pwd)/downloads:/app/downloads $IMAGE_NAME || { echo "Docker run failed, exiting."; exit 1; }
    echo "Container started successfully."
    log_execution_time "${FUNCNAME[0]}" $start_time
}

function stop_and_remove_container() {
    local start_time=$(date +%s)
    echo "Stopping container..."
    docker stop $CONTAINER_NAME || { echo "Docker stop failed, exiting."; exit 1; }
    echo "Removing container..."
    docker rm $CONTAINER_NAME || { echo "Docker remove failed, exiting."; exit 1; }
    log_execution_time "${FUNCNAME[0]}" $start_time
}

function restart_container() {
    local start_time=$(date +%s)
    echo "Restarting Docker container..."
    docker restart $CONTAINER_NAME || { echo "Docker restart failed, exiting."; exit 1; }
    echo "Container restarted successfully."
    log_execution_time "${FUNCNAME[0]}" $start_time
}

function flush_environment() {
    local start_time=$(date +%s)
    echo "Flushing environment: Removing all containers and images..."
    docker rm $(docker ps -aq) 2>/dev/null || true
    docker rmi $(docker images -aq) 2>/dev/null || true
    echo "Environment flushed successfully."
    log_execution_time "${FUNCNAME[0]}" $start_time
}

echo "Select an option:"
echo "1) Build and Run"
echo "2) Stop and Remove Container"
echo "3) Restart Container"
echo "4) Flush Environment"
echo "5) Exit"

read -p "Enter choice: " choice

case $choice in
    1) build_and_run ;;
    2) stop_and_remove_container ;;
    3) restart_container ;;
    4) flush_environment ;;
    5) echo "Exiting..." ;;
    *) echo "Invalid choice, exiting." ;;
esac