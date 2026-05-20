# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ____"
youtuber = "CodeWithHarry" #some string variable

#a few ways to do this
print("subscribe to " + youtuber) #old way
print("subscribe to {}".format(youtuber)) #using the format method
print(f"subscribe to {youtuber}") #f-string (python 3.6