/*
 * MPU.h
 *
 *  Created on: Aug 29, 2023
 *      Author: SAI SUDDHIR
 */

#ifndef INC_MPU_H_
#define INC_MPU_H_

#include "stm32f4xx_hal.h"

void MPU_init (void);
void accel_read (void);
void gyro_read (void);



#endif /* INC_MPU_H_ */
