#!/usr/bin/env bash

# Versoin: 1.1
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


SCRIPT=$0
let TRACKER=0
ERR="$G[$S-$G]$R "
INFO="$R[$S+$R]$G "

LIB=("requests"
	 "opencage"
	 "countryinfo" 
	 "phonenumbers")

function slow() {
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
        echo -ne "$color"  # Reset color
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

function installed()
{
	apt install ruby -y
	gem install lolcat
	apt install figlet -y
	let TRACKER=$TRACKER+1
	
	redirection
}

function internet()
{
	wget -q --spider http://google.com
}

function setupEnv()
{
    clear || cls
	figlet Geo-Phone | lolcat 
	
    load " Setting Up Your Environment" "$INFO"

    for i in "${LIB[@]}"
	do
		pip install $i
	done

    pip install webbrowser

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
	figlet Geo-Phone | lolcat &>> log
	if [[ $? == 0 ]]; then
		setupEnv
	elif [[ $? != 0 ]] && [[ $TRACKER == 2 ]]; then
		setupEnv
	else
		installed
	fi
}

function main()
{
	internet
	if [[ $? != 0  ]]; then 
		slow '\n'
		load " Please Check Your Internet Connection" "$ERR"
		slow '\n'
		exit 
	fi

	installed

    	clear || cls
 	F30N1X
	exit
}


main


