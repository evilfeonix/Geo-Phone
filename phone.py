import os,sys,time,argparse


# Versoin: 2.0.1
# Name: Geo-Trace
# Author: evilfeonix
# Date: 29 - FEBUARY - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


##### This is an Information Gathering tool based on SIM and it Country
##### Geo-Trace was build with the help of python programming language
##### The purpose of this script can be catagorized in-to three (3)
##### First step: Fetch information on a given phone number and it country
##### Second step: Track the location of the phone number
##### Third step: Generate a link that will directly track down the phone number on a map


# stop="\033[0m"
# red="\033[31;1m"
# blue="\033[34;1m"
# green="\033[32;1m"
# yellow="\033[33;1m"
# purple="\033[35;1m"
# cyan="\033[36;1m"
# info2 = "%s[%s•%s]%s "%(green,stop,green,purple)
# info = "%s[%s+%s]%s "%(red,stop,red,yellow)
# error = "%s[%s!%s]%s "%(blue,stop,blue,red)
# success = "%s[%s√%s]%s "%(purple,stop,purple,green)

stop="\033[0m"
red="\033[31;1m"
d_red="\033[91m"
cyan="\033[36;1m"
blue="\033[34;1m"
green="\033[32;1m"
yellow="\033[33;1m"
purple="\033[35;1m"


error="%s[%s-%s]%s "%(blue,stop,blue,red)
info2="%s[%s•%s]%s "%(green,stop,green,purple)
add="%s[%s+%s]%s "%(red,stop,red,yellow)
notice="%s[%s!%s]%s "%(blue,stop,blue,red)
success="%s[%s√%s]%s "%(purple,stop,purple,green)
first= "%s[%s01%s]%s "%(green,stop,green,purple)
second= "%s[%s02%s]%s "%(green,stop,green,purple)
third= "%s[%s03%s]%s "%(green,stop,green,purple)
version = "2.0.1.6"

lib = ["countryinfo","lolcat","pyfiglet","requests","phonenumbers","opencage"]

def slow(dhf):
    for a in dhf + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./300)
def loadbr(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)

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

# try:import lolcat, pyfiglet, requests, opencage, countryinfo, phonenumbers
try:import pyfiglet, requests, opencage, countryinfo, phonenumbers
except ModuleNotFoundError:
    os.system("pyfiglet Geo-Trace | lolcat")
    slow("\t%sSetting up ur environment%s"%(info2,stop))
    for i in lib:os.system("pip install %s"%(i))
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
    os.system("pyfiglet Geo-Phone | lolcat")
    slow("%s"%(red))
    slow("="*60)
    slow('\t%sTool Name      %s:>>%s  Geo-Trace'%(info2,blue,purple))
    slow('\t%sVersion        %s:>>%s  v[%s]'%(info2,blue,purple,version[:-2]))
    slow('\t%sAuthor         %s:>>%s  F30N1X'%(info2,blue,d_red))
    slow('\t%sGithub         %s:>>%s  Evil %sFeoniX'%(info2,blue,purple,d_red))
    slow('\t%sYoutube        %s:>>%s  Evil %sFeoniX'%(info2,blue,purple,d_red))
    slow('\t%sLatest Update  %s:>>%s  14-11-2024'%(info2,blue,purple))
    slow('\t%sWebsite        %s:>>%s  www.evilfeonix.com%s'%(info2,blue,purple,red))
    slow("="*60)
    slow("")
    act=input('%sPress %s[%sENTER%s]%s To Continue%s'%(add,purple,stop,purple,yellow,stop))
    os.sys.exit()
    
