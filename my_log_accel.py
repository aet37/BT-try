from Accelerometer import *

# Set the address
address = 'C5:02:6A:76:E4:5D'

# Create the Accerlerometer device
accelDevice = Accelerometer(address)

# Connect the Device
isConnected = accelDevice.connect()
if isConnected:
	print("Connected to " + accelDevice.device.address)

# Start logging and recording
isRecording = accelDevice.log()
if isRecording:
	print("Recording...")

# Collect for 2 seconds
sleep(2)

# Stop the recording and save the file
print('Downloading data...')
isDownloaded = accelDevice.stop_log()
if isDownloaded:
	print('  Done.')

# Reset the Device
print('Reseting...')
isReset = accelDevice.reset()
if isReset:
	print('  Done.')