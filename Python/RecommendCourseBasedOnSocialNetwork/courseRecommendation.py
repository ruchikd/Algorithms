#def getDirectFriendsForUser(user):
#  returns an array
#  e.g. ['friend1', 'friend2']

#def getAttendedCoursesForUser(user):
#  returns an array
#  e.g. ['course1', 'course2']

import collections

def getDirectFriendsForUser(user):
	friendsList = ['f1', 'f2', 'f3', 'f4', 'f2', 'f4']

	return friendsList

def getAttendedCoursesForUser(user):
	return ['c1', 'c2', 'c3']

def removeDups(socialNetwork):
	#uniqueNetwork = list(set(socialNetwork))
	#return uniqueNetwork
	return socialNetwork

def addCourses(myNetwork):
	courses = {}

	for nw in myNetwork:
		attendedCourses = getAttendedCoursesForUser(nw)
		for i in xrange(len(attendedCourses)):
			if attendedCourses[i] in courses:
				priority = courses[attendedCourses[i]]
				courses[attendedCourses[i]] = priority+1
			else:
				courses[attendedCourses[i]] = 1

	print courses

	sortedCourse = sorted(courses, key=lambda key: courses[key])
	return sortedCourse

# Complete the function below.
def getRankedCourses(user):
	network = []
	friendsList = getDirectFriendsForUser(None)

	for friends in friendsList:
		lists = getDirectFriendsForUser(friends)
		network.extend(lists)

	print network

	myNetwork = removeDups(network)

	courses = addCourses(myNetwork)
	print courses

	return courses

def main():
	getRankedCourses(None)

if __name__ == '__main__':
	main()