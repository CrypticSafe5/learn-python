def friend(x):
	friend_list = []
	for person in x:
		if len(person) == 4:
			friend_list.append(x)
	return friend_list
