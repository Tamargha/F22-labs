import urllib.request   #library for web scraping (getting the source code from the url)

given_url = input() # getting input from the user (the url)

content = urllib.request.urlopen(given_url).read() # store the source code(this is in byte stream) into content variable

content = str(content) # convert the byte stream into string (decoded into utf-8)
content = content[2:-1] # the string had some unneeded prefix and suffix
content = 'dict = ' + content # the given data was actually a nested data structure ( dictionary ), so named it 'dict'



f = open("datastructure.py","w") # creates a new file called datastructure.py on the same directory as this file
f.write(content) # saves the data structure (the dictionary 'dict' ) into the newly created file
f.close()  # closes the file

from datastructure import * # imports the file containing the data structure into this file to be able to access the dictionary

investors_status = {} # a result dictionary to save the final sorted result. 
#this result dictionary will contain index(key) as investor's names and value as the list of companies invested by that investor



for episode,episode_idealist in dict.items(): # iterates over the episodes
	for idea in episode_idealist: # iterates over each individual entrepreneur
		interested_investors = idea["investors"]; # the string containing names of investors separated by 'and' or 'commas'
		if not interested_investors: # if string is empty, continue
			continue
		interested_investors = interested_investors.replace(' and ',',') # replace "and" by comma
 		interested_investors = interested_investors.replace('\\n','') # replace "\\n" by nothing
		interested_investors = interested_investors.replace('\xe2\x80\x99','`')  # a character encoding problem
		interested_investors = interested_investors.replace('` ','`') # this was done because two different names were being generated for the same person(with spaces and without)
		
		company = idea["company"] # get the 3rd nested dictionary inside the provided data structure and store it into company variable
		company_name = company["title"] # access title of the company 
		
		temp_list = interested_investors.split(',') # create a list out of the string of investor names separated by commas
		for investor in temp_list: # iterate over the list created in the above(previous) line
			if not investor: # if no investor present , then continue
				continue
			if investor[0] == ' ': # some names had spaces in front, so to remove the unneeded spaces
				investor = investor[0][1:]
			if investor not in investors_status: # checks if the investor name is present in the "result dictionary" (named as investor_status)
				investors_status[investor] = [] # if an entry not present, then create one empty list against the investor name
			investors_status[investor].append(company_name) # enter the company name into the list against the investor name
		

print("\n\n")

for index,key in enumerate(sorted(investors_status.keys(), key=lambda x :len(investors_status[x]), reverse=True)): # this iterates over the sorted "result dictionary" (named as investors_status) in descending order of list size 
	if not key:
		continue
	print(index+1,".",key , " : ",investors_status[key],"\n\n") # prints out the values
