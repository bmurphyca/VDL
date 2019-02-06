# icm20948_mag.hpp

#pragma once

#include "icm20948.hpp"

#cnamespace DriverFramework
#{

# Forward reference:
# class icm20948;

# Magnetometer device ID
icm20948_AKM_DEV_ID	= 0x09
# icm20948_AKM_DEV_ID = "0x09"

# Magnetometer device address

icm20948_AK8963_I2C_ADDR = 0x0C
icm20948_AK8963_I2C_READ = 0x80
icm20948_AK8963_I2C_WRITE = 0x00

# icm20948_AK8963_I2C_ADDR = "0x0C"
# icm20948_AK8963_I2C_READ = "0x80"
# icm20948_AK8963_I2C_WRITE = "0x00"



# icm20948 Magnetometer Register Addresses: Defines only the register addresses
# used in icm20948 driver.

icm20948_MAG_REG_WIA = 0x01
icm20948_MAG_REG_ST1 = 0x10 # two of these
icm20948_MAG_REG_DATA = 0x11
icm20948_MAG_REG_HXL = 0x11
icm20948_MAG_REG_ST2 = 0x18
icm20948_MAG_REG_CNTL2 = 0x31
icm20948_MAG_REG_CNTL3 = 0x32
icm20948_MAG_REG_ASAX = 0x10 # two of these
icm20948_MAG_REG_ASAY = 0x11
icm20948_MAG_REG_ASAZ = 0x12

# icm20948_MAG_REG_WIA = "0x01"
# icm20948_MAG_REG_ST1 = "0x10"
# icm20948_MAG_REG_DATA = "0x11"
# icm20948_MAG_REG_HXL = "0x11"
# icm20948_MAG_REG_ST2 = "0x18"
# icm20948_MAG_REG_CNTL2 = "0x31"
# icm20948_MAG_REG_CNTL3 = "0x32"
# icm20948_MAG_REG_ASAX = "0x10"
# icm20948_MAG_REG_ASAY = "0x11"
# icm20948_MAG_REG_ASAZ = "0x12"



# Bit definitions for the magnetometer registers

BIT_MAG_CNTL1_MODE_POWER_DOWN = 0x0
BIT_MAG_CNTL1_MODE_SINGLE_MEASURE_MODE = 0x1
BIT_MAG_CNTL1_MODE_CONTINUOUS_MEASURE_MODE_1 = 0x2
BIT_MAG_CNTL1_MODE_CONTINUOUS_MEASURE_MODE_2 = 0x4
BIT_MAG_CNTL1_FUSE_ROM_ACCESS_MODE = 0xF
BIT_MAG_CNTL1_16_BITS = 0x10
BIT_MAG_HOFL =0x08

BIT_MAG_CNTL2_SOFT_RESET = 0x01

MAG_ERROR_DATA_OVERFLOW	= -3


# BIT_MAG_CNTL1_MODE_POWER_DOWN = "0x0"
# BIT_MAG_CNTL1_MODE_SINGLE_MEASURE_MODE = "0x1"
# BIT_MAG_CNTL1_MODE_CONTINUOUS_MEASURE_MODE_1 = "0x2"
# BIT_MAG_CNTL1_MODE_CONTINUOUS_MEASURE_MODE_2 = "0x4"
# BIT_MAG_CNTL1_FUSE_ROM_ACCESS_MODE = "0xF"
# BIT_MAG_CNTL1_16_BITS = "0x10"
# BIT_MAG_HOFL = "0x08"

# BIT_MAG_CNTL2_SOFT_RESET = "0x01"

# MAG_ERROR_DATA_OVERFLOW	= "-3"


# 16bit mode: 0.15uTesla/LSB, 100 uTesla == 1 Gauss
# MAG_RAW_TO_GAUSS = (float(0.15 / 100.0));		#MPU9250
# MAG_RAW_TO_GAUSS = (float(0.15 / 100.0));

MAG_RAW_TO_GAUSS = (float(0.15 / 100.0))		#MPU9250
MAG_RAW_TO_GAUSS = (float(0.15 / 100.0))



#enum mag_sample_rate_e {
#    icm20948_MAG_SAMPLE_RATE_8HZ = 0
#    icm20948_MAG_SAMPLE_RATE_100HZ = 1
#    NUM_icm20948_MAG_SAMPLE_RATES
#    };

# class icm20948_mag
# {
# public:
# 	icm20948_mag(icm20948 &imu, enum mag_sample_rate_e sample_rate) :
# 		_mag_initialized(false), _sample_rate(sample_rate), _imu(imu)
# 	{
# 	}

# 	@brief
# 	Called to initialize the magnetometer connection via the
# 	internal I2C bus of the sensor.  The gyro and accelerometer
# 	must have been previously configured.
# 	@return
# 	- 0 on success,
# 	 - -errno on failure
# 	int initialize(int output_data_rate_in_hz);

# 	 @brief
# 	 Reads the sensitivity values contained in the FUSE memory of the mag and
# 	 generates values used internally to process mag measurements.
# 	 @return
# 	 - 0 on success, -
# 	 errno on failure
# 	int get_sensitivity_adjustment(void);

# 	@brief
# 	Verifies the presence of the mag on the internal I2C bus, by querying
# 	for the known device ID.
# 	@return
# 	- 0 on success
# 	-errno on failure
# 	int detect(void);

# 	@brief
# 	Writes a value to the specified IMU register, and verifies that it was
# 	successfully written by attempting to read it back.
# 	@return
# 	- 0 on success
# 	- -errno on failure
# 	int write_imu_reg_verified(int reg, uint8_t val, uint8_t mask);

# 	@brief
# 	Reads the value of the specified magnetometer register and returns the
# 	register value in the "val" parameter.
# 	@return
# 	- 0 on success
# 	- -errno on failure
# 	int read_reg(uint8_t reg, uint8_t *val);

# 	@brief
# 	Writes the value passed in to the specified magnetometer register.
# 	@return
# 	- 0 on success
# 	- -errno on failure
# 	int write_reg(uint8_t reg, uint8_t val);

# 	@brief
# 	Process the data passed in to generate mag values in Gauss units.
# 	@param mag_ga_x: Use to return mag value in Gauss for x
# 	@param mag_ga_y: Use to return mag value in Gauss for y
# 	@param mag_ga_z: Use to return mag value in Gauss for z
# 	@return
# 	- 0 on success
# 	- -errno on failure
# 	int process(const struct mag_data &data, float &mag_ga_x, float &mag_ga_y, float &mag_ga_z);

# protected:
# 	@brief
# 	Used internally to perform a complete mag initialization.  Called
# 	multiple times by the initialize() function if the first initialization
# 	attempt fails.
# 	@param
# 	output_data_rate_in_hz
#   The rate at which the sensor produces new IMU data (accel, gyro, and temperature data)
# 	@return
# 	- 0 on success
# 	- -errno on failure
# 	int _initialize(int output_data_rate_in_hz);

# 	@brief
# 	Convert the magnetometer sample rate enum to an equivalent number in Hz.
# 	@return
# 	- 0 on success
# 	- -errno on failure
# 	int _convert_sample_rate_enum_to_hz(enum mag_sample_rate_e sample_rate);

# private:
# 	float _mag_sens_adj[3];
# 	bool _mag_initialized;
# 	mag_sample_rate_e _sample_rate;

# 	Internal reference to the icm20948 object that instantiated this mag class.

# 	icm20948 &_imu;
# };

# }
