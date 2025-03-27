import os, sys, time, socket, hashlib, argparse


####################################################################
##                                                                ##
##          Versoin: 2.0.3                                        ##
##          Name: Geo-Phone                                       ##
##          Author: evilfeonix                                    ##
##          Date: 29 - FEBUARY - 2024                             ##
##          Website: www.evilfeonix.com                           ##
##          Email: evilfeonix@gmail.com                           ##
##          Twiter: https://x.com/evilfeonix                      ##
##          Github: https://github.com/evilfeonix                 ##
##          Youtube: https://youtube.com/evilfeonix               ##
##                                                                ##
####################################################################


#####    A free and open source OSINT tool that enables users to gathers information,
#####    And also enables users to track and map phone numbers from around the world.


stop="\033[0m"
red="\033[91;1m"
cyan="\033[96;1m"
blue="\033[94;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"


add=f"{purple}[{stop}+{purple}]{green} "
error=f"{purple}[{stop}-{purple}]{red} "
info=f"\033[97;1m[{purple}•\033[97;1m]{purple} "
note=f"\033[97;1m[{purple}!\033[97;1m]{purple} "
version = "2.0.3.6"


def slow(F3):
    for a in F3 + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./300)

def load(F3):
    for x in F3:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)
    


def F30N1X():
    usage = f"""
 Useage: python3 {sys.argv[0]} [OPTION...]
------------
      | OPTIONS
      |----------
            | -u <Script Updating>       | Update Geo-Phone Script for Better performance
            | -a <About Tool & Author>   | About Tool and Author's Contact Information
            | -c <Victim's Country Code> | Specify Victim's Country Code WithOut "+" .eg 234
            | -p <Victim's Phone Number> | Specify Victim's Phone Number'
      | EXAMPLES
      |----------
            | python3 {sys.argv[0]} -u                   | Script Updating
            | python3 {sys.argv[0]} -a F30N1X            | About Tool & Author
            | python3 {sys.argv[0]} -c 234 -p 7000000000 | Specify victim's Country Code & Phone Number         
    """
    os.system("clear || cls")
    return usage
    os.sys.exit()

def banner():
    os.system("clear || cls")
    return f"""{purple} 
_________               ______________          {cyan}v\033[97;1m2.0.3{purple}
__/ ____/__________     ___/ __ \__/ /___________________ 
_/ / __ _/ _ \  __ \______/ /_/ /_/ __ \  __ \\\  __ \  _ \\
/ /_/ / /  __/ /_/ /_____/  ___/_/ / / / /_/ // / / /  __/
\____/  \___/\____/     /_/     /_/ /_/\____//_/ /_/\___/ 
{stop}"""


try:import requests, opencage, countryinfo, phonenumbers, urllib.request
except ModuleNotFoundError:
    
    slow(banner())
    slow(f"\n{note}Ops! Sorry,"                                    )
    slow(f'{info}Look Like This Script Is Missing Some Requirment.{red}')
    slow('===========================================================')
    slow(f'        	{green}Run: {purple}bash installer.sh{red}   ')
    slow('===========================================================')
    slow('\033[0m')
    os.sys.exit()
    
from countryinfo import CountryInfo
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, timezone, geocoder, is_valid_number

def internet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    
def aboutus():
    
    slow(banner())
    slow(f"{red}===========================================================")
    slow(f'    {info}Tool Name      {blue}:>>{purple}  Geo-Phone')
    slow(f'    {info}Version        {blue}:>>{purple}  v[{version[:-2]}]')
    slow(f'    {info}Author         {blue}:>>{purple}  evilfeonix')
    slow(f'    {info}Latest Update  {blue}:>>{purple}  13-02-2025')
    slow(f'    {info}Github         {blue}:>>{purple}  Digital Firebird')
    slow(f'    {info}Youtube        {blue}:>>{purple}  Digital Firebird')
    slow(f'    {info}Website        {blue}:>>{purple}  www.evilfeonix.com{red}')
    slow(f'    {info}Email          {blue}:>>{purple}  evilfeonix@gmail.com{red}')
    slow("===========================================================")

    slow(f"""
   {purple} Follow Us on Github
   {purple} Fork our Repositories  
   {purple} Give our Repositories a Star
   {purple} Contribute to our Repositories  
   {purple} Contact us at evilfeonix@gmail.com 
{stop}
         [++] {purple}Subscribe To Our YouTube Channel{stop} [++]{red}
===========================================================""")
    act=input(f'{purple}Press [{stop}ENTER{purple}]{purple} To Continue{stop} ')
    evilfeonix="https://github.com/evilfeonix" 
    os.system(f"xdg-open {evilfeonix}")
    os.sys.exit()
    
