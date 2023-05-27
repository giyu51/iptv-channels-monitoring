# IptvChannelsMonitoring

## Description

📺 **iptv-channels-monitoring** is a Python script built using FastAPI and VLC media player that enables monitoring and tracking of IPTV channels' activity and statistics. The script allows you to add and manage multiple channels, providing functionalities such as playing channels ▶️, updating video frames 🖼️, retrieving channel statistics 📊, and clearing channel buffers 🧹. It utilizes VLC media player's capabilities to handle various stream types, including HTTP, HTTPS, and UDP. The project aims to provide a convenient solution for monitoring IPTV channels and gathering valuable insights about their performance. 🚀

## Getting started

To begin with, download the dependencies:

### Dependencies
- Python >= 3.7
- Python packages:
  - FastAPI
  - python-vlc
- VLC media player

#### Debian-based (e.g., Ubuntu, Debian):
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install fastapi
sudo apt install vlc
pip3 install python-vlc
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
```




## Usage

## Usage

1. **Create a CSV File:** First, create a CSV file named `all_channels.csv` and write the names and links of the channels in the following format: `<channel_name>,<channel_link>` (without any spaces). Here's an example of how it should look:
```csv
DiscoveryScience,http://example.com/DiscoveryScience
Scifi,http://example.com/Scifi
Nickelodeon,http://example.com/Nickelodeon
```


2. **Run the ASGI Server:** Use `uvicorn` to run the ASGI server for the application. Open your terminal and navigate to the project directory. 
    -    ```
        cd <your_project_directory>
        ```
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

Please note that you need to have the required dependencies installed and properly configured before running the application.




## 👥 Authors

- [rio51](https://github.com/rio51) - Primary Author

## 🙏 Acknowledgments

- Thanks to [@someone](https://github.com/someone) for the idea and inspiration to create this project.


## Project Status

✅ This project has been successfully completed and is ready for use. All the desired features have been implemented, and the script is fully functional. You can now monitor IPTV channels, track their activity and statistics, and perform various operations such as playing channels, updating video frames, retrieving channel statistics, and clearing channel buffers. Feel free to use and customize this script according to your specific requirements.

🐛 If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

🎉 Happy monitoring! 📺🔍📊

