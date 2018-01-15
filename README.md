# Cellular Connected Autonomous AR Drone 2.0
![pi-in-the-sky](http://mayorquinmachines.ai/images/pi-in-the-sky.jpg)

Put your drone on a longer leash executing programmed flight on a powered Pi zero. Perform YOLO object recognition connect over Hologram CLI.

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
The wiring of the pi is very simple for this project. We used a USB to TTL converter to power the raspberry pi through the GPIO pins using the drone's battery. Connecting the power and ground pins to pins 2 and 6 of the pi. Connect the usb end to the usb port at the top of the AR Drone 2.0 next to the battery, where you would normally plug in a usb to store video. Other than that, connect the pi cam using the ribbon cable for pi zero and use a microusb to usb converter to plug in the Hologram Nova. 
![pi drone wiring](http://mayorquinmachines.ai/images/robocopter_bb.png)

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
```