def get_remote_hash(url):
   try:
      response = urllib.request.urlopen(url)
      data = response.read()
      return hashlib.md5(data).hexdigest()
   except Exception as e:
      slow(f"{error}Please Check Your Internet Connection.{stop}")
      slow(f"")
      os.sys.exit()

def get_local_hash(script_path):
   try:
      with open(script_path, 'rb') as f:
         data = f.read()
         return hashlib.md5(data).hexdigest()
   except Exception as e:
      slow(f"{error}Error reading local script: {e}.{stop}\n")
      os.sys.exit()


def updateus(): 
    slow(banner())
    try:
        script_url = "https://github.com/evilfeonix/Geo-Phone/raw/main/phone.py"
        script_path = os.path.abspath(__file__)
        
        remote_hash = get_remote_hash(script_url)
        local_hash = get_local_hash(script_path)
        
        if remote_hash and local_hash and remote_hash == local_hash:
            time.sleep(2)
            slow(f"{error}Geo-Phone is Up-To Date.{stop}\n")
            os.sys.exit()
        
        time.sleep(1)
        slow(f"{add}Update Found...")
        time.sleep(1)
        slow(f"{add}Downloading latest Version...")
        time.sleep(3)
        urllib.request.urlretrieve(script_url, script_path)
        slow(f"{stop}\n")
        time.sleep(5)
        slow(header())
        slow(f"{red}===========================================================")
        slow(f"""{info}Geo-Phone Successfully Updated...,

   {purple} Follow Us on Github
   {purple} Fork our Repositories  
   {purple} Give our Repositories a Star
   {purple} Contribute to our Repositories  
   {purple} Contact us at evilfeonix@gmail.com  
{stop}
         [++] {purple}Subscribe To Our YouTube Channel{stop} [++]{red}
===========================================================""")
        act=input(f'{purple}Press [{stop}ENTER{purple}]{purple} To Continue{stop} ')
        evilfeonix="https://github.com/evilfeonix" 
        os.system(f"xdg-open {evilfeonix}")
        os.sys.exit()
         
    except Exception as e:
        slow(f"")
        slow(f"{error}Error Updating Geo-Phone: {e}{stop}\n")



