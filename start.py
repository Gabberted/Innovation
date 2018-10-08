#!/usr/bin/python

# This program will query the user for the project description
# Filter the vowes, store them online db and exits (for now)
import argparse
import sys
import os
import npyscreen
import pymssql

#from pyautogui import *
from argp import *
from debugFnct import *
from dbConn import *

# For now we don't have any 
# cli input at init
parser=createParser()
parseAction(parser)

def QueryUser(strText):
	print(strText)
	strDescr=input("Input:>_")
	return strDescr.lower()

def storeW(strWord):
	if boWordKnown:
		print("Word already in db")
	else:
		strQ="insert into Nouns(word)values(" + strWord + ")"
		ExecuteQuery(strQ)
		print(strWord + " stored.")



def storeNoun(strWord):
	print("Storing: " + strWord)
	strHost="mysql8.mijnhostingpartner.nl"
	strUser="Autar3Joomla"
	strPwd="ijQ84mTO"
	strDb="autar3newj"

	print("Connect to local db:")
	store(strWord)
	#testConn(strHost,strUser,strPwd,strDb)


def newproject():
	# we start with asking the user for the description
	strDescr=input("Please give a complete description of the project:\n_>")
	debugprint("Input: " + strDescr)

	#we store the project for later usage
	strQ="insert into projects(project)values('" + strDescr + "')"
	ExecuteQuery(strQ)

	# we chop all the words in description in split
	for word in strDescr.split(" "):
		# loop through them
		print("Evaluating: " + word)
		strNoun=input("Is '" + word +  "' a noun? (y/N)\n_>")

		# if the word is noun 
		if strNoun.lower() == "y":
		#	store db
			debugprint("Storing Noun")
			storeW(word.lower())
	# continue loop

def listTable(strTable):
	os.system('clear')
	strQ="Select * from " + strTable
	cur=ReturnCursor(strQ)
	print("\n\n")
	print("Listing " + strTable + ":")
	for row in cur:
		print(str(row[0])+ " : \t" + str(row[1]))
	cur.close()
	strSel=selection("Main")
	return strSel


def openproject(strProjectNr):
	print("opening project: " + strProjectNr)
	#Clear the screen
	os.system('clear')
	#get the information related to this project
	strQ="Select InnovationName,Account,Description,StartDate,EndDate from innovations where ind='" + strProjectNr + "'"
	row=ExecuteQueryRow(strQ)
	print("Project: " + row[0])
	print("Description: " + row[2])
	print("")
	print("Start Date: " + str(row[3]))
	print("End Date: " + str(row[4]))
	print("")
	print("========== EDIT ===========")
	print("Project:1")
	print("Description:2")
	print("End Date:3")

	strSel=selection("OpenProject", strProjectNr)


def editItems(strSection, strProjectNr):
	os.system('clear')
	strQ="Select InnovationName,Account,Description,StartDate,EndDate from innovations where ind='" + strProjectNr + "'"
	row=ExecuteQueryRow(strQ)
	strTable=""
	if strSection=="1":
		print("Project: " + row[0])
		strTable="InnovationName"
	if strSection=="2":
		print("Description: " + row[2])
		strTable="Description"
	if strSection=="3":
		print("End Date: " + str(row[4]))
		strTable="EndDate"

	strNew=input("Input:>_")
	strQ="update innovations set " + strTable + " ='" + strNew + "' where ind='" + strProjectNr + "'"
	ExecuteQuery(strQ)

def insertWord(strTable,strWord):
	debugprint("Entering")
	if boWordKnown(strWord,strTable)==False:
		strQ="insert into " + strTable + "(word)values('" + strWord + "')"
		debugprint(strQ)
		ExecuteQuery(strQ)
	else:
		debugprint("Word Ignored")

def reprocess(strProject):
	print("Reprocessing: " + strProject)
	#open the project
	strQ="Select InnovationName,Account,Description,StartDate,EndDate from innovations where ind='" + strProject + "'"
	row=ExecuteQueryRow(strQ)

	#chop the description into words
	lstWords=row[2].split(" ")
	#eval each word
	print("Please indicate the type of word:")
	print("1 for Noun")
	print("2 for Verb")
	print("3 to ignore the word from now")
	print(" ")
	for word in lstWords:
		#ask user for type of word
		print("What type of word is: " + word)
		strDescr=input("Input:>_").lower()
		#if word is noun save
		if strDescr=="1":
			insertWord("Nouns",word)
		#if word is verb save
		if strDescr=="2":
			insertWord("verbs",word)
		#if word is ignore save
		if strDescr=="3":
			insertWord("ignored",word)
	main()

def selection(strSection, strInd=""):
	strDescr=strSection
	print("")
	debugprint("Mode: " + strSection)
	print("Main Menu:M")
	print("Exit:E")
	print("===========================")
	strDescr=input("Input:>_").lower()
	debugprint("strDescr: " + strSection)

	#if strSection=="Main":
	debugprint("Entering Main")
	if strDescr.lower()=="1":
		iProject=listTable("Innovations")
		openproject(iProject)
	if strDescr.lower()=="2":
		listTable("verbs")
	if strDescr.lower()=="3":
		listTable("Nouns")
	if strDescr.lower()=="4":
		listTable("ignored")
	if strDescr.lower()=="5":
		listTable("ignored")
	if strDescr.lower()=="e":
		return 0
	if strDescr.lower()=="m":
		Main()
	if strSection=="OpenProject":
	#if strDescr=="OpenProject":
		debugprint("Entering OpenProject")
		if strDescr.lower()=="1":
			#edit Project
			editItems("1", strInd)
		if strDescr.lower()=="2":
			#edit description
			editItems("2", strInd)
		if strDescr.lower()=="3":
			#edit End date"
			editItems("3", strInd)
	if strDescr=="5":
		#debugprint("Entering Reprocess")
		iProject=listTable("Innovations")
		reprocess(iProject)


	if strDescr.lower()=="e":
		return 0
	if strDescr.lower()=="m":
		Main()
	return strDescr


def Main():
	os.system('clear')
	print("Start up")
	print("========== MAIN MENU ===========")
	print("List current Projects:1")
	print("List Verbs:2")
	print("List Nouns:3")
	print("List ignored words:4")
	print("Reprocess project:5")
	print("Add new project:6")

	strSel=selection("Main")


Main()


