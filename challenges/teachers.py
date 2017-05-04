def num_teachers(dictionary):
	count = 0

	for teacher in dictionary.keys():
		count += 1

	return count


def num_courses(dictionary):
	count = 0

	for key in dictionary.values():
		count += len(key)

	return count


def courses(dictionary):
	new_list = []

	for key in dictionary.values():
		for item in key:
			new_list.append(item)

	return new_list
		

def most_courses(dictionary):
	max_count = 0
	name = None

	for key, value in dictionary.items():
		courses = len(value)

		if courses > max_count:
			max_count = courses
			name = key
			
	return name
		


def stats(dictionary):
	new_list = []

	for key, value in dictionary.items():
		courses = [key, int(len(value))]
		new_list.append(courses)

	return new_list

		

num_teachers({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})

num_courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})

courses({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})

most_courses({'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
        'Kenneth Love': ['Python Basics', 'Python Collections']})

stats({'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
        'Kenneth Love': ['Python Basics', 'Python Collections']})