def infoga(cncode,number):
    slow(banner())
    num = f"+{cncode}{number}"
    load(f"{add}Starting Reconnaissance Scan On {num}")
    time.sleep(1)
    try:
        load(f"{info}Fetching Basic Phone Information")
        time.sleep(2)
        try:
            phoneNumber = phonenumbers.parse(num)
            if is_valid_number(phoneNumber):
                valid_number=True
            else:
                valid_number=False
                slow(f"{error}Phone Number Seems To Be Invalid!\n")
                os.sys.exit()
        except Exception as e:
            slow(f"{error}Error Parsing Phone Number: {e}{stop}\n")
            os.sys.exit()
            
        gc = geocoder.description_for_number(phoneNumber,"en")
        c = carrier.name_for_number(phoneNumber,"en")
        load(f"{info}Collecting Country Information")
        time.sleep(2)
        if not (gc and c):
            slow(f"{error}Can Not Get Country Information!")
            time.sleep(1)
        inter = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nation = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.E164)

        load(f"{info}Running OSINT Lookup")
        time.sleep(3)
        if not (gc and c):
            slow(f"{error}Running OSINT Lookup Error!")
            time.sleep(1)
        gc = geocoder.description_for_number(phoneNumber,"en")  # country
        tz = timezone.time_zones_for_number(phoneNumber)        # timezone
        c = carrier.name_for_number(phoneNumber,"en")           # ISP   (INTERNET SERVICE PROVIDER)

        load(f"{info}Running OVH Scan")
        time.sleep(3)
        if not (gc and c):
            slow(f"{error}Running OVH Scan Error!")
            time.sleep(1)
        local = phoneNumber.national_number
        cncode = phoneNumber.country_code

        load(f"{info}Mapping Number")
        time.sleep(1)
        
        act=input(f'\n{purple}Press [{stop}ENTER{purple}]{purple} To Continue{stop} ')
        time.sleep(1)
        slow(banner())
        
        if (gc and c):   
            gcd = gc
            country = CountryInfo(gcd)
            iso = country.iso()["alpha2"]
            print("\033[92;1m", end="\r")

            slow("===========================================================")
            slow(f"[!] Attemting To Track Location Of {cyan}{inter.replace(' ','-')}{green}  [!]")
            slow("===========================================================")

            time.sleep(3)
            slow(f"    {cyan}International Format{blue}  :>>  {green}{inter}")
            slow(f"    {cyan}National Format{blue}  :>>  {green}{nation}")
            slow(f"    {cyan}E164 Format{blue}  :>>  {green}{e164}")
            slow(f"    {cyan}Local Format{blue}  :>>  {green}{local}")
            slow(f"    {cyan}Country Found{blue}  :>>  {green}+{cncode} ({iso})")
            slow(f"    {cyan}Country Name{blue}  :>>  {green}{gcd} (+{cncode})")
            slow(f"    {cyan}Time Zone ID{blue}  :>>  {green}{tz[0]}")
            slow(f"    {cyan}Service Providers{blue}  :>>  {green}{c}")
            slow(f"    {cyan}Chacking Validation{blue}  :>>  {green} Found")
            
            slow(f"")

            data = country.info()
            for i, j in data.items():
                slow(f"    {cyan}{i}{blue}  :>>  {green}{j}")

            slow(f"")

            slow(f"    {cyan}Number{blue}  :>>  {green}(+{cncode}) {local}")
            slow(f"    {cyan}Country{blue}  :>>  {green}{gcd} ({iso})")
            slow(f"    {cyan}Location{blue}  :>>  {green}Found")

            try:
                Key = "42c84373c47e490ba410d4132ae64fc4"  # ~mine
                # Key = "03c48dae07364cabb7f121d8c1519492"    # 
                coder = OpenCageGeocode(Key)
                query = str(gcd)

                results = coder.geocode(query)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']

                slow(f"    {cyan}Latitude{blue}  :>>  {green}{lat}")
                slow(f"    {cyan}Longitude{blue}  :>>  {green}{lng}")
                addr = coder.reverse_geocode(lat,lng)

                if addr:
                    address = addr[0] ['formatted']
                    slow(f"    {cyan}Address{blue}  :>>  {green}{address}")
                else:slow(f"    {purple}No Address Found For The Given Phone Number.")

            except Exception:
                time.sleep(1)
                slow(f"{error}Please Check Your Internet Connection.{stop}\n")
                os.sys.exit()
                
            url=f"https://google.com/maps/place/{lat},{lng}/@{lat},{lng},16z" 
            os.system(f"xdg-open {url}")

            slow(f"                     ")
            act=input(f'{purple}Press [{stop}ENTER{purple}]{purple} To Continue{stop} ')
            time.sleep(2)

            slow(banner())
            slow(f"{red}===========================================================")
            slow(f"""{info}Kindly Support Us By The Following!,

   {purple} Follow Us on Github
   {purple} Fork our Repositories  
   {purple} Give our Repositories a Star
   {purple} Contribute to our Repositories  
   {purple} Contact us at evilfeonix@gmail.com  
{stop}
         [++] {purple}Subscribe To Our YouTube Channel{purple} [++]{red}
===========================================================""")
            act=input(f'{purple}Press [{stop}ENTER{purple}]{purple} To Continue{stop} ')
            evilfeonix="https://github.com/evilfeonix" 
            os.system(f"xdg-open {evilfeonix}")
            slow(f"{red}")
            slow(f"==========================================================={stop}")
            slow(f" ^_^           {purple}Thanks For Using Geo-Phone{stop}             ^_^ ")
            slow("===========================================================")
            slow('\033[0m\n')
            os.sys.exit()
            
        else:
            c = "Unkown"
            gc = "Unkown"
            gcd = gc

            print("\033[91;1m", end="\r")
            slow("===========================================================")
            slow(f"[!] Attemting To Track Location Of {cyan}{inter.replace(' ','-')}{red} [!]")
            slow("===========================================================")
            time.sleep(3)

            slow(f"    {cyan}International Format{blue}  :>>  {red}{number}")
            slow(f"    {cyan}National Format{blue}  :>>  {red}{nation}")
            slow(f"    {cyan}E164 Format{blue}  :>>  {red}{e164}")
            slow(f"    {cyan}Local Format{blue}  :>>  {red}{local}")
            slow(f"    {cyan}Country{blue}  :>> {red} Not Found")
            slow(f"    {cyan}Time Zone ID{blue}  :>>  {red}{tz[0]}")
            slow(f"    {cyan}Service Providers{blue}  :>>  {red}{c}")
            slow(f"    {cyan}Chacking Validation{blue}  :>> {red} Not Found")
            slow(f"")

            act=input(f'{purple}Press [{stop}ENTER{purple}]{purple} To Continue{stop} ')
            time.sleep(2)

            slow(banner())
            slow(f"\n{error}The Phone Number Specified Here Was Invalid!.    ")
            slow("===========================================================")
            slow(f"    {stop}Please Specify A Valid Phone Number.             ")
            slow(f"    Also Ensure That The Country Code you Provided is     ")
            slow(f"    Corresponded To The Phone Number Provided.{red}         ")
            slow(f"==========================================================={stop}")
            slow(f" ^_^           {purple}Thanks For Using Geo-Phone{stop}             ^_^ ")
            slow(f"{red}===========================================================")
            slow('\033[0m\n')
            os.sys.exit() 


    except Exception as err:
        time.sleep(3)
        slow(f"\n{error}Could Not Get The Location Of This Number.       ")
        slow("===========================================================")
        slow(f"{stop}    Please Specify A Valid Phone Number.             ")
        slow(f"    Also Ensure That The Country Code you Provided is     ")
        slow(f"    Corresponded To The Phone Number Provided.{red}         ")
        slow(f"==========================================================={stop}")
        slow(f" ^_^           {purple}Thanks For Using Geo-Phone{stop}             ^_^ ")
        slow(f"{red}===========================================================")
        slow('\033[0m\n')
        os.sys.exit() 

