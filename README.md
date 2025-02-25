![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg) 



<div align='center'>

![Geo-Phone](https://img.shields.io/badge/Geo-Phone-blue.svg) 

![Geo-Phone](https://github.com/evilfeonix/Geo-Phone/blob/main/phone.png)

</div>

# Geo-Phone

**Geo-Phone** is an OSINT tool that enables users to track and map phone numbers from around the world. With a user-friendly interface, **GeoPhone** provides quick insights into the origin of any phone number, displaying the country and marking an approximate location on a map. 

## Tested on:
- *Termux*
- *Kali Linux*

    
## Installation in Termux and Usage:
Download Termux app from google play store and type following commands:
    
```
      apt update && apt upgrade
```
```
      apt install git
```
```
      pkg install python3
```
```
      git clone https://github.com/evilfeonix/Geo-Phone.git
```
```
      cd Geo-Phone
```
```
      bash installer.sh
```
```
      python3 phone.py -c <countryCode> -p <phoneNumber>
```


Download and Install kali-linux from their official website and type following commands:
 
```
      sudo apt update && sudo apt upgrade
```
```
      git clone https://github.com/evilfeonix/Geo-Phone.git
```
```
      cd Geo-Phone
```
```
      bash installer.sh
```
```
      python3 phone.py -c <countryCode> -p <phoneNumber>
```

## Geo-Phone Usage:
```
 Useage: python3 phone.py [OPTION...]
------------
      | OPTIONS
      |----------
            | -u <Script Updating>       | Update Geo-Phone Script for Better performance
            | -a <About Tool & Author>   | About Tool and Author's Contact Information
            | -c <Victim's Country Code> | Specify Victim's Country Code WithOut "+" .eg 234
            | -p <Victim's Phone Number> | Specify Victim's Phone Number'
      | EXAMPLES
      |----------
            | python3 phone.py -u                   | Script Updating
            | python3 phone.py -a F30N1X            | About Tool & Author
            | python3 phone.py -c 234 -p 7000000000 | Specify victim's Country Code & Phone Number
```
### Geo-Phone Map
A sample of **Geo Phone** outputed map:

![Geo-Phone v2.0.3](https://github.com/evilfeonix/Geo-Phone/blob/main/maps.jpg)


# Support US 
Support us by following us!,

Also star and fork our repositories.


### License

[GNU General Public License v3.0](https://github.com/evilfeonix/Geo-Phone/blob/main/LICENSE)

<div align=center>

Happy Phone Number OSINT & Tracking

👨🏾‍💻👨🏾‍💻👨🏾‍💻

<div>

