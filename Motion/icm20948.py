# icm20948.cpp
# covert to python

#include <stdint.h>
#include <string.h>
#include "math.h"
#include "DriverFramework.hpp"
#include "icm20948.hpp"
#include "icm20948_mag.hpp"

import stdint
import string
import math.h
import DriverFramework.hpp
import icm20948.hpp
import icm20948_mag.hpp

#TOdd Debug
#include <sys/time.h>
import time

icm20948_DEBUG = 1
icm20948_DEBUG = 1

icm20948_ONE_G = 9.80665 # float?
Sicm20948_ONE_G = 9.80665 # float?

#define MIN(_x, _y) (_x) > (_y) ? (_y) : (_x)
# MIN(_x, _y) (_x) > (_y) ? (_y) : (_x):

# Uncomment to allow additional debug output to be generated.
icm20948_DEBUG = 1

icm20948_DEBUG = 1
# using namespace DriverFramework;

icm20948::icm20948_init()

#{
# Use 1 MHz for normal registers.
	#ifndef __IMU_USE_I2C
# _setBusFrequency(SPI_FREQUENCY_1MHZ);
#endif	
# Zero the struct

# fix above and below
# _writeReg(ICMREG_REG_BANK_SEL,0x00)
# all floats
m_sensor_data.accel_m_s2_x = 0.0
m_sensor_data.accel_m_s2_y = 0.0
m_sensor_data.accel_m_s2_z = 0.0
m_sensor_data.gyro_rad_s_x = 0.0
m_sensor_data.gyro_rad_s_y = 0.0
m_sensor_data.gyro_rad_s_z = 0.0
m_sensor_data.mag_ga_x = 0.0
m_sensor_data.mag_ga_y = 0.0
m_sensor_data.mag_ga_z = 0.0
m_sensor_data.temp_c = 0.0

m_sensor_data.read_counter = 0
m_sensor_data.error_counter = 0
m_sensor_data.fifo_overflow_counter = 0
m_sensor_data.fifo_corruption_counter = 0
m_sensor_data.gyro_range_hit_counter = 0
m_sensor_data.accel_range_hit_counter = 0

m_sensor_data.fifo_sample_interval_us = 0
m_sensor_data.is_last_fifo_sample = false

##########################################
##########################################
#### Ints as strings
m_sensor_data.accel_m_s2_x = "0.0"
m_sensor_data.accel_m_s2_y = "0.0"
m_sensor_data.accel_m_s2_z = "0.0"
m_sensor_data.gyro_rad_s_x = "0.0"
m_sensor_data.gyro_rad_s_y = "0.0"
m_sensor_data.gyro_rad_s_z = "0.0"
m_sensor_data.mag_ga_x = "0.0"
m_sensor_data.mag_ga_y = "0.0"
m_sensor_data.mag_ga_z = "0.0"
m_sensor_data.temp_c = "0.0"

m_sensor_data.read_counter = "0"
m_sensor_data.error_counter = "0"
m_sensor_data.fifo_overflow_counter = "0"
m_sensor_data.fifo_corruption_counter = "0"
m_sensor_data.gyro_range_hit_counter = "0"
m_sensor_data.accel_range_hit_counter = "0"

m_sensor_data.fifo_sample_interval_us = "0"
m_sensor_data.is_last_fifo_sample = false

##########################################
##########################################

result = _writeReg(ICMREG_PWR_MGMT_1, BIT_H_RESET)

if result != 0
print "reset failed":       #DF_LOG_ERR = "reset failed"

#  if result (result != 0)
#  st DF_LOG_ERR("reset failed")

time.sleep(100) # c++ to python sleep is 1 to 1000.....usleep(100000)

	DF_LOG_INFO("Reset icm20948")
	result = _writeReg(ICMREG_PWR_MGMT_1, 0x01):

if (result != 0)
	DF_LOG_ERR("wakeup sensor failed"):

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000)

result = _writeReg(ICMREG_PWR_MGMT_2, 0);
    return _writeReg(ICMREG_PWR_MGMT_2, 0)

	if (result != 0) {
		DF_LOG_ERR("enable failed");
	}

