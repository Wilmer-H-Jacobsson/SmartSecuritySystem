Created by: Wilmer Hallin Jacobsson

Student credentials: wh222dj

Date: 2022 july 4th

# Smart (and simple) Security System


In this tutorial I will show you how to create your own (simple) security system using a microcontroller (ESP32), a motion sensor (AM312), some code (MicroPython), your phone, Google Sheets and the platform IFTTT.

  


**Time estimation for project: 4 hours**

 



## 1. Objectives


### 1.1 The why

After purchasing a lot of different sensors and trying to make many of them work, I got tired. It was harder than I initially anticipated. To first find information on how to properly connect this sensor with the esp32, then (often) having to find a library that was written in python and finally finding info on how to set up the code in the program was breathtaking. There was almost always a small error that led to hours trying to fix it and resulting in other issues. After getting 3 sensors to work I thought the motion sensor was the one that would best hold on its own (I did not see a way that could utilize multiple of them, not a way that would bring any more value anyway). Since I had been looking through countless youtube videos I had stumbled across a guy who connected his motion sensor to the service IFTTT. I was sort of familiar with it and could see how IFTTT sending me a message on the phone if the motion sensor was triggered could be a cool project. So I was thinking, “what if I could get a notification on my phone every time someone entered my room?”. The project therefore became sort of a simple security system.


### 1.2 Purpose

The purpose of this tutorial is to guide the reader through, step by step, how to create their own security system using the same material and software as I did.


### 1.3 Insights that the project might bring

Hopefully this tutorial will bring insights in microcontrollers and sensors (hardware), setting up a coding environment for a ESP32, a bit of microPython coding, connecting a microcontroller to wifi, sending an HTTP request and some understanding about the service IFTTT.

 
  
  



## 2. Material

 
  


| **Material’s name**                                 | **What it does**                                                                                                                                | **Where to buy**                                                                                                                                         | **Price** |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| ESP32 (ESP32-WROOM with DEVKITV1)                   | A microcontroller. It stores and runs programs and has multiple pins for connections to sensors. It also has the capability of running on WiFi. | <https://sizable.se/P.CE9S1/ESP32> \[2022-07-04]                                                                                                         | 94 kr     |
| USB- to micro-USB-cable (that can transfer data)    | Transfers electricity between the computer and the ESP32 so it both can charge the microcontroller and program it.                              | <https://www.kjell.com/se/produkter/mobilt/ladda-koppla/kablar-adaptrar/micro-usb-kablar/linocell-micro-usb-kabel-med-bojskydd-2-m-p97282> \[2022-07-04] | ~100 kr   |
| A computer with an USB-port (i used a USB 2.0 port) | It lets you code the project with a nice interface and send it to your microcontroller.                                                         | Any computer with an operating system that is not too old.                                                                                               | \-        |
| Motion Sensor (Mini PIR AM312)                      | Sense movement in a restricted area and can send data about this to another computer.                                                           | <https://sizable.se/P.JMSYC/Mini-PIR-Rorelsesensor-AM312> \[2022-07-04]                                                                                  | 25 kr     |
| A Breadboard                                        | A board filled with simple connections to make it easier to connect your devices (sensors and microcontroller) together.                        | <https://www.kjell.com/se/produkter/el-verktyg/elektronik/elektroniklabb/luxorparts-kopplingsdack-400-anslutningar-2-pack-p36283> \[2022-07-04]          | 99 kr     |
| Cables (male to male)                               | Cables connect the electricity between your devices (or in our case, between the devices and the breadboard)                                    | <https://www.kjell.com/se/produkter/el-verktyg/elektronik/elektroniklabb/kopplingskablar-hane-hane-65-pack-p87212> \[2022-07-04]                         | 99 kr     |




## 3. Environment setup


### 3.1 Why I choose Atom IDE

I chose Atom’s IDE as my enviroment and MicroPython as my coding language since both of these were recommended by the instructors of the course. I tried out Arduino’s IDE and for quite a while I was determined that I was going to use that instead but since I wanted to learn Python much more then C++ it came down to me redoing half my project in Atom instead. I also thought that Arduino’s IDE made it too easy (if that is even possible) since their IDE really was designed for microcontrollers. Arduino IDE did also give me errors that I was not able to fix.


