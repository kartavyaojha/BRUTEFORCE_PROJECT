# BRUTEFORCE_PROJECT

## Brute Force Testing Project

This project includes a Python script for brute force testing and a Flask web server that simulates a login endpoint with rate limiting.

## Project Structure

- **`exploit.py`**: Brute force script for attempting login with different username and password combinations.
- **`server.py`**: Flask server script that simulates a login endpoint with rate limiting.
- **`username.txt`**: Text file containing a list of usernames.
- **`password.txt`**: Text file containing a list of passwords.
- **`setup.py`**: Script to install the required Python packages.

## Requirements

To run this project, you'll need Python installed on your system. This project requires the following Python packages:

- `requests`
- `pyfiglet`
- `termcolor`
- `Flask`

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kartavyaojha/BRUTEFORCE_PROJECT
   cd BRUTEFORCE_PROJECT

    Install Dependencies

    Run the following command to install the required packages:

    python setup.py install

Running the Server

To start the Flask server, use the following command:
```bash

python server.py
```

The server will be available at http://127.0.0.1:5000.
Running the Brute Force Script

To run the brute force script, use the following command:

```bash

python exploit.py
```

You will be prompted to enter the URL of the login page and the paths to the username and password files.
Configuration
server.py

    RATE_LIMIT: Maximum number of login attempts allowed from a single IP address within a TIME_WINDOW.
    TIME_WINDOW: Time window (in seconds) during which the rate limit applies.

exploit.py

    rate_limit: Number of requests per second the script will make.
    num_threads: Number of threads used to perform login attempts.

Testing

    Ensure that the Flask server is running.
    Execute the brute force script and provide the required inputs.


This project is intended for educational purposes only. Use it responsibly and with permission.


This script installs the required dependencies for the project. Save this script to install_dependencies.py and run it with:

```bash

python setup.py

```





