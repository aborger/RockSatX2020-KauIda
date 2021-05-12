# THETA WebAPI tester for Raspberry Pi

version 0.1.2-alpha

```shell
$ ./theta app --version
0.1.2-alpha
pi@raspberrypi:~/Development/webapi/build $ 
```

## working commands

```shell
$ ./theta --help
RICOH WebAPI Tester

Usage: ./theta <command> [arguments]

Global options:
-h, --help    Print this usage information.

Available commands:
  app                    information on this app. --version shows version
  autoBracket            apply test 3 image auto bracket settings
  deleteAll              DANGER: Delete all image and video files from camera
  download               Save images, thumbnails or video files to local storage.
  exposureCompensation   set exposure compensation with --value=2.0
  exposureDelay          set self timer delay in seconds
  exposureProgram        set exposure program 1 (manual), 2 (auto), 3 (aperture Z1 only), 4 (shutter), 9 (iso)
  getMetadata            Get image metadata from camera by passing URL of the file
  getMySetting           Display settings from My Settings on V, Z1, SC2, SCB. Will not work SC, or S
  getOption              Display single option
  getOptions             get camera options
  getTimeShift           get Time Shift settings. SC2B, V, Z1 only
  hdr                    Enable, save, delete, disable, and show hdr settings
  info                   Camera info: model, serialNumber, apiLevel... 
  listFiles              list all image and video files on camera
  listUrls               print and return URLs as an array of strings
  offDelay               Set or disable camera auto power off.
  preset                 SC2 only. Preset shooting modes. face, night, lens-by-lens
  reset                  Reset camera settings. Camera will turn off. Need to reconnect
  setLanguage            Z1, V only. Set language with --lang=en-US
  setModeImage           Set camera to image mode
  setMySetting           Save single setting to My Setting
  setOption              Set single option. --name=_colorTemperature --value=5000
  setShutter             set shutter speed
  shutterVolume          set shutter volume off, low, medium, max
  sleepDelay             Set or disable camera auto-sleep.
  startCapture           Start capture. Must specifiy capture mode
  state                  Camera state: batteryLevel, storageUri...
  status                 Show camera status. Requires id value returned from takePicture
  stopCapture            stops interval, video, and continuous shooting. returns list of URLs for interval shots
  takeAndDownload        Take picture. Show elapsed time. Download to local disk.
  takeAndReady           Take picture. Show elapsed time. Show file URI when ready for download
  takePicture            take picture, similar to pressing shutter button

Run "./theta help <command>" for more information about a command.
pi@raspberrypi:~/Development/webapi/build $ 
```


## Change Highlights for v0.1.2-alpha

* `theta getMySetting` now shows  saved settings in My Settings for SC2, SC2B, V, and Z1.  Does not work with SC and S as a different format is needed for the SC and S.


## Change Highlights for v0.1.1-alpha

* save and show my settings
* save and show any single option
* read it option settings from file and load into camera
* stop capture for continuous interval shots
* shutterVolume can turn off shutter volume, which is nice for continuous shooting
* fileDownload replaced with download 
* thumbWrite replaced with download
* app --version will show version of this app.

## Support

* [community.theta360.guide forum](https://community.theta360.guide/c/theta-api-usage/5)
* [WebAPI Tester Blog](https://theta360developers.github.io/webapi/)

## Release Testing

```shell
pi@raspberrypi:~/Development/webapi/build $ bash test.sh 
test completed on
Tue 16 Feb 2021 03:57:07 PM PST
Tested on
linux-gnueabihf
version of this app
0.1.2-alpha
---
firmware version
Camera firmware version: 1.60.1
camera mode
Camera model: RICOH THETA Z1
testing takePicture with check to make sure camera is ready for next command
Test of taking picture and then checking to see if picture is ready for download
---
The status ID is 655
Elapsed time: 0 seconds. State: inProgress
Elapsed time: 1 seconds. State: inProgress
Elapsed time: 2 seconds. State: inProgress
Elapsed time: 3 seconds. State: done
picture ready for download at http://192.168.1.1/files/150100524436344d42013765da9bc400/100RICOH/R0010718.JPG
testing take and save to local storage
Test of taking picture and then checking to see if picture is ready for download
---
The status ID is 656
Elapsed time: 0 seconds. State: inProgress
Elapsed time: 1 seconds. State: inProgress
Elapsed time: 2 seconds. State: inProgress
Elapsed time: 3 seconds. State: done
picture ready for download at http://192.168.1.1/files/150100524436344d42013765da9bc400/100RICOH/R0010718.JPG
Writing file from the following URL
http://192.168.1.1/files/150100524436344d42013765da9bc400/100RICOH/R0010724.JPG
download complete
image download complete
testing thumbnail
basic test complete
pi@raspberrypi:~/Development/webapi/build $ 

```

### File Test

```shell

 $ bash test_serve.sh 
test completed on
Tue 16 Feb 2021 03:58:39 PM PST
Tested on
linux-gnueabihf
version of this app
0.1.2-alpha
---
firmware version
Camera firmware version: 1.60.1
camera mode
Camera model: RICOH THETA Z1
testing file access
saving last file
Starting work on file at http://192.168.1.1/files/150100524436344d42013765da9bc400/100RICOH/R0010718.JPG
Starting download and write process for R0010718.JPG
starting python server on port 8000
CTRL-C will stop server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [16/Feb/2021 15:58:56] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [16/Feb/2021 15:59:00] "GET /R0010724.JPG HTTP/1.1" 200 -


```