### 3.2 Setting up the environment

If you are struggling with any of the steps I am about to mention, just know that it is completely normal. Very often, your problems are just a google search away from being fixed so don’t lose your head. Patience is key.

**Step 0: Operating system**

I am using macOS (Montery) for this tutorial. With that said you could probably follow along quite well with windows (10 or above).

**Step 1: install python**

You need to have python installed on your computer in order for this to work. Follow the link:<https://www.python.org/downloads/>.

**Step 2: install node.js**

Next, you will need node.js. Follow this link:<https://nodejs.org/en/download/>.

**Step 3: install xcode**

This might not be necessary for everyone but for me an error would not go away unless I got myself Xcode. It is also nice not to have to wait for it to download and install (about 2 hours) when you are coding. Follow the link:<https://developer.apple.com/xcode/>.

**Step 4: install Atom**

Go to<https://atom.io/> and choose your OS.

**Step 5: install pymakr plugin in Atom**

1. Go to “Atom” > “preferences…”
2. Go to “install”
3. in the search bar, search for “pymakr”
4. Press “install” on the one from Pycom
5. Once downloaded, a new window should cover up the lower part of Atom.


**Step 6: install a driver for ESP32**

Sometimes the OS will do this by itself when it recognizes a new device. But to be safe we can download this driver:<https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>

(go to “downloads” and download the one for your OS).

Just to be sure it was installed, you can restart the computer.


**Step 7: flash your ESP32 and make it compatible with microPython**

Link to another tutorial on this:<https://hackmd.io/@lnu-iot/SyZ2diUOq#Mac-OS>

1. Plug your ESP32 to your computer.
2. Go to<https://nabucasa.github.io/esp-web-flasher/>
3. In the right upper corner, select “460800 baud” from the dropdown and press “connect”
4. You will get a new little window with the devices that are plugged in to your computer. For me, this was the right one (picture below), but you might have to try some of them before finding which one that is right for you.

