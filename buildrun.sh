#!/bin/bash
# buildrun.sh
# Version 5.3

IMAGE_NAME="mxdload"
CONTAINER_NAME="mxdload_contain"
LOG_FILE="buildrun.log"

function log_operation() {
    local operation=$1
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Operation: $operation" >> $LOG_FILE
}

function log_execution_time() {
    local function_name=$1
    local start_time=$2
    local end_time=$(date +%s)
    local execution_time=$((end_time - start_time))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Function: $function_name, Execution Time: $execution_time seconds" >> $LOG_FILE
}

function build_and_run() {
    local start_time=$(date +%s)
    log_operation "Building Docker image"
    docker build -t $IMAGE_NAME . || { echo "Docker build failed, exiting."; exit 1; }
    log_operation "Docker image built successfully"
    
    local container_exists=$(docker ps -aq -f name=^/$CONTAINER_NAME$)
    if [ -n "$container_exists" ]; then
        read -p "Container '$CONTAINER_NAME' already exists. Do you want to flush it? (y/n): " flush_choice
        log_operation "User prompted to flush existing container '$CONTAINER_NAME'"
        if [ "$flush_choice" == "y" ] || [ "$flush_choice" == "Y" ]; then
            log_operation "User chose to flush container '$CONTAINER_NAME'"
            docker rm -f $CONTAINER_NAME
            log_operation "Container '$CONTAINER_NAME' flushed"
        else
            log_operation "User chose not to flush container '$CONTAINER_NAME'"
            local counter=1
            while [ -n "$(docker ps -aq -f name=^/${CONTAINER_NAME}_${counter}$)" ]; do
                ((counter++))
            done
            CONTAINER_NAME="${CONTAINER_NAME}_${counter}"
            log_operation "New container name: '$CONTAINER_NAME'"
        fi
    fi
    
    log_operation "Running Docker container '$CONTAINER_NAME'"
    docker run -it --name $CONTAINER_NAME -v $(pwd)/downloads:/app/downloads $IMAGE_NAME /bin/bash -c "python main.py; read -p 'Press Enter to exit...'"
    log_operation "Container '$CONTAINER_NAME' exited"
    log_execution_time "${FUNCNAME[0]}" $start_time
    

}

function stop_and_remove_container() {
    local start_time=$(date +%s)
    log_operation "Stopping container '$CONTAINER_NAME'"
    docker stop $CONTAINER_NAME || { echo "Docker stop failed, exiting."; exit 1; }
    log_operation "Container '$CONTAINER_NAME' stopped"
    log_operation "Removing container '$CONTAINER_NAME'"
    docker rm $CONTAINER_NAME || { echo "Docker remove failed, exiting."; exit 1; }
    log_operation "Container '$CONTAINER_NAME' removed"
    log_execution_time "${FUNCNAME[0]}" $start_time
}

function restart_container() {
    local start_time=$(date +%s)
    log_operation "Restarting Docker container '$CONTAINER_NAME'"
    docker restart $CONTAINER_NAME || { echo "Docker restart failed, exiting."; exit 1; }
    log_operation "Container '$CONTAINER_NAME' restarted successfully"
    log_execution_time "${FUNCNAME[0]}" $start_time
}

function flush_environment() {
    local start_time=$(date +%s)
    log_operation "Flushing environment: Removing all containers and images"
    docker rm $(docker ps -aq) 2>/dev/null || true
    docker rmi $(docker images -aq) 2>/dev/null || true
    log_operation "Environment flushed successfully"
    log_execution_time "${FUNCNAME[0]}" $start_time
}

function display_menu() {
    echo "Select an option:"
    echo "1) Build and Run"
    echo "2) Stop and Remove Container"
    echo "3) Restart Container"
    echo "4) Flush Environment"
    echo "5) Exit"

    read -p "Enter choice: " choice
    log_operation "User selected option: $choice"

    case $choice in
        1) build_and_run ;;
        2) stop_and_remove_container ;;
        3) restart_container ;;
        4) flush_environment ;;
        5) echo "Exiting..." ;;
        *) echo "Invalid choice, exiting." ;;
    esac
}

display_menu