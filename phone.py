import os, sys, time, argparse


# Versoin: 2.0.2
# Name: Geo-Trace
# Author: evilfeonix
# Date: 29 - FEBUARY - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


#####    A free and open source OSINT tool that enables users to gathers information, track and map phone numbers from around the world.
#####    Geo-Trace is a Python-based project designed to track and map phone numbers globally. By leveraging phone number data,
#####    Geo-Trace helps users determine the country of origin for any given number and displays its approximate location on a map.


stop="\033[0m"
red="\033[91;1m"
cyan="\033[96;1m"
blue="\033[94;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"


add=f"{red}[{stop}+{red}]{green} "
error=f"{green}[{stop}-{green}]{red} "
info=f"{blue}[{stop}•{blue}]{purple} "
version = "2.0.2.6"


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
            | -u <Script Updating>       | Update Geo-Trace Script for Better performance
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


try:import requests, opencage, countryinfo, phonenumbers

except ModuleNotFoundError:
    load(f"\n{red}[!] Ops! Sorry,"                                    )
    slow(f'{info}Look Like This Script Is Missing Some Requirment.   ')
    slow('===========================================================')
    slow(f'        {green}Run: {purple}bash installer.sh{red}  	     ')
    slow('===========================================================')
    slow('\033[0m')
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
    os.system("clear || cls")
    os.system(f"figlet Geo-Trace | lolcat || figlet Geo-Trace")
    slow(f"{red}")

    slow("===========================================================")
    slow(f'\t{info}Tool Name      {blue}:>>{purple}  Geo-Trace')
    slow(f'\t{info}Version        {blue}:>>{purple}  v[{version[:-2]}]')
    slow(f'\t{info}Author         {blue}:>>{purple}  evilfeonix')
    slow(f'\t{info}Github         {blue}:>>{purple}  Evil {red}FeoniX')
    slow(f'\t{info}Youtube        {blue}:>>{purple}  Evil {red}FeoniX')
    slow(f'\t{info}Latest Update  {blue}:>>{purple}  30-12-2024')
    slow(f'\t{info}Website        {blue}:>>{purple}  www.evilfeonix.com{red}')
    slow("===========================================================")

    slow("")
    act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue{stop}')
    os.sys.exit()
    
def updateus():
    os.system("clear || cls")
    os.system(f"figlet Geo-Trace | lolcat || figlet Geo-Trace")

    slow(f"{red}")
    slow("===========================================================")
    load(f"{add}Updating Geo-Trace!")

    os.system("cd $HOME")
    os.system("rm -f -r Geo-Trace")
    os.system("git clone https://github.com/evilfeonix/Geo-Trace.git")

    slow(f"{add}Geo-Trace Successfully Updated.{stop}")
    act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue{stop}')
    os.sys.exit()


