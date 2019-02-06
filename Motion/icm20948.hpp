/****************************************************************************
 *
 *   Copyright (C) 2016 Julian Oes. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 * 3. Neither the name PX4 nor the names of its contributors may be
 *    used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 * OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 ****************************************************************************/

#pragma once

#include "ImuSensor.hpp"
#include "icm20948_mag.hpp"

namespace DriverFramework
{
//#define MPUREG_WHOAMI			0x75
#define ICMREG_WHOAMI			0x00
#define ICMREG_USER_CTRL		0x03
#define ICMREG_PWR_MGMT_1		0x06
#define ICMREG_PWR_MGMT_2		0x07
#define ICMREG_INT_PINICFG		0x0F
#define ICMREG_INT_ENABLE		0x10
#define ICMREG_INT_ENABLE1		0x11
#define ICMREG_INT_ENABLE2		0x12
#define ICMREG_INT_ENABLE3		0x13
#define ICMREG_I2C_MST_STATUS	0x17	
#define ICMREG_INT_STATUS		0x19	
#define ICMREG_INT_STATUS1		0x1A
#define ICMREG_INT_STATUS2		0x1B
#define ICMREG_ONT_STATUS3		0x1C
#define ICMREG_ACCEL_XOUT_H		0x2D
#define ICMREG_ACCEL_XOUT_L		0x2E
#define ICMREG_ACCEL_YOUT_H		0x2F
#define ICMREG_ACCEL_YOUT_L		0x30
#define ICMREG_ACCEL_ZOUT_H		0x31
#define ICMREG_ACCEL_ZOUT_L		0x32
#define ICMREG_GYRO_XOUT_H		0x33
#define ICMREG_GYRO_XOUT_L		0x34
#define ICMREG_GYRO_YOUT_H		0x35
#define ICMREG_GYRO_YOUT_L		0x36
#define ICMREG_GYRO_ZOUT_H		0x37
#define ICMREG_GYRO_ZOUT_L		0x38
#define ICMREG_TEMP_OUT_H		0x39
#define ICMREG_TEMP_OUT_L		0x3A
#define ICMREG_EXT_SLV_SNS_D00	0x3B
#define ICMREG_EXT_SLV_SNS_D01  0X3C
#define ICMREG_EXT_SLV_SNS_D02  0X3D
#define ICMREG_EXT_SLV_SNS_D03	0X3E
#define ICMREG_EXT_SLV_SNS_D04	0X3F
#define ICMREG_EXT_SLV_SNS_D05	0x40
#define ICMREG_EXT_SLV_SNS_D06	0x41
#define ICMREG_EXT_SLV_SNS_D07	0x42
#define ICMREG_EXT_SLV_SNS_D08	0x43
#define ICMREG_EXT_SLV_SNS_D09	0X44
#define ICMREG_EXT_SLV_SNS_D10	0X45
#define ICMREG_EXT_SLV_SNS_D11	0X46
#define ICMREG_EXT_SLV_SNS_D12  0X47
#define ICMREG_EXT_SLV_SNS_D13	0X48
#define ICMREG_EXT_SLV_SNS_D14	0X49
#define ICMREG_EXT_SLV_SNS_D15	0X4A
#define ICMREG_EXT_SLV_SNS_D16	0X4B
#define ICMREG_EXT_SLV_SNS_D17	0X4C
#define ICMREG_EXT_SLV_SNS_D18	0X4D
#define ICMREG_EXT_SLV_SNS_D19	0X4E
#define ICMREG_EXT_SLV_SNS_D20  0x4F
#define ICMREG_EXT_SLV_SNS_D21	0X50
#define ICMREG_EXT_SLV_SNS_D22	0X51
#define ICMREG_EXT_SLV_SNS_D23	0X52
#define ICMREG_FIFO_EN1			0X66
#define ICMREG_FIFO_EN2			0X67
#define ICMREG_FIFO_RST			0X68
#define ICMREG_FIFO_MODE		0X69
#define ICMREG_FIFO_COUNTH		0X70
#define ICMREG_FIFO_COUNTL		0X71
#define ICMREG_FIFO_R_WR		0X72
#define ICMREG_DATA_RDY_STS		0X74
#define ICMREG_FIFO_CFG			0X76
#define ICMREG_REG_BANK_SEL		0X7F


//USER BANK 2
#define ICMREG_GYRO_DIV		0x00
#define ICMREG_GYRO_CONFIG_1	0x01
#define ICMREG_ACCEL_DIVH		0x10
#define ICMREG_ACCEL_DIVL		0x11
#define ICMREG_ACCEL_CONFIG		0x14
#define ICMREG_ACCEL_CONFIG2	0X15
#define ICMREG_FSYNC_CONFIG		0x52

//USER BANK 3
#define ICMREG_I2C_MST_CTRL		0x01 
#define ICMREG_I2C_MST_DELAY_CTRL	0x02
#define ICMREG_I2C_SLV0_ADDR	0x03
#define ICMREG_I2C_SLV0_REG		0x04
#define ICMREG_I2C_SLV0_CTRL	0x05
#define ICMREG_I2C_SLV4_ADDR	0x13
#define ICMREG_I2C_SLV4_REG		0x14
#define ICMREG_I2C_SLV4_CTRL	0x15
#define ICMREG_I2C_SLV4_DO		0x16
#define ICMREG_I2C_SLV4_DI		0x17



	

// Length of the FIFO used by the sensor to buffer unread
// sensor data.
#define ICM_MAX_LEN_FIFO_IN_BYTES 512

// Configuration bits ICM 9250
#define BIT_SLEEP			0x40
#define BIT_H_RESET			0x80
#define MPU_CLK_SEL_AUTO	0x01

#define BITS_USER_CTRL_DMP_EN		0x80
#define BITS_USER_CTRL_FIFO_EN		0x40
#define BITS_USER_CTRL_FIFO_RST		0x1F
#define BITS_USER_CTRL_I2C_MST_EN  	0x20
#define BITS_USER_CTRL_I2C_IF_DIS  	0x10
#define BITS_USER_CTRL_I2C_MST_RST  	0x02

#define BITS_CONFIG_FIFO_MODE_OVERWRITE	0x00
#define BITS_CONFIG_FIFO_MODE_STOP	0x40

#define BITS_GYRO_ST_X			0x80
#define BITS_GYRO_ST_Y			0x40
#define BITS_GYRO_ST_Z			0x20
#define BITS_FS_250DPS			0x00
#define BITS_FS_500DPS			0x01
#define BITS_FS_1000DPS			0x02
#define BITS_FS_2000DPS			0x03
#define BITS_FS_MASK			0x03
// This is FCHOICE_B which is the inverse of FCHOICE
#define BITS_BW_3600HZ			0x02
// The FCHOICE bits are the same for all Bandwidths below 3600 Hz.
#define BITS_BW_LT3600HZ		0x00

#define BITS_DLPF_CFG_196HZ		0x00
#define BITS_DLPF_CFG_151HZ		0x08
#define BITS_DLPF_CFG_119HZ		0x10
#define BITS_DLPF_CFG_51HZ		0x18
#define BITS_DLPF_CFG_24HZ		0x20
#define BITS_DLPF_CFG_11HZ		0x21
#define BITS_DLPF_CFG_6HZ		0x30
#define BITS_DLPF_CFG_361HZ		0x38
#define BITS_DLPF_CFG_MASK		0x38
#define BITS_DLPF_FCHOICE		0x01

#define BITS_FIFO_ENABLE_TEMP_OUT	0x01
#define BITS_FIFO_ENABLE_GYRO_XOUT	0x02
#define BITS_FIFO_ENABLE_GYRO_YOUT	0x04
#define BITS_FIFO_ENABLE_GYRO_ZOUT	0x08
#define BITS_FIFO_ENABLE_ACCEL		0x10
#define BITS_FIFO_ENABLE_SLV3		0x08
#define BITS_FIFO_ENABLE_SLV2		0x04
#define BITS_FIFO_ENABLE_SLV1		0x02
#define BITS_FIFO_ENABLE_SLV0		0x01


#define BITS_ACCEL_CONFIG_02G		0x00
#define BITS_ACCEL_CONFIG_04G		0x02
#define BITS_ACCEL_CONFIG_08G		0x04
#define BITS_ACCEL_CONFIG_16G		0x06

// This is ACCEL_FCHOICE_B which is the inverse of ACCEL_FCHOICE
#define BITS_ACCEL_CONFIG2_BW_1130HZ	0x08
#define BITS_ACCEL_CONFIG2_BW_41HZ		0x03

#define BITS_I2C_SLV0_EN    0x80
#define BITS_I2C_SLV0_REG_DIS	0x20
#define BITS_I2C_SLV0_READ_8BYTES 0x08
#define BITS_I2C_SLV0_READ_10BYTES 0x0A
#define BITS_I2C_SLV0_GRP	0x10
#define BITS_I2C_SLV0_SWP	0x40
#define BITS_I2C_SLV1_EN    0x80
#define BITS_I2C_SLV1_DIS   0x00
#define BITS_I2C_SLV2_EN    0x80
#define BITS_I2C_SLV4_EN    0x80
#define BITS_I2C_SLV4_DONE  0x40

#define BITS_SLV4_DLY_EN    0x10
#define BITS_SLV3_DLY_EN    0x08
#define BITS_SLV2_DLY_EN    0x04
#define BITS_SLV1_DLY_EN    0x02
#define BITS_SLV0_DLY_EN    0x01

#define BIT_RAW_RDY_EN		0x01
#define BIT_INT_ANYRD_2CLEAR	0x10

#define BITS_INT_STATUS_FIFO_OVERFLOW	0x1F

#define BITS_I2C_MST_CLK_304_KHZ	0x08
#define BITS_I2C_MST_CLK_432_KHZ	0x0D

#ifndef M_PI_F
#define M_PI_F 3.14159265358979323846f
#endif

#if defined(__DF_EDISON)
// update frequency 250 Hz
#define icm20948_MEASURE_INTERVAL_US 4000
#elif defined(__DF_RPI_SINGLE)
// update frequency 1000 Hz,if using rpi1,rpi zero,1000hz may be to higher,please reduce the frequency
#define icm20948_MEASURE_INTERVAL_US 500
#else
// update frequency 1000 Hz
#define icm20948_MEASURE_INTERVAL_US  500
#endif

// -2000 to 2000 degrees/s, 16 bit signed register, deg to rad conversion
#define GYRO_RAW_TO_RAD_S 	 (2000.0f / 32768.0f * M_PI_F / 180.0f)

// TODO: include some common header file (currently in drv_sensor.h).
#define DRV_DF_DEVTYPE_icm20948 0x41

#define MPU_WHOAMI_ICM20948			0xEA
#define MPU_WHOAMI_9250_REAL		0x73

#pragma pack(push, 1)
struct fifo_packet {
	int16_t accel_x;
	int16_t accel_y;
	int16_t accel_z;
	int16_t gyro_x;
	int16_t gyro_y;
	int16_t gyro_z;
	int16_t temp;
};
struct fifo_packet_with_mag {
	int16_t accel_x;
	int16_t accel_y;
	int16_t accel_z;
	int16_t gyro_x;
	int16_t gyro_y;
	int16_t gyro_z;
	int16_t temp;
	char mag_st1; // 14 mag ST1 (1B)
	int16_t mag_x; // 15-16 (2B)
	int16_t mag_y; // 17-18 (2B)
	int16_t mag_z; // 19-20 (2B)
	char dummy1;		// reads register 0x17 but 
	char mag_st2; // 21 mag ST2 (1B)
};
// This data structure is a copy of the segment of the above fifo_packet_with_mag data
// struture that contains mag data.
struct mag_data {
	char mag_st1; // mag ST1 (1B)
	int16_t mag_x; // uT (2B)
	int16_t mag_y; // uT (2B)
	int16_t mag_z; // uT (2B)
	char mag_st2; // mag ST2 (1B)
};
#pragma pack(pop)

class icm20948: public ImuSensor
{
public:
	icm20948(const char *device_path, bool mag_enabled = false) :
		ImuSensor(device_path, icm20948_MEASURE_INTERVAL_US, mag_enabled), // true = mag is enabled
		_last_temp_c(0.0f),
		_temp_initialized(false),
		_mag_enabled(mag_enabled),
#if defined(__DF_EDISON)
		_packets_per_cycle_filtered(4.0f), // The FIFO is supposed to run at 1kHz and we sample at 250Hz.
#else
		_packets_per_cycle_filtered(8.0f), // The FIFO is supposed to run at 8kHz and we sample at 1kHz.
#endif
		_mag(nullptr)
	{
		m_id.dev_id_s.devtype = DRV_DF_DEVTYPE_icm20948;
		// TODO: does the WHOAMI make sense as an address?
		m_id.dev_id_s.address = MPU_WHOAMI_ICM20948;
	}

	// @return 0 on success, -errno on failure
	int writeReg(int reg, uint8_t val)
	{
		return _writeReg(reg, val);
	}

	int readReg(uint8_t address, uint8_t &val)
	{
		return _readReg(address, val);
	}

	int modifyReg(uint8_t address, uint8_t clearbits, uint8_t setbits)
	{
		return _modifyReg(address, clearbits, setbits);
	}

	// @return 0 on success, -errno on failure
	virtual int start() override;

	// @return 0 on success, -errno on failure
	virtual int stop() override;

protected:
	virtual void _measure() override;
	virtual int _publish(struct imu_sensor_data &data) = 0;

private:
	// @returns 0 on success, -errno on failure
	int icm20948_init();

	// @returns 0 on success, -errno on failure
	int icm20948_deinit();

	// @return the number of FIFO bytes to collect
	int get_fifo_count();

	void reset_fifo();

	void clear_int_status();

	float _last_temp_c;
	bool _temp_initialized;
	bool _mag_enabled = 0;
	float _packets_per_cycle_filtered;

	icm20948_mag *_mag;
};

}
// namespace DriverFramework
