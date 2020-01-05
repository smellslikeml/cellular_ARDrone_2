
# Cellular Connected Autonomous AR Drone 2.0
![ardrone_nova](https://hackster.imgix.net/uploads/attachments/406284/20180112_230948_xJJlkJM25e.jpg?auto=compress%2Cformat&w=740&h=555&fit=max)

Put your drone on a longer leash executing programmed flight on a powered Pi zero. Second part of a YOLO object recognition project using Hologram Nova, see [here](https://github.com/mayorquinmachines/PoochPak). Contest entry with additional information [here](https://www.hackster.io/pie_in_the_sky/cellular-connected-autonomous-ar-drone-2-0-0feb3d). More drone hacking [here](http://smellslikeml.com/drone_pwn.html). We modified [this repo](https://github.com/fkmclane/python-ardrone) for ardrone control on our raspberry pi. 

## Hardware
We used:
* [Parrot AR Drone 2.0](https://www.amazon.com/Parrot-AR-Drone-2-0-Elite-Quadcopter/dp/B00FS7SU7K/ref=sr_1_1_sspa?s=electronics&ie=UTF8&qid=1515981794&sr=1-1-spons&keywords=parrot%2Bar%2Bdrone%2B2.0&th=1)
* [Raspberry Pi Zero](https://www.amazon.com/Raspberry-Starter-Power-Supply-Premium/dp/B0748MBFTS/ref=sr_1_5?s=electronics&ie=UTF8&qid=1515127853&sr=1-5&keywords=raspberry+pi+zero)
* [Hologram Nova USB Modem](https://hologram.io/nova/)
* [Pi Camera](https://www.amazon.com/Raspberry-Starter-Power-Supply-Premium/dp/B0748MBFTS/ref=sr_1_5?s=electronics&ie=UTF8&qid=1515127853&sr=1-5&keywords=raspberry+pi+zer://www.amazon.com/Camera-Video-Module-Webcam-Raspberry/dp/B071NYSXY9/ref=sr_1_4?s=electronics&ie=UTF8&qid=1515981842&sr=1-4&keywords=raspberry+pi+zero+camera)
* [USB to TTL Converter](https://www.amazon.com/gp/product/B009T2ZR6W/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1)

## Software
Requirements:
- [Raspbian Jessie image 2017-06-21](http://downloads.raspberrypi.org/raspbian/images/raspbian-2017-06-23/2017-06-21-raspbian-jessie.zip)
- [hologram-python-sdk](https://github.com/hologram-io/hologram-python)
- [Hologram Data Router Dashboard](https://dashboard.hologram.io/)

## Wiring it up
![pi drone wiring](https://hackster.imgix.net/uploads/attachments/407063/robocopter_bb_ljN1bPDd1J.png?auto=compress%2Cformat&w=740&h=555&fit=max)
The wiring of the pi is very simple for this project. We used a USB to TTL converter to power the raspberry pi through the GPIO pins using the drone's battery. Connecting the power and ground pins to pins 2 and 6 of the pi. Connect the usb end to the usb port at the top of the AR Drone 2.0 next to the battery, where you would normally plug in a usb to store video. Other than that, connect the pi cam using the ribbon cable for pi zero and use a microusb to usb converter to plug in the Hologram Nova.

# Install
Compatibility between project dependencies requires python3.4 as default python3. You should burn
[this](http://downloads.raspberrypi.org/raspbian/images/raspbian-2017-06-23/2017-06-21-raspbian-jessie.zip) specific
image for your raspberry pi zero.
After making this image and wiring the pi, boot up and go through the first-time boot configuration.
You should make sure to:
* Under *Advanced Options*, Expand filesystem
* Under *Localization Options* change timezone
* Change User password

After a reboot, git clone this repo
```
cd ~/
git clone https://github.com/smellslikeml/cell_pwn_drone
cd cell_pwn_drone
```
And run the install script
```
./install.sh
./ardrone_setup.py
```
## Configuration
* Position drone upside down to access pi and disable flight mode
* Set DEVICEKEY in config.py
* Set /etc/wpa_supplicant/wpa_supplicant.conf to the drone's SSID
* Reboot, connect peripherals, note the time (Pi off wifi on drone network)
* As root (sudo su), set crontab for the time based on start time
* Unplug keyboard, plug in Hologram Nova
* From Hologram Dashboard, prepare for 'land' command to break flight
* Unplug HDMI after reboot and position drone
* Monitor flight with Dashboard for kill switch

## TODO
* Work out monitor issue
* Set process
* Create remote Start, Reboot 
* awscli download to flight instructions from S3 bucket
* text location, slackbot images?
