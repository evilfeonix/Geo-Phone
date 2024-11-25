import os,sys,time,argparse


# Versoin: 2.0.1
# Name: Geo-Trace
# Author: evilfeonix
# Date: 29 - FEBUARY - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


#####    A free and open source OSINT tool that enables users to gathers information, track and map phone numbers from around the world.
#####    Geo-Trace is a Python-based project designed to track and map phone numbers globally. 
#####    By leveraging phone number data, Geo-Trace helps users determine the country of origin for any given number and displays its approximate location on a map. 
#####    Whether you're curious about the origin of a call or need location data for analysis, Geo-Trace offers a simple and accessible solution for anyone interested in phone number tracking.
#####    With Geo-Trace, you can visualize phone data on a map, providing both geographic insights and a practical tool for anyone interested in telecommunications and data visualization.


stop="\033[0m"
red="\033[31;1m"
cyan="\033[36;1m"
blue="\033[34;1m"
darkred="\033[91m"
green="\033[32;1m"
yellow="\033[33;1m"
purple="\033[35;1m"


add=f"{red}[{stop}+{red}]{purple} "
error=f"{blue}[{stop}-{blue}]{red} "
info=f"{green}[{stop}•{green}]{purple} "
version = "2.0.1.6"


def slow(F3):
    for a in dhf + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./300)
def load(F3):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)
lib = ["countryinfo","lolcat","pyfiglet","requests","phonenumbers","opencage"]


def F30N1X():
    usage = """
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
    """
    return usage
    os.sys.exit()


try:import pyfiglet, lolcat
except ModuleNotFoundError:
    slow(f"\n{notice}Attention!!!.")
    slow(f"{info2}You will firstly need to run:{stop}")
    slow("     pip install -r requirements.txt")
    slow(f"{yellow}Before trying to run the main script.")
    os.sys.exit()


try:import requests, opencage, countryinfo, phonenumbers
except ModuleNotFoundError:
    os.system("pyfiglet Geo-Trace | lolcat")
    load(f"\t{info}Setting up your environment{stop}")
    for i in lib:os.system(f"pip install {i}")
    os.system("pip install webbrowser")
    os.system("pip install lolcat")
    os.system("clea" + "r || cls")
    print(F30N1X())
    os.sys.exit()
    
from countryinfo import CountryInfo
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, timezone, geocoder

def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    
def aboutus():
    os.system("clea" + "r || cls")
    os.system(f"pyfiglet Geo-Phone | lolcat{red}")
    slow("="*60)
    slow(f'\t{info}Tool Name      {blue}:>>{purple}  Geo-Trace')
    slow(f'\t{info}Version        {blue}:>>{purple}  v[{version[:-2]}]')
    slow(f'\t{info}Author         {blue}:>>{purple}  evilfeonix')
    slow(f'\t{info}Github         {blue}:>>{purple}  Evil {darkred}FeoniX')
    slow(f'\t{info}Youtube        {blue}:>>{purple}  Evil {darkred}FeoniX')
    slow(f'\t{info}Latest Update  {blue}:>>{purple}  24-11-2024')
    slow(f'\t{info}Website        {blue}:>>{purple}  www.evilfeonix.com{red}')
    slow("="*60)
    slow("")
    act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue{stop}')
    os.sys.exit()
    
def updateus():
    os.system("clea" + "r || cls")
    os.system("pyfiglet Geo-Trace | lolcat")
    load(f"{add}Checking For Update")
    server=requests.get("https://github.com/evilfeonix/Geo-Trace/blob/main/phone.py")
    sertxt=server.text
    sertxt=sertxt.replace("\n","")
    server=sertxt.replace("\r","")

    with open(sys.argv[0], 'r') as fr:
        client = fr.read()
        if not server==client:
            slow(f"{add}Update Found!")
            time.sleep(1)
            act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue{stop}')
            os.system("clea" + "r || cls")
            os.system("pyfiglet Geo-Trace | lolcat")
            load(f"{add}Updating Geo-Trace!")
            time.sleep(4)
            with open(sys.argv[0], 'w+') as fw:
                fw.write(sertxt)
            slow(f"{add}Geo-Trace Successfully Updated.{stop}")
            os.sys.exit()
        slow(f"{add}Geo-Trace is up-to date!{stop}")
        os.sys.exit()


