from Accelerometer import *

# Set the address
address = 'C5:02:6A:76:E4:5D'
fpath = '/home/hifu/test.csv'
#fpath = 'C:\\Users\\rasla\\Desktop\\test.csv'

# Create the Accerlerometer device
accelDevice = Accelerometer(address, fpath)

# Connect the Device
isConnected = False
while not isConnected:
	isConnected = accelDevice.connect()
	sleep(1.5)


print("Connected to " + accelDevice.device.address)

#print('Device battery: ')
#print(accelDevice.get_battery())

# Start logging and recording
isRecording = accelDevice.log()
if isRecording:
	print("Recording...")

# Collect for 2 seconds
sleep(20)

# Stop the recording and save the file
print('Downloading data...')
isDownloaded = accelDevice.stop_log()

# Reset the Device
print('Reseting...')
isReset = accelDevice.reset()
if isReset:
	print('  Done.')