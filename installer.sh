#!/usr/bin/env bash

# Versoin: 1.2
# Author: evilfeonix
# Date: 28 - DECEMBER - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 
# Name: Geo-Phone Setup Wizerd


S="\e[0m"
R="\e[91m"
G="\e[92m"
B="\e[94m"
P="\e[95m"
Y="\e[43m"


ERR="$P[$S-$P]$R "
INFO="$P[$S+$P]$G "

LIB=("urllib2"
	 "requests"
	 "opencage"
	 "countryinfo" 
	 "phonenumbers")

function slow()
{
    local F3="$1"
    local color="$2"  # Optional color argument (default: no color)

    # Print the color code if provided
    if [[ -n "$color" ]]; then
        echo -ne "$color"
    fi

    # Print each character with a slight delay
    for (( i=0; i<${#F3}; i++ )); do
        echo -n "${F3:$i:1}"
        sleep 0.003  # Delay between characters
    done

    # Reset formatting
    if [[ -n "$color" ]]; then
        echo -ne "$S"  # Reset color
    fi
    echo
}

function load()
{
	local F3="$1"
	local color="$2"
	
	if [[ -n "$color" ]]; then
        echo -ne "$color" 
    fi
    
    for (( i=0; i<${#F3}; i++ ))
	do
        echo -n -e "${F3:$i:1}"
        sleep 0.003  # Delay between characters
    done
	dot=(. . .)
	for i in "${dot[@]}"
	do
		echo -n $i
		sleep $((1))
	done
	
	if [[ -n "$color" ]]; then
        echo -ne "$S"  # Reset color
    fi
	echo
}

function banner()
{
    clear || cls
    local Ban="
_________               ______________          v2.0.3
__/ ____/__________     ___/ __ \__/ /___________________ 
_/ / __ _/ _ \  __ \______/ /_/ /_/ __ \  __ \\\  __ \  _ \\
/ /_/ / /  __/ /_/ /_____/  ___/_/ / / / /_/ // / / /  __/
\____/  \___/\____/     /_/     /_/ /_/\____//_/ /_/\___/ 
	"
	slow "$Ban" "$P"
}

function installed()
{
	redirection
}

function internet()
{
	wget http://google.com > /dev/null 2>&1
}

function setupEnv()
{
    load " Setting Up Your Environment" "$INFO"

    for i in "${LIB[@]}"
	do
		pip install $i
	done

	slow " Installation Successfully Finished." "$INFO"
	slow " Press [ENTER] To Continue" "$INFO"
	read act;load " Loading, Please Wait!" "$INFO"
}

function F30N1X()
{
	local USAGE="
Usage: python3 phone.py [OPTION...]
------------
      | OPTIONS
      |----------
            | -u <Script Updating>       | Update Geo-Phone Script for Better performance
            | -a <About Tool & Author>   | About Tool and Author's Contact Information
            | -c <Victim's Country Code> | Specify Victim's Country Code Without \"+\" .eg 234
            | -p <Victim's Phone Number> | Specify Victim's Phone Number'
      | EXAMPLES
      |----------
            | python3 phone.py -u                   | Script Updating
            | python3 phone.py -a F30N1X            | About Tool & Author
            | python3 phone.py -c 234 -p 7000000000 | Specify victim's Country Code & Phone Number         
    "
    echo "$USAGE"
	exit
}

function redirection()
{
	setupEnv
}

function main()
{
	banner
	internet
	if [[ $? != 0  ]]; then 
	# if [[ $? == 0  ]]; then 
		slow " Status: Offline." "$INFO"
		load " Please Check Your Internet Connection" "$ERR"
		slow ' '
		exit 
	fi
	slow " Status: Online." "$INFO"
	installed

    clear || cls
 	F30N1X
	exit
}


main


