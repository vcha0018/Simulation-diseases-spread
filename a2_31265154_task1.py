"""
Topic:              Assignment 2 - Simulating disease spread
Task number:        1
Author:             Vivekkumar Vitthalbhai Chaudhari
Student ID:         31265154
Task Description:   Creating Person class objects from a file with basic properties and add a social connection to his friends(also a Person objects).
"""


class Person:
    """
    This class represent the blue-print of a Person object,
    with its basic characteristics like first and last name and relation with his friends who also a Person objects
    :param first_name: first name of a person object as a type of string
    :param last_name: last name of a person object as a type of string
    """
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = set()

    def add_friend(self, friend_person):
        """
        This method add a relationship between this Person object with given friend Person object.
        :param friend_person: A friend person object (type of Person)
        :return: None
        """
        if isinstance(friend_person, Person):
            self.friends.add(friend_person)

    def get_name(self):
        """
        This method returns person's full name.
        :return: Person's full name as a string.
        """
        return f"{self.first_name} {self.last_name}"

    def get_friends(self):
        """
        This method returns friends of this person.
        :return: A list of Person objects.
        """
        return list(self.friends)


def load_people():
    """
    This method load person information from a file and
    create Person's objects with relations with his friends that is also a Person objects.
    :return: A list of Person objects
    """
    try:
        person_file = open("a2_sample_set.txt", "r", buffering=1024, encoding="utf-8")
        # read file at once.
        person_text = str(person_file.read()).strip()
        person_file.close()
        # key: person's name, value: person object and his friend names as a tuple.
        person_dict = dict()
        for line in person_text.split("\n"):
            name = line.strip().split(": ")[0].strip()
            # create person object
            person = Person(name.split(" ")[0], name.split(" ")[1])
            person_dict[person.get_name()] = (person, line.strip().split(": ")[1].split(", "))

        for key, val in person_dict.items():
            for friend_name in val[1]:
                friend = person_dict.get(friend_name)
                # add friend to person.
                val[0].add_friend(friend[0])
        # return list of person objects from dictionary.
        return [item[0] for item in person_dict.values()]
    except IOError:
        print("Error: cannot find file or read data")


if __name__ == '__main__':
    people = load_people()
    c = 1
    all_meetings = 0
    for p in people:
        # print(f"{c}: {p.get_name()}  has {len(p.get_friends())} friends")
        c += 1
        all_meetings += len(p.get_friends())
    print(type(people))
    print(len(people))
    print(f"all_meetings:{all_meetings}")