def infoga(cncode,number):
    try:
        num = f"+{cncode}{number}"
        phoneNumber = phonenumbers.parse(num)
        inter = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nation = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.E164)
        gc = geocoder.description_for_number(phoneNumber,"en")
        tz = timezone.time_zones_for_number(phoneNumber)
        c = carrier.name_for_number(phoneNumber,"en")
        cncode = phoneNumber.country_code
        local = phoneNumber.national_number
        
        if (gc and c):   
            gcd = gc
            country = CountryInfo(gcd)
            iso = country.iso()["alpha2"]
            slow("\033[31;1m")
            slow("="*60)
            slow(f"[!] Attemting to track location of {inter.replace(" ","-")}  [!]")
            slow("="*60)
            load(f"\t{purple}Running local scan")
            slow(f"\t{cyan}International Format{blue} :>>  {green}{inter}")
            slow(f"\t{cyan}National Format{blue} :>>  {green}{nation}")
            slow(f"\t{cyan}E164 Format{blue} :>>  {green}{e164}")
            slow(f"\t{cyan}Local Format{blue} :>>  {green}{local}")
            slow(f"\t{cyan}Country Found{blue} :>>  {green}+{cncode} ({iso})")
            time.sleep(1/3)
            
            Do = input(f"{info}Do you want to get country infomation {blue}[{stop}Yes{blue}/{stop}nO{blue}]{%red} :>>  {green}")
            
            if Do.upper() in ["YES","Y"]:
                data = country.info()
                load(f"\t{purple}Collecting country info")
                for i, j in data.items():
                    slow(f"\t{cyan}{i} {blue} :>> {green}{j}")
            elif Do.upper() in ["NO","N"]:slow(f"{info}We hope you know what you are doing!!!")
            else:
                time.sleep(1)
                slow(f"\t{error}Invalid Option{stop}")
                os.sys.exit()
                
            slow(f"\t{cyan}City/Area{blue} :>>  {green}{gcd} (+{cncode})")
            slow(f"\t{cyan}Time Zone ID{blue} :>>  {green}{tz}")
            slow(f"\t{cyan}Service Providers{blue} :>>  {green}{c}")
            if (phonenumbers.is_valid_number(phoneNumber)):slow(f"\t{cyan}Chacking Validation{blue} :>> {green} Found")
            else:slow(f"\t{cyan}Chacking Validation{blue} :>> {red} Not Found")
            
            load(f"\t{purple}Running Numverify.com scan")
            slow(f"\t{cyan}Number{blue} :>> {green} (+{cncode}) {local}")
            slow(f"\t{cyan}Country{blue} :>> {green} {gcd} ({iso})")
            slow(f"\t{cyan}Location{blue} :>> {green} Found")
            
            load(f"\t{purple}Checking for approximate location")
            try:
                # Key = "42c84373c47e490ba410d4132ae64fc4"
                Key = "03c48dae07364cabb7f121d8c1519492"
                code = OpenCageGeocode(Key)
                query = str(gcd)
                results = code.geocode(query)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                slow(f"\t{cyan}Latitude{blue} :>>  {green}{lat}{stop}, {cyan}Longitude{blue} :>>  {green}{lng}")
                addr = coder.reverse_geocode(lat,lng)
                if addr:
                    address = addr[0] ['formatted']
                    slow(f"\t{purple}Approximate Location{red} :>>  {green}{address}")
                else:slow(f"\t{info}No address found for the given phone number.")
            except Exception:
                time.sleep(1)
                slow(f"\t{error}Please check your internet connection.{stop}")
                os.sys.exit()
                
            try:import webbrowser
            except ModuleNotFoundError:
                time.sleep(1)
                slow(f'{error}U will have to install "webbrowser" manually\n    type "pip install webbrowser" to install webbrowser.{stop}')
                os.sys.exit()
                
            try:
                # https://cdn.apple-mapkit.com/ti/csr/1.x.x/mk-csr.js?mapkitVersion=5.78.87
                # https://api.opencagedata.com/geocode/v1/json?q=0.565656+0.656565&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en
                # https://api.what3words.com/v3/convert-to-3wa?coordinates=0.565656%2C0.656565&language=it&format=json
                # https://google.com/map/place/0.565656,0.656565/@0.565656,0.656565,16z

                url=f"https://google.com/maps/place/{lat},{lng}/@{lat},{lng},16z" 
                webbrowser.open(url,new=1,autoraise=True)
            except NameError:
                time.sleep(1)
                slow(f"\t{error}Could not get Aerial Coverage for this number.{stop}")
                os.sys.exit()
            load(f"\t{purple}Running OVH scan")
            load(f"\t{purple}Running OSINT footprint reconnissance")
            slow(f"\t{green}Generating scan URL on 411.com!")
            slow(f"\t{cyan}Scan URL {blue}:>>{green} https://www.411.com/phone/{inter.replace(" ","-")}")
            time.sleep(2)
            slow(f"\t{green}\nPrograms rans Successfully\nThanks for Using this Tool{stop}")
            os.sys.exit()
            
        else:
            cc = "Unkown"
            gc = "Unkown"
            gcd = gc
            slow("\033[31;1m")
            slow("="*60)
            slow(f"[!] Attemting to track location of {inter.replace(" ","-")} [!]")
            slow("="*60)
            load(f"\t{cyan}Running local scan"%(purple))
            slow(f"\t{cyan}International Format{blue} :>>  {red}{number}")
            slow(f"\t{cyan}National Format{blue} :>>  {red}{nation}")
            slow(f"\t{cyan}E164 Format{blue} :>>  {red}{e164}")
            slow(f"\t{cyan}Local Format{blue} :>>  {red}{local}")
            slow(f"\t{cyan}Country{blue} :>> {red} Not Found")
            slow(f"\t{cyan}City/Area{blue} :>>  {red}{gcd}")
            slow(f"\t{cyan}Time Zone ID{blue} :>>  {red}{tz[0]}")
            slow(f"\t{cyan}Service Providers{blue} :>>  {red}{cc}")
            if (phonenumbers.is_valid_number(phoneNumber)):slow(f"\t{cyan}Chacking Validation{blue} :>> {red} Not Found")
            else:slow(f"\t{cyan}Chacking Validation{blue} :>> {red} Not Found")
            time.sleep(1)
            slow(f"\n{error}The phone number specified here was invalid!.\n{error}Please specify a valid phone number and make sure that the country code you provided is corresponded to the phone number.{stop}\n")
            os.sys.exit() 
    except Exception as err:
        time.sleep(1)
        slow (f"\n{error}Could not get the location of this number. Please specify a valid phone number {stop}\n")
        os.sys.exit() 

def main():
    parser = argparse.ArgumentParser( description = "a free and open source OSINT tool that enables users to gathers information, track and map phone numbers from around the world.")
    parser.add_argument ( "-c" , "--code" , dest= "coutry_code", type=str, help='Specify victims country code without "+" eg.234')
    parser.add_argument ( "-p" , "--phone" , dest= "phone_number", type=str, help="Specify victim's phone number")
    parser.add_argument ( "-a" , "--about" , dest= "about_tool",  type=str, help="About Tool and Author's Contact Information")
    parser.add_argument ( "-u" , "--update" , dest= "update_script",  action ="store_true",help='Update Geo-Trace Script for Better performance')
    argument = parser.parse_args()
    number = argument.phone_number
    cncode = argument.coutry_code
    update = argument.update_script
    about = argument.about_tool
    if not internet():
        slow(f"\n{error}Please check your internet connection{stop}")
        os.sys.exit()
    if update:updateus()
    elif str(about).upper() in ["FEONIX","F30N1X"]:aboutus()
    elif number and cncode:infoga(cncode,number)
    else:print(F30N1X())
    #return argument


if __name__ == "__main__":
    main()

