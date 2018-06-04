# 0x05. Processes and signals

## What you should learn from this project

This project begins the system engineering and dev-ops track
At the end of this project we are expected to be able to explain, without the help of Google:

- What is a PID
- What is a process
- How to find a process PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
- The first line of all Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all Bash scripts should be a comment explaining what is the script doing

## Project

- Write a Bash script that displays its PID.

- Write a Bash script that displays a list of currently running processes.

- write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process

- Write a Bash script that displays the PID, along with the process name, of processes which name contains the word bash.

- Write a Bash script that displays To infinity and beyond indefinitely.

- Write a Bash script that kills 4-to_infinity_and_beyond process.

- Write a Bash script that kills 4-to_infinity_and_beyond process. (Cannot use kill or killall)

- Write a Bash script that displays:

  - To infinity and beyond indefinitely
  - With a sleep 2 in between each iteration
  - I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

- Write a Bash script that kills the process 7-highlander.