![](https://lh5.googleusercontent.com/LJXSLgjhOV9DT2JZnt0GcDbwYtfkjneF014kOZ0gdlieeE6g-RZP39gkWYVifn9AMIWBp3PqMlWDXa9SZylPpX4jv0FntQpVmDwenJa-kMBItJKi98dbK332VcWaXYkaYkg9ofjTBwXVndxeX5o)

(“kopplad means connected in Swedish)

5. In my case, I had to hold down the “boot” button (on the ESP32) as soon as I click the blue “connect” button in the little window in order for the connection to work.
6. I keep holding the “boot” button until the code have runned and I get 2 new buttons on the screen to click: “clear” and “program”. Once again hold down the “boot” button and press the “clear” button on the screen.
7. Once the clear is done, download this file:<https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin>
8. Type in “1000” in the first input field and press the button on the right of it. Choose the file that you just downloaded. Hold down the “boot” button once again and this time press “program”. Once the code has stopped running, you can close the tab.

**Step 8: Copy my code to your project**

You can either clone my Github repository or create your own folder and files and copy and paste the code.

There are at least 3 ways to clone the repository: With git, with Github Desktop App and by doing it inside Atom. I prefered doing it with the Github Desktop App.

1. first i went to this site:<https://desktop.github.com/> to download it. Zip it up and move it to your “Applications” folder. Login in with your github account.
2. Press “File” and then “clone repository”.
3. Click on the URL tab and paste in this:<https://github.com/Wilmerrrrr/smartSecuritySystem.git>
4. Choose where you want to store the files localy and then press clone.
5. You can then press “open in Atom” to view the project there.

Alternatively, as I said, you could also create your own folder and files and then copy the code.

1. Click on “Add project folder…”
2. choose a location for the folder
3. create a new file by clicking on “File” then “new File”
4. name it boot.py
5. create another one and name it main.py
6. create a third one and name it config.py (these 3 files are usually the standard for a microPython program).
7. Copy and paste the code from here:<https://github.com/Wilmerrrrr/smartSecuritySystem>

**Step 9: Connect your ESP32 to Atom**

1. go to Atom and inside the pyMakr-box, click on settings.
2. click on global settings
3. a new tab should open up with settings for PyMakr
4. scroll down inside the settings until you see “Device Adresses”
5. in the input field type “/dev/” followed by your device name like this “/dev/tty.usbserial-0001”. (You can find the name for your device by typing “ls /dev/” inside a terminal).
6. Shut down Atom and plug out and plug back in the ESP32 to your computer.
7. Start Atom again and inside the pyMakr window, 1. choose the project you created and 2. your device.
8. If everything went right the toggle on the left should be green and the REPL should give you this “>>>” where you can type code. If it is red, try replugging the device again and close the device tab and open a new one.

**Step 10: How you upload code**

To upload code, you simply save the files in the project and then tap on the arrow that is pointing up in the PyMakr window.

**Step 11: create an account on IFTTT and set up an “applet”**

1. Go to<https://ifttt.com/> and follow the instructions for creating an account.
2. Press the create button to create a new applet
3. click on “add” right beside “If this” and find “Webhooks”. This will be our trigger.
4. Choose “Receive a web request” and enter a name and click on “create trigger” . I named mine “smart_security_system”.
5. Next, click on “Add” besides “Then That”.
6. Find and click on “notifications” and choose “Send a notification from the IFTTT app”
7. Here you can type any message, I choose “Someone is in your room!”. Click on “create action”.
8. Once again you are brought back to the “if this, then that” page. This time, click on the plus sign under “then that” to add another action.
9. Search for “google sheets” and click on the result. Choose “Add row to spreadsheet”.
10. On the first dropdown, type in/connect to your google account. Give your spreadsheet a name (could be any).
11. Under “formatted row” type in the following: “{{Value1}} {{Value2}}|||1”. The driver folder path could be anything. Press create action.

**Step 12: Set up the config.py file**

1. While in IFTTT, go to the homepage and press your avatar picture in the upper right and then choose “my services”.
2. Scroll down and press on “Webhooks”. Next, press “documentation”.
3. With big bolded letters your webhooks key should be written at the top of the page. Copy it and add it like the picture below:

![](https://lh4.googleusercontent.com/tIeWTe9mzn-T8URi8nyEDJ9UsbseTXAeydgUhC37Fo7xchOvzZLgyQOmaD3t66f7yGAfRpaT7_AGhIqXa0yRc0_Dtlw14cCV4-FAFQe8CIp04ldBLQCN6rcitc9jrn-fxpdW4B6OSwjR4UXKiD0)

(this is not my real key, you should not share it to anyone).

4. As you can see in the picture, do also add the name of the Webhook event name that you typed in earlier.
5. Inside the config.py file, change the wifi name and password to match your own wifi:

![](https://lh3.googleusercontent.com/9TVKgaocZYZ6O4gDyhN6O-e2JNo1OYujrIbi9uk9vUHa5ZkcIr8fQAlC4K8cNkhmUY6ujc9PdrUx18_TIC6i5sfZxvsIdm5DE3vnO116FWBsPMD6DZ_ciELDiATL8TanF70cbigyoaCksT1cbZ4)

Make sure you use a WiFi with 2,4 GHz or the ESP32 can not connect.

**Step 13: download the IFTTT app**

Go onto your phone and search for IFTTT in the App Store or Google Play. Make sure to log into the same account as the one created before.


## 4. Putting everything together
[![](https://lh5.googleusercontent.com/UfTEr0iS6X3T_CmMCrAIbAc3i2_FRlXLlcF5PABfYPE6N92mn0k1BW2-A2eD5nkMr75HNzYNZtKRVKGH6wi3XYTd566pzVYq9uH3c4RhbFYZyti7K_AychW8ZckLNuCRLJf_XK7IIUXpxZUtJP4)](https://github.com/iot-lnu/applied-iot/tree/master/sensor-examples/HC-SR501%20-%20PIR%20Sensor)

_Source for picture:_[_https://github.com/iot-lnu/applied-iot/tree/master/sensor-examples/HC-SR501%20-%20PIR%20Sensor_](https://github.com/iot-lnu/applied-iot/tree/master/sensor-examples/HC-SR501%20-%20PIR%20Sensor)__


## 5. Platforms and infrastructure

### Why I chose IFTTT

After testing the possibility of using MQTT as a platform I chose in the end IFTTT. I almost chose MQTT since there existed a very handy tutorial for that platform but in IFTTT I got a peak of the potential to get a notification on my phone from my program which I thought was too cool not to choose. It turned out that IFTTT also gave me what I would call a better way to gather my data then MQTT. In MQTT you could personalize your own dashboard for your various sensor data but there were no satisfying ways of presenting dates that my project required. IFTTT lets me send the dates and times when my motion sensor is triggered to Google Sheets which feel like a nicer place to store your data in terms of the many more possibilities an excel file has to be turned into great visual diagrams and could easily be imported to other database managers or programs for more customized diagrams.

In terms of functionality, IFTTT has got a lot of connection to various service providers such as Google, Spotify, Slack and many, many more and can therefore be used in a lot of different ways. You simply give an ‘if statement’ like “if I post something on Instagram” and then give it a ‘then statement’ like “then post the same post on Twitter”. You can both have multiple triggers and multiple actions on the triggers (this does however come with a cost of 31 kr/month). If you want a completely free solution you could use both IFTTT and MQTT, the first one to send notification to your phone and second one to store the data (although somewhat difficult to represent in a timeline or similar).


## 6. The code

There are 3 files in my project: boot.py, config.py and main.py. They all carry at least one important part of the code. Boot.py is where the program looks to first and holds the set up for the wifi connection:
``` python=
# Setting up a wifi connection
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect(config.WIFI_SSID, config.WIFI_PASS)

while not sta_if.isconnected():
  pass

print('network config:', sta_if.ifconfig())
```

Config.py keeps the credentials for the wifi, the configuration for the motion sensor (PIR) and the Webhooks request:
``` python=
# WiFi credentials
WIFI_SSID = 'WIFI_NAME'
WIFI_PASS = 'WIFI_PASS'

# pir sensor config
motionDetected = 1
noMotionDetected = 0
hold_time_sec = 5

# Webhooks / IFTTT config
event_name = "EVENT_NAME"
webhooks_key = "WEBHOOKS_KEY"
```

Finally, the main.py file does 3 things: (1) keeps the setup for sending a request to an IFTTT link. When this function is called, it takes the date and time as an argument. This is to get the exact time of the motion and to pass this date and time with the HTTP request. The setup with Webhooks we did earlier will put these in the Google sheets file. (It is passed as 2 values since HTTP “values” didn’t allow spaces as in “2022-07-04 13.04.56”.)
``` python=
def http_post(values, url = 'https&#x3A;//maker.ifttt.com/trigger/{}/with/key/{}'.format(config.event_name, config.webhooks_key)):
  import socket # Used by HTML get request
  import time # Used for delay
  value1, value2 = values.split(' ', 1) # values = current date and time
  url += '?value1={}'.format(value1) # value1 = the date --- Passing on the date in the request to be stored in sheets-file
  url += '&value2={}'.format(value2) # value2 = the time --- Passing on the time in the request to be stored in sheets-file
  _, _, host, path = url.split('/', 3) # Separate URL request
  addr = socket.getaddrinfo(host, 80)\[0]\[-1] # Get IP address of host
  s = socket.socket() # Initialise the socket
  s.connect(addr) # Try connecting to host address
  # Send HTTP request to the host with specific path
  s.send(bytes('POST /%s HTTP/1.0\\r\\nHost: %s\\r\\n\\r\\n' % (path, host), 'utf8'))
  time.sleep(1) # Sleep for a second
  rec_bytes = s.recv(10000) # Receive response
  s.close()
```

(2) main.py keeps the PIR setup so that the microcontroller knows which pin the motion sensor is connected to:
``` python=
pir = Pin(13 ,mode=Pin.IN)
```

(3) Last, it contains the loop to keep checking if the motion sensor is triggered and if so, calling on the HTTP function higher up in the main-file. It needs a few extra lines to get the correct date and time to know when the motion sensor is triggered. The “http_post” caller also takes the values argument which looks a bit long but really is just the current date and time in a format that Google Sheets liked better than the default.
``` python=
print("Starting Detection")
while True:
  if pir()==config.motionDetected:
  ntptime.settime() #syncs the to (almost) local time
  t = time.localtime()
  http_post(values="{:04d}-{:02d}-{:02d} {:02d}.{:02d}.{:02d}".format(t\[0], t\[1], t\[2], t\[3] + 2, t\[4], t\[5])) # calls for the HTTP request function (I have added 2 hours to match my local time)
  print("Motion Detected! Time: {:04d}-{:02d}-{:02d} {:02d}.{:02d}.{:02d}".format(t\[0], t\[1], t\[2], t\[3] + 2, t\[4], t\[5])) # optional print out to the REPL

#if the motion sensor isn't triggered it will just pass
if pir()==config.noMotionDetected:
  pass

# A short delay to stop the program from sending multiple requests after a single motion is detected
time.sleep(config.hold_time_sec)
```

## 7. The physical network layer

The data from the sensor goes directly through the wires and into the pins of the microcontroller which through WiFi sends a webhook request to an IFTTT address which triggers the actions to first send a message to my phone via the IFTTT app and then creates a new row in a specific Google Sheets document where it types the date and time of the motion. The data is sended irregularly, that is, whenever the motion sensor is triggered, data is being sent.


## 8. Visualization and user interface

Since I use Google Sheets to store my data it was very easy to create a diagram. Though it is debatable if this is the best way to represent this data (time stamps) like in the picture to the left, in my opinion it is completely acceptable.

![](https://lh4.googleusercontent.com/U9OVgakdUeEwmjair0U7Ivrz3kKkkpZYUCoxhurhQHnAFBmTbC6oSroQLcqxGtXR4-oU5ECW8RPxZxs5MvGvspswhZKktrwrOYTSkhBKDMgTwf60RmMtTki5lK7G0-Bt7DHZo4zXlyRiOMIVIMU)

You have got your list of every occurance when the motion sensor has been triggered in the first column of the sheet and a simple diagram to go along with it that can be customized. As I mentioned earlier, the format of an excel file makes this data homogen since it is a widely accepted file format. As you can see on this second picture, it is also possible to filter your data.

![](https://lh4.googleusercontent.com/3GXtSUT4RfCYLhMQ1alGa2dKxwQyBMnSTN7qfO-ExIyrGcFqOqWIJnXja2H1Bp7--QhFvvl9oY10J8MdIncom_28aqCyidujjXXKTIOUGt4-AWoQ5L0dy-SD4J_3lP-bh-L8FuLczZbkGO1NBqo)

You can filter it to result in just detection on a certain day or over a specific period of days (for some reason they have not added the feature to filter by time unfortunately). Data is saved in the sheets file as soon as a new row has been added (which is irregular as pointed out in the last section). I really tried to find a way to delete old data after a certain period of time had passed but it turned out to be too difficult and time consuming. Google do have API’s for all their apps Sheets included, but there was so many additional steps to make it work that I: A. could barely make it work with 6 hours of fixing and B. would add too many additional steps in this tutorial and the result would not at all, in my opinion, be comparable with that effort.


## 9. Finalizing the design

I would say that the project overall went great, I learned many, many new things in the process of making it. I will mostly remember that IoT is not as hard as it looks even though it might consume some hours just trying to find the causes of errors. It is also a way bigger area of expertise than my initial impression. I will also bring with me that python as a language is not as difficult to learn as I first thought as someone who is used to javascript.

Unfortunately, I was not too happy with my result. I felt it was way too simple and I feel a bit embarrassed that I could not pull off a project with a little more complexity. Hopefully I will keep IoT as a hobby and try more challenging projects in the future.

![](https://lh3.googleusercontent.com/xkFPeSweD2h99rN2HtqdEvw9vK6Tb4hUEBI7QLgWQKhZ5ReqGGm03vaINhv-7JvyTJubhQqgNdvXfBynyhGDR_sO2_cbDZXAO9dNrFuygHO92Jnr2EquGnYMoRGuR5I5ObwW3DofgIJQ7aVREts)![](https://lh4.googleusercontent.com/NH9Nv33cbYJbOrJJDsiiLJP6Cy1ouwhtXF1a6ajXILgMFi-ZnYq9GfLpgelMdgz8__T3rZp245VNduOnUoStXEc2n_zYoFi2XVmz8T5dFpGDfCp-3U7776_SGS-eM6NbW227KDP_Ssp2i5X7vWY)
