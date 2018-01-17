# fydp-codebase
The FYDP (Fourth Year Design Project) is targeted towards attempting to build a sensor for determining parking lot occupance through via a camera.  Using a camera enables us to be able to determine occupancy for more than one spot for each sensor.  

## What the codebase contains?
This codebase contains the image processing and the motor control code.  

## Image Processing:

### rev 0 prototype:
* take two imgs (car and no_car)
* clean them (flip and grayscale)
* define regions where cars exist (regions of interest) - just squares for now
* slice the two imgs using regions of interest
* flatten the resultant matrix for analysis
* compute summary stats for both car and no_car
* determine a decent way to distiguish between car and no_car

### rev 1 prototype:
* instead of fixed boxes for regions of interest, use sets of vertices 
*  transform the resultant shape into a rectangle 

### rev 2 prototype:
* basic UI to define the parking spot

### rev 3: 
* setup parkinglot simulation environment 
* work on line detection for these spots