def infoga(cncode,number):
    try:
        num = f"+{cncode}{number}"
        phoneNumber = phonenumbers.parse(num)
        inter = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nation = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.E164)

        gc = geocoder.description_for_number(phoneNumber,"en")  # country
        tz = timezone.time_zones_for_number(phoneNumber)        # timezone
        c = carrier.name_for_number(phoneNumber,"en")           # ISP   (INTERNET SERVICE PROVIDER)

        local = phoneNumber.national_number
        cncode = phoneNumber.country_code
        os.system("clear || cls")
        # os.system(f"figlet Geo-Trace | lolcat || figlet Geo-Trace)
        os.system(f"pyfiglet Geo-Phone".center(100," "))
        
        if (gc and c):   
            gcd = gc
            country = CountryInfo(gcd)
            iso = country.iso()["alpha2"]
            print("\033[92;1m", end="\r")

            slow("===========================================================")
            slow(f"[!] Attemting To Track Location Of {cyan}{inter.replace(' ','-')}{green}  [!]")
            slow("===========================================================")

            time.sleep(3)
            load(f"\t{purple}Running Local Scan")
            slow(f"\t{cyan}International Format{blue} :>>  {green}{inter}")
            slow(f"\t{cyan}National Format{blue} :>>  {green}{nation}")
            slow(f"\t{cyan}E164 Format{blue} :>>  {green}{e164}")
            slow(f"\t{cyan}Local Format{blue} :>>  {green}{local}")
            slow(f"\t{cyan}Country Found{blue} :>>  {green}+{cncode} ({iso})")
            slow(f"\t{cyan}Country Name{blue} :>>  {green}{gcd} (+{cncode})")
            slow(f"\t{cyan}Time Zone ID{blue} :>>  {green}{tz[0]}")
            slow(f"\t{cyan}Service Providers{blue} :>>  {green}{c}")

            if (phonenumbers.is_valid_number(phoneNumber)):slow(f"\t{cyan}Chacking Validation{blue} :>> {green} Found")
            else:slow(f"\t{cyan}Chacking Validation{blue} :>> {red} Not Found")

            time.sleep(1/3)
            
            Do = input(f"{info}Do You Want To Get Country Infomation {blue}[{stop}Yes{blue}/{stop}nO{blue}]{red} :>>  {green}")
            
            if Do.upper() in ["YES","Y"]:
                data = country.info()
                load(f"\t{purple}Collecting Country Information")
                for i, j in data.items():
                    slow(f"\t{cyan}{i} {blue} :>> {green}{j}")
            elif Do.upper() in ["NO","N"]:slow(f"{info}We Hope You Know What You Are Doing!!!")

            else:
                time.sleep(1)
                slow(f"{error}Invalid Option{stop}\n")
                os.sys.exit()
            
            load(f"\t{purple}Running Numverify.com Scan")
            slow(f"\t{cyan}Number{blue} :>> {green} (+{cncode}) {local}")
            slow(f"\t{cyan}Country{blue} :>> {green} {gcd} ({iso})")
            slow(f"\t{cyan}Location{blue} :>> {green} Found")
            
            load(f"\t{purple}Checking For Approximate Location")

            try:
                # Key = "42c84373c47e490ba410d4132ae64fc4"  ~mine
                Key = "03c48dae07364cabb7f121d8c1519492"    # 
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

                else:slow(f"\t{info}No Address Found For The Given Phone Number.")

            except Exception:
                time.sleep(1)
                slow(f"{error}Please Check Your Internet Connection.{stop}")
                os.sys.exit()
                
            try:import webbrowser
            except ModuleNotFoundError:pass
            url=f"https://google.com/maps/place/{lat},{lng}/@{lat},{lng},16z" 

            try:
                # https://cdn.apple-mapkit.com/ti/csr/1.x.x/mk-csr.js?mapkitVersion=5.78.87
                # https://api.opencagedata.com/geocode/v1/json?q=0.565656+0.656565&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en
                # https://api.what3words.com/v3/convert-to-3wa?coordinates=0.565656%2C0.656565&language=it&format=json
                # https://google.com/map/place/0.565656,0.656565/@0.565656,0.656565,16z

                webbrowser.open(url,new=1,autoraise=True)

            except NameError:
                os.system(f"xdg-open {url}")

            os.sys.exit()
            load(f"\t{purple}Running OVH Scan")
            load(f"\t{purple}Running OSINT Footprint Reconnissance")
            slow(f"\t{green}Generating Scan URL On 411.com!")
            slow(f"\t{cyan}Scan URL {blue}:>>{green} https://www.411.com/phone/{inter.replace(' ','-')}")

            act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue{stop}')
            time.sleep(2)

            slow(f"\n{green}Programs Rans Successfully.                      ")
            slow("===========================================================")
            slow(f"         Please Specify A Valid Phone Number.             ")
            slow(f"    Also Ensure that the country code you provided is     ")
            slow(f"       corresponded to the phone number provided.         ")
            slow("===========================================================")
            slow(f" ^_^           Thanks For Using Geo-Trace             ^_^ ")
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

            load(f"\t{purple}Running Local Scan")
            slow(f"\t{cyan}International Format{blue} :>>  {red}{number}")
            slow(f"\t{cyan}National Format{blue} :>>  {red}{nation}")
            slow(f"\t{cyan}E164 Format{blue} :>>  {red}{e164}")
            slow(f"\t{cyan}Local Format{blue} :>>  {red}{local}")
            slow(f"\t{cyan}Country{blue} :>> {red} Not Found")
            slow(f"\t{cyan}City/Area{blue} :>>  {red}{gcd}")
            slow(f"\t{cyan}Time Zone ID{blue} :>>  {red}{tz[0]}")
            slow(f"\t{cyan}Service Providers{blue} :>>  {red}{c}")

            if (phonenumbers.is_valid_number(phoneNumber)):slow(f"\t{cyan}Chacking Validation{blue} :>> {red} Not Found")
            else:slow(f"\t{cyan}Chacking Validation{blue} :>> {red} Not Found")

            act=input(f'{add}Press {purple}[{stop}ENTER{purple}]{yellow} To Continue{stop}')
            time.sleep(1)

            slow(f"\n{error}The Phone Number Specified Here Was Invalid!.    ")
            slow("===========================================================")
            slow(f"         {stop}Please Specify A Valid Phone Number.             ")
            slow(f"    Also Ensure that the country code you provided is     ")
            slow(f"       corresponded to the phone number provided.{red}         ")
            slow(f"==========================================================={stop}")
            slow(f" ^_^           {purple}Thanks For Using Geo-Trace{stop}             ^_^ ")
            slow(f"{red}===========================================================")
            slow('\033[0m\n')
            os.sys.exit() 


    except Exception as err:
        time.sleep(3)
        slow(f"\n{err}")
        slow(f"\n{error}Could Not Get The Location Of This Number.       ")
        slow("===========================================================")
        slow(f"         {stop}Please Specify A Valid Phone Number.             ")
        slow(f"    Also Ensure that the country code you provided is     ")
        slow(f"       corresponded to the phone number provided.{red}         ")
        slow(f"==========================================================={stop}")
        slow(f" ^_^           {purple}Thanks For Using Geo-Trace{stop}             ^_^ ")
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
        action ="store_true", help='Update Geo-Trace Script for Better performance')

    argument = parser.parse_args()
    number = argument.phone_number
    cncode = argument.coutry_code
    update = argument.update_script
    about = argument.about_tool

    # if not internet():
    if internet():
        slow(f"\n{error}Please Check Your Internet Connection{stop}\n")
        os.sys.exit()

    if update:updateus()
    elif number and cncode:infoga(cncode,number)
    elif str(about).upper() in ["FEONIX","F30N1X"]:aboutus()
    else:print(F30N1X())
    return argument


if __name__ == "__main__":
    main()