time.sleep(10) # c++ to python sleep is 1 to 1000........usleep(10000)

	# Reset I2C master and device.
	result = _writeReg(ICMREG_USER_CTRL,
			   BITS_USER_CTRL_I2C_MST_RST);


	if (result != 0) {
		DF_LOG_ERR("user ctrl 1 failed");
	}

time.sleep(1) # c++ to python sleep is 1 to 1000......usleep(1000)

# Reset and enable FIFO
	result = _writeReg(ICMREG_FIFO_RST,BITS_USER_CTRL_FIFO_RST)

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000)

	result = _writeReg(ICMREG_FIFO_RST,0);

	result = _writeReg(ICMREG_USER_CTRL,BITS_USER_CTRL_FIFO_EN
# BITS_USER_CTRL_DMP_EN
# BITS_USER_CTRL_I2C_MST_EN
# BITS_USER_CTRL_I2C_IF_DIS
 );

#	unsigned char ctrlreg;
	result = _readReg(ICMREG_USER_CTRL, ctrlreg);
	printf("user ctrl test = %x\r\n",ctrlreg);


	if (result != 0) {
		DF_LOG_ERR("Fifo reset failed");
	}

time.sleep(1)  # c++ to python sleep is 1 to 1000.......usleep(1000);

	if (_mag_enabled) {
		result = _writeReg(ICMREG_FIFO_EN2,
				   BITS_FIFO_ENABLE_TEMP_OUT | BITS_FIFO_ENABLE_GYRO_XOUT
				   | BITS_FIFO_ENABLE_GYRO_YOUT
				   | BITS_FIFO_ENABLE_GYRO_ZOUT | BITS_FIFO_ENABLE_ACCEL);
		result = _writeReg(ICMREG_FIFO_EN1, BITS_FIFO_ENABLE_SLV0); # SLV0 is configured for bulk transfer of mag data over I2C

	} else {
		result = _writeReg(ICMREG_FIFO_EN2,
				   BITS_FIFO_ENABLE_TEMP_OUT | BITS_FIFO_ENABLE_GYRO_XOUT
				   | BITS_FIFO_ENABLE_GYRO_YOUT
				   | BITS_FIFO_ENABLE_GYRO_ZOUT | BITS_FIFO_ENABLE_ACCEL);
		DF_LOG_INFO("initializing icm20948 driver without mag support");
	}

	if (result != 0) {
		DF_LOG_ERR("FIFO enable failed");
	}

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000)

result = _writeReg(ICMREG_GYRO_CONFIG_1,BITS_DLPF_CFG_51HZ);
result = _writeReg(ICMREG_REG_BANK_SEL,0x20);

result = _writeReg(ICMREG_GYRO_DIV,0x04);
result = _writeReg(ICMREG_GYRO_DIV,0x03);
result = _writeReg(ICMREG_GYRO_CONFIG_1,BITS_DLPF_CFG_51HZ | BITS_DLPF_FCHOICE);
	if (result != 0) {
		DF_LOG_ERR("config failed");
	}

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000)

#result = _writeReg(0x01,0x07); # Gyro Config
#result = _writeReg(ICMREG_FSYNC_CONFIG, BITS_FS_2000DPS);

	if (result != 0) {
		DF_LOG_ERR("Gyro scale config failed");
	}

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000)

	result = _writeReg(ICMREG_ACCEL_CONFIG, BITS_ACCEL_CONFIG_16G | BITS_DLPF_CFG_51HZ);


	result = _writeReg(MPUREG_ACCEL_CONFIG, BITS_ACCEL_CONFIG_16G);
	result = _writeReg(ICMREG_ACCEL_CONFIG, BITS_ACCEL_CONFIG_16G | BITS_DLPF_CFG_6HZ);
	result = _writeReg(ICMREG_ACCEL_CONFIG, BITS_ACCEL_CONFIG_16G | BITS_DLPF_CFG_6HZ);
	result = _writeReg(ICMREG_ACCEL_DIVL,0x04);
	result = _writeReg(ICMREG_ACCEL_CONFIG, BITS_ACCEL_CONFIG_16G | BITS_DLPF_CFG_361HZ | 0x01);


