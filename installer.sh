#!/usr/bin/env bash

# Versoin: 1.1
# Author: evilfeonix
# Date: 28 - DECEMBER - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 
# Name: Geo-Trace Setup Wizerd


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

function load()
{
	dot=(. . . '\n')
	for i in "${dot[@]}"
	do
		echo -e -n $i
		sleep $((1))
	done
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
    clear || clr || cls
	figlet Geo-Trace | lolcat || figlet Geo-Trace
    echo -e -n  $INFO "Setting Up Your Environment"$S;load

    for i in "${LIB[@]}"
	do
		pip install $i
	done

    pip install webbrowser

	echo -e  $INFO  "Installation Successfully Finished."
	echo -n -e  $INFO  'Press '$P'['$S'ENTER'$P'] '$G'To Continue'$S
	read act 
	echo -n -e  $INFO  'Loading, Please Wait!'$S
	load
}

function F30N1X()
{
	local USAGE

    USAGE="""
 Useage: python3 phone.py [OPTION...]\n
------------\n
\t | OPTIONS\n
\t |----------\n
\t\t\t| -u <Script Updating>       | Update Geo-Trace Script for Better performance\n
\t\t\t| -a <About Tool & Author>   | About Tool and Author's Contact Information\n
\t\t\t| -c <Victim's Country Code> | Specify Victim's Country Code WithOut "+" .eg 234\n
\t\t\t| -p <Victim's Phone Number> | Specify Victim's Phone Number\n
\t | EXAMPLES\n
\t |----------\n
\t\t\t| python3 phone.py -u                   | Script Updating\n
\t\t\t| python3 phone.py -a F30N1X            | About Tool & Author\n
\t\t\t| python3 phone.py -c 234 -p 7000000000 | Specify victim's Country Code & Phone Number\n   
    """

    clear || clr || cls
    echo -e $USAGE
	exit
}

function redirection()
{
	figlet Geo-Trace | lolcat &>> log
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
		echo -e -n '\n'$ERR'Please Check Your Internet Connection'
		load
		exit 
	fi

	installed

 	F30N1X
	exit
}


main

