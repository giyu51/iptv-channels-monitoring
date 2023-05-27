import vlc
from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio
import csv

# Create a local dictionary of channels from the csv file.
channels_dict = {}
with open("all_channels.csv", "r") as file:
    reader = csv.reader(file)
    for eachLine in reader:
        if len(eachLine) == 0:  # if the line is empty, ignore that line.
            continue
        ch_name = eachLine[0]
        ch_link = eachLine[1]
        channels_dict.update({ch_name: ch_link})

# Define a class which will be used for each new channel.
class AddChannel:
    channels_list = [] # All channels list

    def __init__(self, name):
        AddChannel.channels_list.append(self)

        self.name = name
        self.link = channels_dict.get(self.name)
        
        print("New channel: {0}".format(self.name))



        # As channels are tested in web, the flags such as "--no-audio" and "--vout dummy" are used,
        # If you want to initiate real vlc application, remove these flags.
        vlc_instance = vlc.Instance("--no-audio --vout dummy")
        self.player = vlc_instance.media_player_new()

        if self.link.startswith("http") or self.link.startswith("https"):
            self.player.set_mrl(self.link)
        elif self.link.startswith("udp://"):
            self.player.set_mrl(self.link, "udp://")
            
            
    # Start a media player for each channel individually.
    def play(self):
        print("playerPlay")
        self.player.play()

    # Update video frames,
    def update_video(self):
        print('updateVideo')
        # Get the snapshot of the current frame
        self.player.video_take_snapshot(
            0, '{0}.jpg'.format(self.name), 1280, 720)
        
        # Return the taken snapshot to the server
        return FileResponse("{0}.jpg".format(self.name))


    # Get statistics about media.

    def get_stats(self):
        print('getStats')
        s = vlc.MediaStats()
        m = self.player.get_media()
        m.get_stats(s)

        data = {
            'decoded_audio': s.decoded_audio,
            'decoded_video': s.decoded_video,
            'demux_bitrate': int(s.demux_bitrate * 8000),
            'demux_corrupted': s.demux_corrupted,
            'demux_discontinuity': s.demux_discontinuity,
            'demux_read_bytes': s.demux_read_bytes,
            'displayed_pictures': s.displayed_pictures,
            'input_bitrate': int(s.input_bitrate * 8000),
            'lost_abuffers': s.lost_abuffers,
            'lost_pictures': s.lost_pictures,
            'played_abuffers': s.played_abuffers,
            'read_bytes': s.read_bytes,
            'send_bitrate': s.send_bitrate,
            'sent_bytes': s.sent_bytes,
            'sent_packets': s.sent_packets,
            'time': int((self.player.get_time()/(1000*60)) % 60)
        }
        return data




app = FastAPI()

# Automatically go through the channels dictionary and add AddChannel object corresponding to the channels.
for ch_name, ch_link in channels_dict.items():
    print(ch_name, ch_link)
    AddChannel(name=ch_name)


channels_list = AddChannel.channels_list

print('-------------All Channels--------------')
print(channels_list)
print('---------------------------------------')




# Roughly said, it is Remote Control of a whole flow of fastAPI
# In each section the channel list is checked on whether it is a list of AddChannel objects (it should be like this) or is a single AddChannel object (probably is useful for testing each channel)
@app.on_event("startup")
def play():
    if type(channels_list) == AddChannel:   # It is a single channel
        channels_list.play()
    elif type(channels_list) == list:       # There are few channels
        for each_channel in channels_list:
            each_channel.play()


@app.on_event('startup')
async def startup_event():
    asyncio.create_task(clear_buffer())


@app.get("/")
def update_video():
    if type(channels_list) == AddChannel:
        return channels_list.update_video()
    elif type(channels_list) == list:
        return [channel.update_video() for channel in channels_list]


@app.get("/stats")
def get_stats():
    if type(channels_list) == AddChannel:
        return channels_list.get_stats()
    elif type(channels_list) == list:
        return [[channel.name, channel.get_stats()] for channel in channels_list]


# It is a function to get stats of specific channel like ...../stats/TNT or ....../stats/DisneyTr
@app.get("/stats/{channel_name}")
def get_specific_stats(channel_name: str):
    if type(channels_list) == AddChannel:
        if channel_name == channels_list.name:
            return channels_list.name, channels_list.get_stats()
        else:
            return {"ERROR": "the channel is not in the list of available channels, please update the list of channels"}

    elif type(channels_list) == list:
        # We iterate through the channels_list, which holds each channel object. 
        # If we find a channel object whose name matches the channel_name we are searching for, 
        # we assign that channel object to the outputOBJ variable. 
        # Finally, we display the name and statistics of the channel.
        outputOBJ = None
        for channelOBJ in channels_list:
            if channelOBJ.name == channel_name:
                outputOBJ = channelOBJ

        if outputOBJ == None:
            return {"ERROR": "the channel is not in the list of available channels, please update the list of channels"}
        return outputOBJ.name, outputOBJ.get_stats()


@app.get('/screen/{channel_name}')
def get_channel_screen(channel_name: str):
    if type(channels_list) == AddChannel:
        return channels_list.update_video()
    elif type(channels_list) == list:
        outputOBJ = None
        for channelOBJ in channels_list:
            if channelOBJ.name == channel_name:
                outputOBJ = channelOBJ
        if outputOBJ == None:
            return {"ERROR": "the channel is not in the list of available channels, please update the list of channels"}
        return outputOBJ.update_video()


async def clear_buffer():
    while True:
        # To clear the buffer, we periodically reload the player for each open channel if the buffer size exceeds a certain value. 
        # This script runs continuously in a loop every 5 seconds.
        
        print("_____Clearing the buffer______")
        if type(channels_list) == AddChannel:
            stats = channels_list.get_stats()
            buffer = stats["read_bytes"]
            if buffer > 1000:
                # By stopping and starting the player again, we effectively reset the buffer size to 0. 
                # This ensures that the buffer is cleared and ready to receive new data.        
                channels_list.player.stop()
                channels_list.player.play()
            print("Buffer size: ", str(buffer))

        elif type(channels_list) == list:

            for channelOBJ in channels_list:
                print("-------"+str(channelOBJ),channelOBJ.name+"-------")
                channel_stats = channelOBJ.get_stats()
                channel_buffer = channel_stats["read_bytes"]
                if channel_buffer > 100:
                    channelOBJ.player.stop()
                    channelOBJ.player.play()
                    print('Buffer of {0} has been cleared'.format(
                        str(channelOBJ.name)))
        await asyncio.sleep(5)  # Run each 5 seconds
