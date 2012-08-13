This project targets to 
- analyze top pinterest users' pin source
- group these users based on frequencies of these pin sources 
- using 
-- k-means clustering:
- represent these data in a visually easy-to-understand manner
-- dendrogram, scaledown (multidimension spatial) representation
- recommend new pin sources to a user by taking in 1 data (username)
- present in clean front end

file organizer
- find_pin.py: a program that takes in username list from toppinners.py and feed into the mongo db
Note: dont really need re-use it unless want to inject more data

- clusters.py: a program that takes in the database and create k-cluster files

- webapp.py: link it with front end. not active at the moment 


last updated: Aug 13, 2012