def main():
    parser = argparse.ArgumentParser( 
        description = "a free and open OSINT tool that enables users to gathers information" + ", "
                    + "track and map phone numbers from around the world.")

    parser.add_argument( 
        "-c", "--code", 
        dest= "coutry_code", 
        type=str, help='Specify victims country code without "+" eg.234')

    parser.add_argument( 
        "-p", "--phone", 
        dest= "phone_number", 
        type=str, help="Specify victim's phone number")

    parser.add_argument( 
        "-a", "--about", 
        dest= "about_tool",  
        type=str, help="About Tool and Author's Contact Information")

    parser.add_argument( 
        "-u", "--update", 
        dest= "update_script",  
        action ="store_true", help='Update Geo-Phone Script for Better performance')

    argument = parser.parse_args()
    number = argument.phone_number
    cncode = argument.coutry_code
    update = argument.update_script
    about = argument.about_tool

    # if internet():
    if not internet():
        slow(f"\n{error}Please Check Your Internet Connection{stop}\n")
        os.sys.exit()

    if update:updateus()
    elif number and cncode:infoga(cncode,number)
    elif str(about).upper() in ["FEONIX","F30N1X"]:aboutus()
    else:print(F30N1X())
    return argument


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        slow(f"")
        slow(f"\n{error} User Requested an Interrupt!")
        load(f"{error} Program Running Down{stop}")
        time.sleep(2)
        slow(f"")
        os.sys.exit()