if (result != 0) {
	DF_LOG_ERR("Accel scale config failed");
	}

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000);

#result = _writeReg(ICMREG_ACCEL_CONFIG2, BITS_ACCEL_CONFIG2_BW_41HZ);
#result = _writeReg(ICMREG_ACCEL_CONFIG2, 0x00);

if (result != 0) {
	DF_LOG_ERR("Accel scale config2 failed");
	}

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000);

#result = _writeReg(ICMREG_REG_BANK_SEL,0x00);
# Initialize the magnetometer inside the IMU, if enabled by the caller.
if (_mag_enabled && _mag == nullptr) {
	if ((_mag = new icm20948_mag(*this, icm20948_MAG_SAMPLE_RATE_100HZ))
		!= nullptr) {
# Initialize the magnetometer, providing the output data rate for
# data read from the IMU FIFO.  This is used to calculate the I2C
# delay for reading the magnetometer.
			result = _mag->initialize(icm20948_MEASURE_INTERVAL_US);

			if (result != 0) {
				DF_LOG_ERR("Magnetometer initialization failed");
			}

		} else {
			DF_LOG_ERR("Allocation of magnetometer object failed.");
		}
	}

# Enable/clear the FIFO of any residual data
	reset_fifo();

# Clear Interrupt Status
	clear_int_status();

	return 0;
}

int icm20948::icm20948_deinit()
{
# Leave the IMU in a reset state (turned off).
	int result = _writeReg(ICMREG_PWR_MGMT_1, BIT_H_RESET);

	if (result != 0) {
		DF_LOG_ERR("reset failed");
	}

# Deallocate the resources for the mag driver, if enabled.
	if (_mag_enabled && _mag != nullptr) {
		delete _mag;
		_mag = nullptr;
	}

	return 0;
}

int icm20948::start()
{
	printf("DevObj Todd Says Hi\n");

# Open the device path specified in the class initialization
# attempt to open device in start()
	
	#ifdef __IMU_USE_I2C
		
		 int result = I2CDevObj::start();
		 result = _setSlaveConfig(0x68,400,9000);
	#else
		int result = SPIDevObj::start();
	#endif

	if (result != 0) {
		DF_LOG_ERR("DevObj start failed");
		DF_LOG_ERR("Unable to open the device path: %s", m_dev_path);
		return result;
	}
	else
		printf("TODD: start OK\n");		

# Set the bus frequency for register get/set
	#ifndef __IMU_USE_I2C
		result = _setBusFrequency(SPI_FREQUENCY_1MHZ);
	if (result != 0) {
		DF_LOG_ERR("failed setting SPI bus frequency: %d", result);
	}
	#endif

#Try to talk to the sensor

	uint8_t sensor_id;
	result = _readReg(ICMREG_WHOAMI, sensor_id);

	if (result != 0) {
		DF_LOG_ERR("Unable to communicate with the icm20948 sensor");
		goto exit1;
	}

	if (MPU_WHOAMI_ICM20948 != sensor_id) {
		DF_LOG_ERR("icm20948 sensor WHOAMI wrong: 0x%X, should be: 0x%X",
			   sensor_id, MPU_WHOAMI_ICM20948);
		result = -1;
		goto exit1;
	}

	result = icm20948_init();

	if (result != 0) {
		DF_LOG_ERR("error: IMU sensor initialization failed, sensor read thread not started");
		goto exit1;
	}

	result = DevObj::start();

	if (result != 0) {
		DF_LOG_ERR("DevObj start failed");
		return result;
	}

exit1:
	return result;
}

int icm20948::stop()
{
	int result = icm20948_deinit();

	if (result != 0) {
		DF_LOG_ERR(
			"error: IMU sensor de-initialization failed.");
		return result;
	}

	result = DevObj::stop();

	if (result != 0) {
		DF_LOG_ERR("DevObj stop failed");
		return result;
	}

# We need to wait so that all measure calls are finished before
# closing the device.

time.sleep(10) # c++ to python sleep is 1 to 1000.......usleep(10000);

	return 0;
}

