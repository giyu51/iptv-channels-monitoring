# IptvChannelsMonitoring

## Description

📺 **iptv-channels-monitoring** is a Python script built using FastAPI and VLC media player that enables monitoring and tracking of IPTV channels' activity and statistics. The script allows you to add and manage multiple channels, providing functionalities such as playing channels ▶️, updating video frames 🖼️, retrieving channel statistics 📊, and clearing channel buffers 🧹. It utilizes VLC media player's capabilities to handle various stream types, including HTTP, HTTPS, and UDP. The project aims to provide a convenient solution for monitoring IPTV channels and gathering valuable insights about their performance. 🚀

## Getting started

To begin with, download the dependencies:

### Dependencies

To run this project, you need to have the following dependencies installed:

- 🐍 [Python](https://www.python.org/downloads/): Python is a programming language used by this project.

- 📦 [pip](https://pip.pypa.io/en/stable/): pip is the package installer for Python.

- ⚡️ [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast (high-performance) web framework for building APIs with Python.

- 🦄 [Uvicorn](https://www.uvicorn.org/): Uvicorn is a lightning-fast ASGI server for running FastAPI applications.

- 📺 [VLC](https://www.videolan.org/vlc/index.html): VLC is a free and open-source multimedia player that can handle various streaming formats.

- 🐍 [vlc-python](https://pypi.org/project/python-vlc/): vlc-python is a Python binding for the VLC media player library, allowing you to interact with VLC in your Python scripts.


## Installation

#### Debian-based (e.g., Ubuntu, Debian):
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install fastapi
sudo apt install vlc
pip3 install python-vlc
pip3 install uvicorn
```
 
#### RPM-based (e.g., Fedora, CentOS, Red Hat Enterprise Linux):
```bash
sudo dnf update
sudo dnf install python3
sudo dnf install python3-pip
pip3 install --upgrade pip
pip3 install fastapi
sudo dnf install vlc
pip3 install python-vlc
pip3 install uvicorn
```

### Windows
1. Install Python:
   - Visit the [Python website](https://www.python.org/downloads/).
   - Download the latest Python installer for Windows.
   - Run the installer and follow the instructions. Make sure to check the option "Add Python to PATH" during the installation process.

2. Install pip:
   - Open the command prompt.
   - Run the following command to upgrade pip:
     ```
     python -m pip install --upgrade pip
     ```

3. Install FastAPI, Uvicorn, VLC, and vlc-python:
   - Open the command prompt.
   - Run the following command to install the necessary packages:
     ```
     pip install fastapi uvicorn python-vlc
     ```

4. Install VLC:
   - Visit the [VLC website](https://www.videolan.org/vlc/index.html).
   - Download the VLC installer for Windows.
   - Run the installer and follow the instructions.


Please make sure to install these dependencies before running the script. Follow the installation instructions for each dependency based on your operating system.





## Usage

1. **Create a CSV File:** First, create a CSV file named `all_channels.csv` and write the names and links of the channels in the following format: `<channel_name>,<channel_link>` (without any spaces). Here's an example of how it should look:
```csv
DiscoveryScience,http://example.com/DiscoveryScience
Scifi,http://example.com/Scifi
Nickelodeon,http://example.com/Nickelodeon
```


2. **Run the ASGI Server:** Use `uvicorn` to run the ASGI server for the application. Open your terminal and navigate to the project directory. 
    Run the following command to start the server:
   - If you want to run the server on the default host and port (localhost:8000), use:
     ```
     uvicorn <your_app_name>:app
     ```

   - If you want to make the server accessible on all interfaces, use:
     ```
     uvicorn <your_app_name>:app --host 0.0.0.0
     ```
   
   - If you want to specify a custom port, use:
     ```
     uvicorn <your_app_name>:app --port <your_port>
     ```

   Replace `<your_app_name>` with the name of your Python application file (without .py).

3. **Access the Application:** Once the server is running, you can access the application by opening a web browser and navigating to `http://localhost:8000`   (replace the port number if you specified a custom port).

   The application provides various endpoints for monitoring and interacting with the IPTV channels. Refer to the API documentation or code comments for more details on available endpoints and their functionalities.

   Following URLs are available:

   - Stats of All Channels: Visit 
   ```
   http://localhost:8000/stats
   ```
    to view the statistics of all channels collectively.

   - Stats of a Specific Channel: To analyze the statistics of a specific channel, replace <channel_name> in the URL 
   ```
   http://localhost:8000/stats/<channel_name>
   ```
    with the desired channel's name.

   - Current Image Frame of a Channel: For accessing the current image frame of a channel, go to 
   
   ```
   http://localhost:8000/screen/<channel_name>
   ```
   Replace <channel_name> with the name of the channel you wish to view.


Please note that you need to have the required dependencies installed and properly configured before running the application.




## 👥 Authors

- [rio51](https://github.com/rio51) - Primary Author

## 🙏 Acknowledgments

- Thanks to [@someone](https://github.com/someone) for the idea and inspiration to create this project.


## Project Status

✅ This project has been successfully completed and is ready for use. All the desired features have been implemented, and the script is fully functional. You can now monitor IPTV channels, track their activity and statistics, and perform various operations such as playing channels, updating video frames, retrieving channel statistics, and clearing channel buffers. Feel free to use and customize this script according to your specific requirements.

🐛 If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

🎉 Happy monitoring! 📺🔍📊

