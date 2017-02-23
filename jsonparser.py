import urllib2
import simplejson
import math
import time

#these are to be taken from frontend
name = str(raw_input("Enter search term: "))
name = name.replace(" ", "+")
year = ""
year = str(raw_input("Enter year or press enter to leave blank: "))

#start time of program (for code profiling)
start = int(round(time.time() * 1000))

#Old Algorithm - json request to get total number of movies
#url = "http://www.omdbapi.com/?s=" + name + "&type=movie&y=" + year + "&r=json"
#r = requests.get(url)
#res = r.json()

#New algorithm - Using urllib2 and simplejson
url = "http://www.omdbapi.com/?s=" + name + "&type=movie&y=" + year + "&r=json"

#Debug End-Point
#print url

response = urllib2.urlopen(url)
res = simplejson.load(response)

#these are temporary lists to store the data before beign sorted
yearlist = []
namelist = []
imdblist = []

#conditions to see result
#to check if any movie is found or not
if res["Response"] == 'False':
    print res["Error"]

#main algorithm to find movies and display
elif res["Response"] == 'True':

    #getting total number of pages and preparing for frontend displaying
    TotalResults = int(res["totalResults"])
    NumberOfPages = int(math.ceil(float(TotalResults) / 10))
    pagenum = 0
    #temporary variable to display page number in terminal
    page = 0
    count = 1

    #runs tills all the results are parsed or displayed
    while (pagenum != NumberOfPages):
        page = page + 1
        # displaying page number and index number of the movies
        if (pagenum + 2 == NumberOfPages) or (pagenum + 1 == NumberOfPages):
            #last few movies in the form 20(n-1)+1 to total number of results
            print
            print "Page " + str(page) + " - Displaying " + str((20 * (page - 1)) + 1) + "-" + str(TotalResults) + " of " + str(TotalResults)
            print
        else:
            #general display in the form 20(n-1)+1 to 20(n)
            print
            print "Page " + str(page) + " - Displaying " + str((20 * (page - 1)) + 1) + "-" + str(20 * page) + " of " + str(TotalResults)
            print
        #first thread to parse 10 movies from odd numbered json requests
        pagenum = pagenum + 1

        #New Algorithm - using urllib2 and simplejson
        url1 = "http://www.omdbapi.com/?s=" + name + "&type=movie&y=" + year + "&r=json&page=" + str(pagenum)
        response1 = urllib2.urlopen(url1)
        json1 = simplejson.load(response1)

        #Old Algorithm
        #url1 = "http://www.omdbapi.com/?s=" + name + "&type=movie&y=" + year + "&r=json&page=" + str(pagenum)
        #r1 = requests.get(url1)
        #json1 = r1.json()

        #second thread to double speed to display 20 items at once and even numbered json requests
        if pagenum != NumberOfPages:
            pagenum = pagenum + 1

            #New Algorithm - using urllib2 and simplejson
            url2 = "http://www.omdbapi.com/?s=" + name + "&type=movie&y=" + year + "&r=json&page=" + str(pagenum)
            response2 = urllib2.urlopen(url2)
            json2 = simplejson.load(response2)

            #Old Algorithm - using requests
            #url2 = "http://www.omdbapi.com/?s=" + name + "&type=movie&y=" + year + "&r=json&page=" + str(pagenum)
            #r2 = requests.get(url2)
            #json2 = r2.json()

            #appending to respective lists and printing to make the screen move
            for index in range (0, len(json2["Search"])):
                print json2["Search"][index]["Title"] + " (" + json2["Search"][index]["Year"] + ") - " + json2["Search"][index]["imdbID"]
                yearlist.append(json2["Search"][index]["Year"])
                namelist.append(json2["Search"][index]["Title"])
                imdblist.append(json2["Search"][index]["imdbID"])

        #appending to respective lists and printing to make the screen move
        for index in range (0, len(json1["Search"])):
            print json1["Search"][index]["Title"] + " (" + json1["Search"][index]["Year"] + ") - " + json1["Search"][index]["imdbID"]
            yearlist.append(json1["Search"][index]["Year"])
            namelist.append(json1["Search"][index]["Title"])
            imdblist.append(json1["Search"][index]["imdbID"])

    #sorting w.r.t year of release
    complist = zip(yearlist, namelist, imdblist)
    #comment this part for ascending order
    sortedlist = sorted(complist, reverse = True)

    #ascending order- uncomment to implement
    #sortedlist = sorted(complist)

    #placing values in different lists
    yearsorted = [x[0] for x in sortedlist]
    namesorted = [x[1] for x in sortedlist]
    imdbsorted = [x[2] for x in sortedlist]

    #This part is for printing the list sorted in descending order
    print
    print "Newest First"
    print
    for i in range(0, len(yearsorted)):
        print imdbsorted[i] + " - " + namesorted[i] + " (" + yearsorted[i] + ")"
    print

#exception handling
else:
    print "Unknown error"

#end time of program (for code profiling)
end = int(round(time.time() * 1000))

#total absolute runtime analysis
runtime = end - start
milliseconds = runtime
seconds = milliseconds / 1000
if seconds > 0:
    milliseconds = runtime % 1000
minutes = seconds / 60
if minutes > 0:
    seconds = seconds % 60
print "Program ran in " + str(minutes) + " minutes " + str(seconds) + " seconds and " + str(milliseconds) + " milliseconds."
