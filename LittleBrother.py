#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style
from lib.menu import checkVersion, clear, menu
from lib.loading import thread_loading
from core.searchEmail import SearchEmail
from core.searchPersonne import searchPersonne
from core.searchAdresse import searchAdresse
from core.searchUserName import searchUserName
from core.ipFinder import ipFinder
from core.bssidFinder import bssidFinder
from core.mailToIP import mailToIP
from core.employee_lookup import employee_lookup
from core.google import google
from core.facebookStalk import facebookStalk
from core.searchTwitter import searchTwitter
from core.searchInstagram import searchInstagram

from txt.help import helpLookup
import settings

init()

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"


checkVersion()
thread_loading()



mainOption = """
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Change country

 [e] Exit script    [h] Help Message    [c] Clear Screen"""


lookupOption = """
 [1] Personne lookup          [8] Mail tracer
 [2] Username lookup          [9] Employés recherche
 [3] Adresse lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearch
 [5] IP lookup                [12] twitter info
 [6] SSID locator             [13] instagram info
 [7] Email lookup

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen"""

otherToolOption = """
 [1] Hash decrypter

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen
"""

profilerOption = """
 [1] Profiler
 [2] Show all Profiles
 [3] Create profile

 [b] back main menu    [c] Clear screen   [h] Help message
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg)
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)

 [b] back main menu   [c] Clear screen   [h] Help message
"""

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n LittleBrother("+Fore.BLUE + "~" + Fore.RESET + ")$ ")

		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = settings.Profiler()
				pr.loadDatabase(settings.pathDatabase)
				database = pr.database

				choix = input("\n LittleBrother("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

				if choix.lower() == 'h':
					print(helpProfiler)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e':
					sys.exit("\n"+information+" Bye ! :)")
				elif choix.lower() == "1":
					profile = input(" Profil: ")
					data = pr.searchDatabase(profile, database=database)
					profilerFunc(data, path=settings.pathDatabase)

				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: Prenom Nom)"+Fore.RESET)
					name = input(" Nom du Profil: ")
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					twitter = input(" Twitter: ")
					# print(found+" %s" % (twitter))
					instagram = input(" Instagram: ")
					# print(found+" %s" % (instagram))
					facebook = input(" Facebook: ")
					# print(found+" %s" % (facebook))

					info = {"URL": {"Twitter": twitter, "Facebook":facebook, "Instagram": instagram}}
					create = pr.writeProfile(fileName=name, path=settings.pathDatabase, info=info)

					if create:
						print("\n"+found+" Le profil '%s' a été créé avec succès." % (name))
					else:
						print("\n"+warning+" Une erreur est survenue. Le profil '%s' n'a pas pu être créé." % (name))

		elif choix.lower() == 'e':
			sys.exit("\n"+information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n LittleBrother("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '4':
					searchNumber(codemonpays)
				elif lookup.lower() == '7':
					SearchEmail()
				#  ...
				elif lookup.lower() == '3':
					searchAdresse(codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Commande introuvable")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n LittleBrother("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n LittleBrother("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					codemonpays = "FR"
					monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					codemonpays = "BE"
					monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					codemonpays = "CH"
					monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					codemonpays = "LU"
					monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					codemonpays = "XX"
					monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMsg)
		else:
			pass
			# print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")
