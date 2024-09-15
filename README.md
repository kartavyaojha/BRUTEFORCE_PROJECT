# BRUTEFORCE_PROJECT
# Brute Force Testing Project

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

   
   git clone <repository_url>
   cd <repository_directory>

    Install Dependencies

    Run the following command to install the required packages:

    python setup.py

Running the Server

To start the Flask server, use the following command:


python server.py

The server will be available at http://127.0.0.1:5000.
Running the Brute Force Script

To run the brute force script, use the following command:

python exploit.py

You will be prompted to enter the URL of the login page, and the paths to the username and password files.
Configuration


Testing

    Ensure that the Flask server is running.
    Execute the brute force script and provide the required inputs.



exploit.py

This script performs a brute force attack by iterating over usernames and passwords. It supports rate limiting to avoid excessive requests.

server.py

This Flask server simulates a login endpoint with rate limiting. Adjust the RATE_LIMIT and TIME_WINDOW variables to configure the rate limiting behavior.


