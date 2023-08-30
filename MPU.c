/*
 * MPU.c
 *
 *  Created on: Aug 28, 2023
 *      Author: SAI SUDDHIR
 */
#include "stm32f4xx_hal.h"
extern I2C_HandleTypeDef hi2c1;
#define MUP6050_I2C &hi2c1


#define MPU6050_ADDR 0x68
#define SMPLRT_DIV_REG 0x19
#define GYRO_CONFIG_REG 0x1B
#define ACCEL_CONFIG_REG 0x1C
#define ACCEL_XOUT_H_REG 0x3B
#define GYRO_XOUT_H_REG 0x43
#define PWR_MGMT_1_REG 0x6B
#define WHO_AM_I_REG 0x75


int16_t Accel_X_RAW = 0;
int16_t Accel_Y_RAW = 0;
int16_t Accel_Z_RAW = 0;

int16_t Gyro_X_RAW = 0;
int16_t Gyro_Y_RAW = 0;
int16_t Gyro_Z_RAW = 0;

float Ax, Ay, Az, Gx, Gy, Gz;

void MPU_init (void)
{
	uint8_t check ;
	uint8_t Data ;
	uint8_t samplerate;
	HAL_I2C_Mem_Read(&hi2c1,MPU6050_ADDR,WHO_AM_I_REG,1,&check,1,HAL_MAX_DELAY);
	if (check == 0x68)
	{
		// powering up the sensors
		Data=0;
		HAL_I2C_Mem_Write(&hi2c1,MPU6050_ADDR,PWR_MGMT_1_REG,1,&Data,1,HAL_MAX_DELAY);

		samplerate = 0x07;
		HAL_I2C_Mem_Write(&hi2c1,MPU6050_ADDR,SMPLRT_DIV_REG,1,&samplerate,1,HAL_MAX_DELAY);

		//GYRO CONFIG
		Data=0x00;
		HAL_I2C_Mem_Write(&hi2c1,MPU6050_ADDR,GYRO_CONFIG_REG,1,&Data,1,HAL_MAX_DELAY);

		//acclerometer config
		Data=0x00;
		HAL_I2C_Mem_Write(&hi2c1,MPU6050_ADDR,ACCEL_CONFIG_REG,1,&Data,1,HAL_MAX_DELAY);

	}
}


void accel_read (void)
{
	uint8_t accln[6];
	HAL_I2C_Mem_Read(&hi2c1,MPU6050_ADDR,ACCEL_XOUT_H_REG,1,accln,6,HAL_MAX_DELAY);

	Accel_X_RAW = (int16_t)(accln[0] << 8 | accln [1]);
	Accel_Y_RAW = (int16_t)(accln[2] << 8 | accln [3]);
	Accel_Z_RAW = (int16_t)(accln[4] << 8 | accln [5]);


	Ax = Accel_X_RAW/16384;
	Ay = Accel_Y_RAW/16384;
	Az = Accel_Z_RAW/16834;

}

void gyro_read (void)
{
	uint8_t gyro[6];
	HAL_I2C_Mem_Read(&hi2c1,MPU6050_ADDR,GYRO_XOUT_H_REG,1,gyro,6,HAL_MAX_DELAY);

	Gyro_X_RAW = (int16_t)(gyro[0] << 8 | gyro [1]);
	Gyro_Y_RAW = (int16_t)(gyro[2] << 8 | gyro [3]);
	Gyro_Z_RAW = (int16_t)(gyro[4] << 8 | gyro [5]);


	Gx = Gyro_X_RAW/16384;
	Gy = Gyro_Y_RAW/16384;
	Gz = Gyro_Z_RAW/16834;


}