def updateus():
    os.system("clea" + "r || cls")
    os.system("pyfiglet Geo-Trace | lolcat")
    loadbr("Checking For Update")
    server=requests.get("https://github.com/evilfeonix/Geo-Trace/blob/main/phone.py")
    sertxt=server.text
    sertxt=sertxt.replace("\n","")
    server=sertxt.replace("\r","")

    with open(sys.argv[0], 'r') as fr:
        client = fr.read()
        if not server==client:
            slow("\rUpdate Found!")
            time.sleep(1)
            act=input('%sPress %s[%sENTER%s]%s To Continue%s'%(add,purple,stop,purple,yellow,stop))
            os.system("clea" + "r || cls")
            loadbr("Updating Geo-Trace!")
            time.sleep(4)
            with open(sys.argv[0], 'w+') as fw:
                fw.write(sertxt)
            slow("Geo-Trace Successfully Updated.")
            os.sys.exit()
        slow("Geo-Trace is up-to date!")
        os.sys.exit()


def infoga(cncode,number):
    try:
        num = "+%s%s"%(cncode,number)
        phoneNumber = phonenumbers.parse(num)#+
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
            slow("[!] Attemting to track location of %s  [!]" % (inter.replace(" ","-")))
            slow("="*60)
            loadbr("\t%sRunning local scan"%(purple))
            slow("\t%sInternational Format%s :>>  %s%s"%(cyan,blue,green,inter))
            slow("\t%sNational Format%s :>>  %s%s"%(cyan,blue,green,nation))
            slow("\t%sE164 Format%s :>>  %s%s"%(cyan,blue,green,e164))
            slow("\t%sLocal Format%s :>>  %s%s"%(cyan,blue,green,local))
            slow("\t%sCountry Found%s :>>  %s+%s (%s)"%(cyan,blue,green,cncode,iso))
            time.sleep(1/3)
            
            Do = input("%sDo u want to get country infomation %s[%sYes%s/%snO%s]%s :>>  %s"%(info2,blue,stop,blue,stop,blue,red,green))
            
            if Do.upper() in ["YES","Y"]:
                data = country.info()
                loadbr("\t%sCollecting country info"%(purple))
                for i, j in data.items():
                    slow("\t%s%s %s :>> %s%s"%(cyan,i,blue,green,j))
            elif Do.upper() in ["NO","N"]:slow("%sWe hope u know what u are doing!!!"%(info2))
            else:
                time.sleep(1)
                slow("\t%sInvalid Option%s"%(error,stop))
                os.sys.exit()
                
            slow("\t%sCity/Area%s :>>  %s%s (+%s)"%(cyan,blue,green,gcd,cncode))
            slow("\t%sTime Zone ID%s :>>  %s%s"%(cyan,blue,green,tz))
            slow("\t%sService Providers%s :>>  %s%s"%(cyan,blue,green,c))
            if (phonenumbers.is_valid_number(phoneNumber)):slow("\t%sChacking Validation%s :>> %s Found"%(cyan,blue,green))
            else:slow("\t%sChacking Validation%s :>> %s Not Found"%(cyan,blue,red))
            
            loadbr("\t%sRunning Numverify.com scan"%(purple))
            slow("\t%sNumber%s :>> %s (+%s) %s"%(cyan,blue,green,cncode,local))
            slow("\t%sCountry%s :>> %s %s (%s)"%(cyan,blue,green,gcd,iso))
            slow("\t%sLocation%s :>> %s Found"%(cyan,blue,green))
            
            loadbr("\t%sChecking for approximate location"%(purple))
            try:
                # Key = "42c84373c47e490ba410d4132ae64fc4"
                Key = "03c48dae07364cabb7f121d8c1519492"
                code = OpenCageGeocode(Key)
                query = str(gcd)
                results = code.geocode(query)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                slow("\t%sLatitude%s :>>  %s%s%s, %sLongitude%s :>>  %s%s"%(cyan,blue,green,lat,stop,cyan,blue,green,lng))
                addr = coder.reverse_geocode(lat,lng)
                if addr:
                    address = addr[0] ['formatted']
                    slow("\t%sApproximate Location%s :>>  %s%s"%(purple,red,green,address))
                else:slow("\t%sNo address found for the given co-ordinates."%(info2))
            except Exception:
                time.sleep(1)
                slow("\t%sPlease check ur internet connection.%s"%(error,stop))
                os.sys.exit()
                
            try:import webbrowser
            except ModuleNotFoundError:
                time.sleep(1)
                slow('%sU will have to install "webbrowser" manually\n    type "pip install webbrowser" to install webbrowser.%s'%(error,stop))
                os.sys.exit()
                
            try:
                # https://cdn.apple-mapkit.com/ti/csr/1.x.x/mk-csr.js?mapkitVersion=5.78.87
                # https://api.opencagedata.com/geocode/v1/json?q=0.565656+0.656565&key=03c48dae07364cabb7f121d8c1519492&no_annotations=1&language=en
                # https://api.what3words.com/v3/convert-to-3wa?coordinates=0.565656%2C0.656565&language=it&format=json
                # https://google.com/map/place/0.565656,0.656565/@0.565656,0.656565,16z

                url="https://api.what3words.com/v3/convert-to-3wa?coordinates=%s%2C%s&language=it&format=json"%(lat,lng)
                webbrowser.open(url,new=1,autoraise=True)
            except NameError:
                time.sleep(1)
                slow("\t%sCould not get Aerial Coverage for this number.%s"%(error,stop))
                os.sys.exit()
            loadbr("\t%sRunning OVH scan"%(purple))
            loadbr("\t%sRunning OSINT footprint reconnissance"%(purple))
            slow("\t%sGenerating scan URL on 411.com!"%(green))
            slow("\t%sScan URL %s:>>%s https://www.411.com/phone/%s"%(cyan,blue,green,inter.replace(" ","-")))
            time.sleep(2)
            slow("\t%s\nPrograms rans Successfully\nThanks for Using this Tool%s"%(green,stop))
            os.sys.exit()
            
        else:
            cc = "Unkown"
            gc = "Unkown"
            gcd = gc
            slow("\033[31;1m")
            slow("="*60)
            slow("[!] Attemting to track location of %s [!]" % (inter.replace(" ","-")))
            slow("="*60)
            loadbr("\t%sRunning local scan"%(purple))
            slow("\t%sInternational Format%s :>>  %s%s"%(cyan,blue,red,number))
            slow("\t%sNational Format%s :>>  %s%s"%(cyan,blue,red,nation))
            slow("\t%sE164 Format%s :>>  %s%s"%(cyan,blue,red,e164))
            slow("\t%sLocal Format%s :>>  %s%s"%(cyan,blue,red,local))
            slow("\t%sCountry%s :>> %s Not Found"%(cyan,blue,red))
            slow("\t%sCity/Area%s :>>  %s%s"%(cyan,blue,red,gcd))
            slow("\t%sTime Zone ID%s :>>  %s%s"%(cyan,blue,red,tz[0]))
            slow("\t%sService Providers%s :>>  %s%s"%(cyan,blue,red,cc))
            if (phonenumbers.is_valid_number(phoneNumber)):slow("\t%sChacking Validation%s :>> %s Not Found"%(cyan,blue,red))
            else:slow("\t%sChacking Validation%s :>> %s Not Found"%(cyan,blue,red))
            time.sleep(1)
            slow("\n%sThe phone number specified here was invalid!.\n    Please specify a valid phone number and make sure that the country code u provided is corresponded to the phone number.%s\n"%(error,stop))
            os.sys.exit() 
    except Exception as err:
        time.sleep(1)
        slow ("\n%sCould not get the location of this number. Please specify a valid phone number %s\n"%(error,stop))
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
    if internet():
        slow("\n%sPlease check your internet connection%s"%(error,stop))
        os.sys.exit()
    if update:updateus()
    elif str(about).upper() in ["FEONIX","F30N1X"]:aboutus()
    elif number and cncode:infoga(cncode,number)
    else:print(F30N1X())
    #return argument


if __name__ == "__main__":
    main()

