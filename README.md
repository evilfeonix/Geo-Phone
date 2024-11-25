![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg) 

# Geo-Trace

![EvilFeonix Basic v1.0](https://github.com/evilfeonix/Geo-Trace/blob/main/phone.png)

# Geo-Trace
**Geo-Trace** is an OSINT tool that enables users to track and map phone numbers from around the world. With a user-friendly interface, **GeoTrace** provides quick insights into the origin of any phone number, displaying the country and marking an approximate location on a map. 


This tool is ideal for anyone curious about incoming calls, telecom data analysis, or exploring how phone numbers are distributed across regions. GeoTrace combines the power of Python with interactive mapping to make phone number tracking easy, insightful, and visually engaging.


## Geo-Trace: Beginner Gray Hat Hacking
**Geo-Trace**, is a basic Python script that aimed to Fetch and information based on the given phone number and it country, before tracking and mapping the phone phone numbers.

This Python script will:

1. Fetch and gather information on a given phone number.
2. track and display the approximately location (country, state, and street) on the screen.
3. and also map the phone number using the coordinate (latitud, and langitude) by directing user to a map.


## is Available on:
- *Termux*
- *Kali Linux*

    
## Installation in Termux and Usage:
Download Termux app from google play store and type following commands:
    
```
      pkg update && apt upgrade
```
```
      pkg install git
```
```
      pkg install python3
```
```
      git clone https://github.com/evilfeonix/Geo-Trace.git
```
```
      cd Geo-Trace
```
```
      pip install -r requirements.txt
```
```
      python3 phone.py -c <countryCode> -p <phoneNumber>
```


Download and Install kali-linux from their official website and type following commands:
 
```
      sudo apt update && sudo apt upgrade
```
```
      sudo apt install git
```
```
      sudo apt install python3 python3-pip
```
```
      git clone https://github.com/evilfeonix/Geo-Trace.git
```
```
      cd Geo-Trace
```
```
      pip install -r requirements.txt
```
```
      python3 phone.py -c <countryCode> -p <phoneNumber>
```

## Geo-Trace Usage:
```
 Useage: python3 phone.py [OPTION...]
------------
      | OPTIONS
      |----------
            | -u <Script Updating>       | Update Geo-Trace Script for Better performance
            | -a <About Tool & Author>   | About Tool and Author's Contact Information
            | -c <Victim's Country Code> | Specify Victim's Country Code WithOut "+" .eg 234
            | -p <Victim's Phone Number> | Specify Victim's Phone Number'
      | EXAMPLES
      |----------
            | python3 phone.py -u                   | Script Updating
            | python3 phone.py -a F30N1X            | About Tool & Author
            | python3 phone.py -c 234 -p 7000000000 | Specify victim's Country Code & Phone Number
```
### Geo-Trace Map
A sample of **Geo Trace** outputed map:

![EvilFeonix Basic v1.0](https://github.com/evilfeonix/Geo-Trace/blob/main/maps.png)

### License

[GNU General Public License v3.0](https://github.com/VirusZzHkP/Email-Spoofing/blob/main/LICENSE)

### Follow Us
website: https://www.evilfeonix.com

web-blog: https://www.evilfeonix.com/blog

youtube: https://www.youtube.com/@3V1LF30N1X

linkedin: https://www.linkedin.com/evilfeonix
