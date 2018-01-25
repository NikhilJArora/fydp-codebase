# fydp-codebase
The FYDP (Fourth Year Design Project) is targeted towards attempting to build a sensor for determining parking lot occupance through via a camera.  Using a camera enables us to be able to determine occupancy for more than one spot for each sensor.  

## What the codebase contains?
This codebase contains the image processing and the motor control code.  

## Image Processing:

### rev 0 prototype: (DONE)
* take two imgs (car and no_car)
* clean them (flip and grayscale)
* define regions where cars exist (regions of interest) - just squares for now
* slice the two imgs using regions of interest
* flatten the resultant matrix for analysis
* compute summary stats for both car and no_car
* determine a decent way to distiguish between car and no_car

### rev 1 prototype: 
* need to have a interface to select region for parking slots for given camera angle


### Future: 
* setup parkinglot simulation env to achieve algorithmic and dynamic line detection 


## NOTES:

### The prototype camera:

* 1080p which is `1080 X 1920` in pixel count
  * will need to downscale images to what will be used in production env

### Prof Tung's Advice:

* don't need to work on line detection alg for now, not a priority.  get the classifier working first 
* utilize model ensembling to combine multiple approaches into our final classifier

### Current Activity:

* prep the dataset
  * downscale all images to `1080 X 1920` pixels
  * for each image define regions of image 
  * slice the images into parking spots based on regions of interest
  * label data manually based on `y=1 (occ) or y=0 (unocc)` or `y=1 (event) or y=0 (nonevent)`
  * save to labelled folders 
  * what do you 
* Method 1: build classifier using summary stats method for each parking spot
  * prep the dataset: 
    * grayscale the image
    * flatten each image
    * compute the summary stats for each image `(x,y)`, storing each summary stat as a input feature
    * create feature for each summary statistic stored in X (vector) and store Y as {1,2} being the label
    * repeat for all images 
    * create a csv training set and the pipeline to create it 
  * train the classifier:
    * start with the simplest approach so start with logisitic regression 
    * split our dataset into test/train
    * train our classifier and score it using train 
    * evaluate the performance and take discussion from here 
* Method 1: build classifier using summary stats method for each parking spot