int icm20948::get_fifo_count()
{
	int num_bytes = 0x0;

	#ifndef __IMU_USE_I2C
	_setBusFrequency(SPI_FREQUENCY_1MHZ);
	
	#endif
	int ret = _bulkRead(ICMREG_FIFO_COUNTH, (uint8_t *) &num_bytes,
			    sizeof(num_bytes));
	
	if (ret == 0) {

		#TODO: add ifdef for endianness
		num_bytes = swap16(num_bytes);

		return num_bytes;

	} else {
		DF_LOG_ERR("FIFO count read failed");
		return ret;
	}
}

void icm20948::reset_fifo()
{
	#ifndef __IMU_USE_I2C
	# Use 1 MHz for normal registers.
	_setBusFrequency(SPI_FREQUENCY_1MHZ);
	#endif
	int result;

	result  = _writeReg(ICMREG_FIFO_RST,BITS_USER_CTRL_FIFO_RST);

time.sleep(1) # c++ to python sleep is 1 to 1000.......usleep(1000);

	result  = _writeReg(ICMREG_FIFO_RST,0x00);
#	result = _modifyReg(MPUREG_USER_CTRL,
#			    0,
#			    BITS_USER_CTRL_FIFO_RST |
#			    BITS_USER_CTRL_FIFO_EN);

	if (result != 0) {
		DF_LOG_ERR("FIFO reset failed");
	}
}

void icm20948::clear_int_status()
{
	int result;
	uint8_t int_status = 0;

	result = _readReg(ICMREG_INT_STATUS, int_status);

	if (result != 0) {
		DF_LOG_ERR("Interrupt status clear failed");
	}
}

