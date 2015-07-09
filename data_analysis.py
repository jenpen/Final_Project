# Open the files you want to read
# Parse each line of the file.
# "5530,Hanna Onjea,hanna.onjea@gmail.com,5647,6/19/15,6/23/15"
# [5530,"Hanna Onjea","hanna.onjea@gmail.com",5647,"6/19/15","6/23/15"]


my_file = open ("info_session.csv")
info_session = my_file.read()
info_session = info_session.split('\r')
my_file.close()

registrants = {}
for line in info_session:
	person = line.split (",")
	registrants[person[4]] = {"first_name":person[2], "last_name":person[3],"attendee_status":person[6],"registered_date":person[1]}


my_file = open ("submitted.csv")
submitted_applications = my_file.read()
submitted_applications = submitted_applications.split('\r')
my_file.close()


applicants ={}
for line in submitted_applications:
	person = line.split (",")
	applicants[person[2]] = {"name":person[1],"submitted_date":[4]}

registered_and_submitted = []
for line in applicants:
	if line in registrants:
		registered_and_submitted.append(line)

attend_info_session =[]
for line in registrants:
	if registrants[line]["attendee_status"] == "Checked In" and line in applicants:
		attend_info_session.append(line)

checked_in =[]
for line in registrants:
	if registrants[line]["attendee_status"] == "Checked In":
		checked_in.append(line)
	

print "Percentage of Info Session RSVPs that submitted applications: ", float(len(registered_and_submitted))/len(registrants)
print "Percentage of total submitted applications that RSVPd: ", float(len(registered_and_submitted))/len(applicants)

print "Percentage of Info Session Checked In that submitted applications: ", float(len(attend_info_session))/len(registrants)
print "Percentage of total submitted applications that RSVPd: ", float(len(attend_info_session))/len(applicants)

print "Percentage of Info Session Checked In that submitted applications: ", float(len(attend_info_session))/len(registrants)
print "Percentage of total submitted applications that RSVPd: ", float(len(attend_info_session))/len(checked_in)

#do i have to erase duplicates? how has this changed over time?