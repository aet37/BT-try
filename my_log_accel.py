from mbientlab.metawear import MetaWear, libmetawear, parse_value, create_voidp, create_voidp_int
from mbientlab.metawear.cbindings import *
from threading import Event

address = 'C5:02:6A:76:E4:5D'
print("Searching for device...")
d = MetaWear(address)
d.connect()
print("Connected to " + d.address)

print("Configuring device")


class Accelerometer:

	# Setup function
	def __init__(self, address, fs=100):
		self.address = address
		self.fs = fs
		self.debug = debug
		self.device = MetaWear(address)
		self.signal = []
		self.logger = []
		self.data = []

	# Function to connect
	def connect(self):
		self.device.connect()
		return True

	# Start logging the acceleration
	def log(self):
		try:
			# Configure the board with the right frequency and g
			libmetawear.mbl_mw_acc_set_odr(self.device.board, self.fs)	# Start the accelerometer
			libmetawear.mbl_mw_acc_set_range(self.device.board, 16)	# Set range to +/-16g or closest valid range
			libmetawear.mbl_mw_acc_write_acceleration_config(self.device.board)

			# Start the logger
			self.signal = libmetawear.mbl_mw_acc_get_acceleration_data_signal(self.device.board)
			self.logger = create_voidp(lambda fn: libmetawear.mbl_mw_datasignal_log(self.signal, None, fn), resource = "acc_logger")
			libmetawear.mbl_mw_logging_start(self.device.board, 0)

			# Start the sampling
			libmetawear.mbl_mw_acc_enable_acceleration_sampling(self.device.board)
			libmetawear.mbl_mw_acc_start(self.device.board)

			return True # If run sucessful

		except:
		RuntimeError as err:
			print(err)
			return False

    # Stop logging and save to file
    def stop_log(self, fpath):
    	try:
			print("Setop acc")
			libmetawear.mbl_mw_acc_stop(d.board)
			libmetawear.mbl_mw_acc_disable_acceleration_sampling(d.board)

			print("Stop logging")
			libmetawear.mbl_mw_logging_stop(d.board)

			print("Flush cache if MMS")
			libmetawear.mbl_mw_logging_flush_page(d.board)

			print("Downloading data")
			libmetawear.mbl_mw_settings_set_connection_parameters(d.board, 7.5, 7.5, 0, 6000)
			sleep(1.0)

			print("Setup Download handler")
			e = Event()
			def progress_update_handler(context, entries_left, total_entries):
			if (entries_left == 0):
				e.set()

			fn_wrapper = FnVoid_VoidP_UInt_UInt(progress_update_handler)
			download_handler = LogDownloadHandler(context = None, received_progress_update = fn_wrapper, received_unknown_entry = cast(None, FnVoid_VoidP_UByte_Long_UByteP_UByte), received_unhandled_entry = cast(None, FnVoid_VoidP_DataP))

			callback = FnVoid_VoidP_DataP(lambda ctx, p: print("{epoch: %d, value: %s}" % (p.contents.epoch, parse_value(p))))

			print("Subscribe to logger")
			libmetawear.mbl_mw_logger_subscribe(logger, None, callback)

			print("Download data")
			libmetawear.mbl_mw_logging_download(d.board, 0, byref(download_handler))
			e.wait()

			return True # Signal sucess

		except:
			RuntimeError as err:
				print(err)
				return False