void icm20948::_measure()
{
	#static struct timeval tvalBefore, tvalAfter;

	#ifndef __IMU_USE_I2C
	# Use 1 MHz for normal registers.
	_setBusFrequency(SPI_FREQUENCY_1MHZ);
	#endif
	uint8_t int_status = 0;

	_readReg(ICMREG_INT_STATUS1, int_status);
	if(!int_status)
		return;

	int result = _readReg(ICMREG_INT_STATUS, int_status);

	if (result != 0) {
		++m_sensor_data.error_counter;
		printf("%s:%d error count - %d\n",__FUNCTION__,__LINE__,m_sensor_data.error_counter);
		
		return;
	}

	# result = _readReg(ICMREG_INT_STATUS2, int_status);
	# if (int_status & BITS_INT_STATUS_FIFO_OVERFLOW) {
	# 	reset_fifo();

	# 	m_sensor_data.fifo_overflow_counter;
	# 	DF_LOG_ERR("FIFO overflow");
	# 	printf("INT_STATUS_2 = %x\n",int_status);

	# 	return;
	# }

	int size_of_fifo_packet;

	if (_mag_enabled) {
		size_of_fifo_packet = sizeof(fifo_packet_with_mag);

	} else {
		size_of_fifo_packet = sizeof(fifo_packet);
	}

# Get FIFO byte count to read and floor it to the report size.

	#int fifo_count_int = get_fifo_count() & 0x1FF;
	#printf("Fifo count = %d, sizeof packet = %d\r\n",fifo_count_int,size_of_fifo_packet);
	#int bytes_to_read = (fifo_count_int) / size_of_fifo_packet
	#		    * size_of_fifo_packet;

	int16_t bytes_to_read = get_fifo_count() / size_of_fifo_packet
			    * size_of_fifo_packet;

	# unsigned char mag_z_l,index;
	# printf("mag reg = ");
	# for(index = ICMREG_EXT_SLV_SNS_D01;index <= ICMREG_EXT_SLV_SNS_D06;index++ )
	# {
	# 	_readReg(index, mag_z_l);
	# 	printf("%02X ",mag_z_l);
	# }
	# printf("\r\n");


	printf("user ctrl test = %x\r\n",sensor_id);
	printf("BTR = %d\n",bytes_to_read);
	if(bytes_to_read <= 0)
		return;

	#  It looks like the FIFO doesn't actually deliver at 8kHz like it is supposed to.
	#  Therefore, we need to adapt the interval which we pass on to the integrator.
	#  The filtering is to lower the jitter that could result through the calculation
	#  because of the fact that the bytes we fetch per _measure() cycle varies.

	_packets_per_cycle_filtered = (0.95f * _packets_per_cycle_filtered) + (0.05f * (bytes_to_read / size_of_fifo_packet));

	if (bytes_to_read < 0) {
		++m_sensor_data.error_counter;
		printf("%s:%d error count - %d\n",__FUNCTION__,__LINE__,m_sensor_data.error_counter);
		return;
	}

	# Allocate a buffer large enough for n complete packets, read from the
	# sensor FIFO.
	const unsigned buf_len = (ICM_MAX_LEN_FIFO_IN_BYTES / size_of_fifo_packet) * size_of_fifo_packet;
	uint8_t fifo_read_buf[buf_len];

	if (bytes_to_read <= 0) {
		++m_sensor_data.error_counter;
		printf("%s:%d error count - %d\n",__FUNCTION__,__LINE__,m_sensor_data.error_counter);
		return;
	}

	#const unsigned read_len = MIN((unsigned)bytes_to_read, buf_len);
	unsigned int read_len = 23;
	memset(fifo_read_buf, 0x0, buf_len);


	#  According to the protocol specs, all sensor and interrupt registers may be read at 20 MHz.
	#  It is unclear what rate the FIFO register can be read at.
	#  If the FIFO buffer was read at 20 MHz, two effects were seen:
	#  The buffer is off-by-one. So the report "starts" at &fifo_read_buf[i+1].
	#  Also, the FIFO buffer seemed to prone to random corruption (or shifting), unless
	#  all other sensors ran very smooth. (E.g. Changing the bus speed of the HMC5883 driver from
	#  400 kHz to 100 kHz could cause corruption because this driver wouldn't run as regularly.
	
	#  Luckily 10 MHz seems to work fine.


#ifndef __IMU_USE_I2C
#if defined(__DF_EDISON)
	#FIFO corrupt at 10MHz.
	_setBusFrequency(SPI_FREQUENCY_5MHZ);
#elif defined(__DF_RPI_SINGLE)
	_setBusFrequency(SPI_FREQUENCY_5MHZ);
#else
	_setBusFrequency(SPI_FREQUENCY_10MHZ);
#endif
#endif
	#result = _bulkRead(ICMREG_FIFO_R_WR, fifo_read_buf, read_len);

	result = _bulkRead(ICMREG_ACCEL_XOUT_H, fifo_read_buf, read_len);
	
# gettimeofday (&tvalAfter, NULL);
# 	printf("%d bytes %ld uSec\n",read_len,((tvalAfter.tv_sec - tvalBefore.tv_sec)*1000000L
#            +tvalAfter.tv_usec) - tvalBefore.tv_usec
#           );
# 	tvalBefore.tv_sec = tvalAfter.tv_sec;
# 	tvalBefore.tv_usec = tvalAfter.tv_usec;

if result != 0
	m_sensor_data.error_counter;
	printf("%s:%d error count - %d\n",__FUNCTION__,__LINE__,m_sensor_data.error_counter);
	return:


#	for (unsigned packet_index = 0; packet_index < read_len / size_of_fifo_packet; ++packet_index)

#		fifo_packet *report = (fifo_packet *)(&fifo_read_buf[packet_index	* size_of_fifo_packet]);
#Print RAW FIFO contents
		# int i;
		# unsigned char *ptr;
		# ptr = (unsigned char *)report;
		# for(i=0;i<size_of_fifo_packet;i++)
		# 	printf("%02x ",*ptr++);
		# printf("\r\n");

		#TODO: add ifdef for endianness
		report->accel_x = swap16(report->accel_x)
		report->accel_y = swap16(report->accel_y)
		report->accel_z = swap16(report->accel_z)
		report->temp = swap16(report->temp)
		report->gyro_x = swap16(report->gyro_x)
		report->gyro_y = swap16(report->gyro_y)
		report->gyro_z = swap16(report->gyro_z)
		# printf("acc %d,%d,%d gyro %d,%d,%d temp %d\n",report->accel_x,report->accel_y,report->accel_z,
		# 												report->gyro_x,report->gyro_y,report->gyro_z,
		# 												report->temp);

		# int temp;
		# temp = report->accel_x;
		# report->accel_x = -report->accel_y;
		# report->accel_y = temp;
		# report->accel_z = -report->accel_z;

		# temp = report->gyro_x;
		# report->gyro_x = -report->gyro_y;
		# report->gyro_y = temp;
		# report->gyro_z = -report->gyro_z;

		# Check if the full accel range of the accel has been used. If this occurs, it is
		# either a spike due to a crash/landing or a sign that the vibrations levels
		# measured are excessive.
		if  report->accel_x == INT16_MIN || report->accel_x == INT16_MAX ||
		    report->accel_y == INT16_MIN || report->accel_y == INT16_MAX ||
		    report->accel_z == INT16_MIN || report->accel_z == INT16_MAX
			print m_sensor_data.accel_range_hit_counter:


		# Also check the full gyro range, however, this is very unlikely to happen.
		if  report->gyro_x == INT16_MIN || report->gyro_x == INT16_MAX ||
		    report->gyro_y == INT16_MIN || report->gyro_y == INT16_MAX ||
		    report->gyro_z == INT16_MIN || report->gyro_z == INT16_MAX
			print m_sensor_data.gyro_range_hit_counter:

		const float temp_c = float(report->temp) / 361.0f + 35.0f;
		const float temp_c = float(report->temp) / 333.87f + 21.0f;

		# Use the temperature field to try to detect if we (ever) fall out of sync with
		# the FIFO buffer. If the temperature changes insane amounts, reset the FIFO logic
		# and return early.
		if (!_temp_initialized) {
			# Assume that the temperature should be in a sane range of -40 to 85 deg C which is
			# the specified temperature range, at least to initialize.
			if (temp_c > -40.0f && temp_c < 85.0f) {

				# Initialize the temperature logic.
				_last_temp_c = temp_c;
				DF_LOG_INFO("IMU temperature initialized to: %f", (double) temp_c);
				_temp_initialized = true;
			}

		} else {
			# Once initialized, check for a temperature change of more than 2 degrees which
			# points to a FIFO corruption.
			if (fabsf(temp_c - _last_temp_c) > 2.5f) {
				DF_LOG_ERR(
					"FIFO corrupt, temp difference: %f, last temp: %f, current temp: %f",
					(double)fabsf(temp_c - _last_temp_c), (double)_last_temp_c, (double)temp_c);
				reset_fifo();
				_temp_initialized = false;
				++m_sensor_data.fifo_corruption_counter;
				return;
			}

			_last_temp_c = temp_c;
		}

		m_sensor_data.accel_m_s2_x = float(report->accel_x)
					     * (icm20948_ONE_G / 2048.0f);
		m_sensor_data.accel_m_s2_y = float(report->accel_y)
					     * (icm20948_ONE_G / 2048.0f);
		m_sensor_data.accel_m_s2_z = float(report->accel_z)
					     * (icm20948_ONE_G / 2048.0f);
		m_sensor_data.temp_c = temp_c;
		m_sensor_data.gyro_rad_s_x = float(report->gyro_x) * GYRO_RAW_TO_RAD_S;
		m_sensor_data.gyro_rad_s_y = float(report->gyro_y) * GYRO_RAW_TO_RAD_S;
		m_sensor_data.gyro_rad_s_z = float(report->gyro_z) * GYRO_RAW_TO_RAD_S;

		if (_mag_enabled) {
			struct fifo_packet_with_mag *report_with_mag_data = (struct fifo_packet_with_mag *)report;
			int mag_error = _mag->process((const struct mag_data &)report_with_mag_data->mag_st1,
						      m_sensor_data.mag_ga_x,
						      m_sensor_data.mag_ga_y,
						      m_sensor_data.mag_ga_z);

			if (mag_error == MAG_ERROR_DATA_OVERFLOW) {
				m_sensor_data.mag_fifo_overflow_counter++;
			}
		}

		# Pass on the sampling interval between FIFO samples at 8kHz.
		m_sensor_data.fifo_sample_interval_us = 1000000 / icm20948_MEASURE_INTERVAL_US
							/ _packets_per_cycle_filtered;

		# Flag if this is the last sample, and _publish() should wrap up the data it has received.
		m_sensor_data.is_last_fifo_sample = ((packet_index + 1) == (read_len / size_of_fifo_packet));

		++m_sensor_data.read_counter;

		# Generate debug output every second, assuming that a sample is generated every
		# 125 usecs
#ifdef icm20948_DEBUG

		if (++m_sensor_data.read_counter % (1000000 / m_sensor_data.fifo_sample_interval_us) == 0) {

			DF_LOG_INFO("IMU: accel: [%f, %f, %f]",
				    (double)m_sensor_data.accel_m_s2_x,
				    (double)m_sensor_data.accel_m_s2_y,
				    (double)m_sensor_data.accel_m_s2_z);
			DF_LOG_INFO("     gyro:  [%f, %f, %f]",
				    (double)m_sensor_data.gyro_rad_s_x,
				    (double)m_sensor_data.gyro_rad_s_y,
				    (double)m_sensor_data.gyro_rad_s_z);
			DF_LOG_INFO("    temp:  %f C", (double)m_sensor_data.temp_c);
			DF_LOG_INFO("     mag:  [%f, %f, %f] ga",
					    (double)m_sensor_data.mag_ga_x, (double)m_sensor_data.mag_ga_y, (double)m_sensor_data.mag_ga_z);

		}

#endif

		#uint8_t ext1,ext2;

		#result = _writeReg(ICMREG_REG_BANK_SEL,0x20);
		#result = _readReg(0x01, ext1);
		#DF_LOG_INFO("Gyro COnfig = [%x]",ext1);
		#result = _writeReg(ICMREG_REG_BANK_SEL,0x00);

		# result = _readReg(0x3D, ext1);
		# result = _readReg(0x3E, ext2);
		# DF_LOG_INFO("EXT_SLV_23 = [%x, %x]",ext1,ext2);
		# #uint8_t *ptr;

		# _mag->read_reg(0x01,&ext1);
		# DF_LOG_INFO("MAG_READ_0x01 = [%x]",ext1);
		# _mag->read_reg(0x11,&ext1);
		# DF_LOG_INFO("MAG_READ_0x11 = [%x]",ext1);
		# _mag->read_reg(0x31,&ext1);
		# DF_LOG_INFO("MAG_READ_0x31 = [%x]",ext1);
		# _mag->read_reg(0x32,&ext1);
		# DF_LOG_INFO("MAG_READ_0x32 = [%x]",ext1);
		# _mag->read_reg(0x33,&ext1);
		# DF_LOG_INFO("MAG_READ_0x33 = [%x]",ext1);
		# _mag->read_reg(0x34,&ext1);
		# DF_LOG_INFO("MAG_READ_0x34 = [%x]",ext1);

		# _mag->read_reg(0x11,&ext1);
		# _mag->read_reg(0x12,&ext2);

		#_mag->read_reg(0x18,&ext1);
		#DF_LOG_INFO("MAG_READ_0x18 = [%x]",ext1);
		
		#DF_LOG_INFO("MAG_READ_X = [%x, %x]",ext1,ext2);

		#DF_LOG_INFO("     mag:  [%f, %f, %f] ga",
		#			    m_sensor_data.mag_ga_x, m_sensor_data.mag_ga_y, m_sensor_data.mag_ga_z);

#ifdef notdefined  # icm20948_DEBUG

		if (_mag_enabled /*&& mag_error == 0*/) {
			if ((m_sensor_data.read_counter % 10000) == 0) {
				DF_LOG_INFO("     mag:  [%f, %f, %f] ga",
					    (double)m_sensor_data.mag_ga_x, (double)m_sensor_data.mag_ga_y, (double)m_sensor_data.mag_ga_z);
			}
		}

#endif
		_publish(m_sensor_data);

	}
}
