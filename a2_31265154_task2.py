from a2_31265154_task1 import *
import random
"""
Topic:              Assignment 2 - Simulating disease spread
Task number:        2
Author:             Vivekkumar Vitthalbhai Chaudhari
Student ID:         31265154
Task Description:   Creating Patient class objects from a file with basic required properties(including health points) 
                    and add a social connection to his friends(also a Patient objects). Simulate with number of days to finds out virus spread. 
"""


class Patient(Person):
    """
    This class represents a blueprint of a Patient object, It inherits from Person class.
    :param first_name: first name of a person object as a type of string
    :param last_name: last name of a person object as a type of string
    :param health: initial health value of a patient object as a type of float
    """
    def __init__(self, first_name: str, last_name: str, health: float):
        self.health = health
        Person.__init__(self, first_name, last_name)

    def get_health(self):
        """
        Returns current health of a patient.
        :return: Type of float value that indicate health points
        """
        return self.health

    def set_health(self, new_health: float):
        """
        Set health of a patient with given 'new_health' value.
        Parameters
        ----------
        new_health: float
            Type of float value
        """
        self.health = 0 if new_health <= 0 else 100 if new_health >= 100 else new_health

    def is_contagious(self):
        """
        Checks that this patient is contagious or not based on his health.
        :return: True if contagious else False
        """
        return True if 0 <= round(self.health) <= 49 else False

    def infect(self, viral_load: float):
        """
        Infect this patient with a given 'viral_load' value and update his health
        :param viral_load: Type of float value
        :return: None
        """
        if 0 <= self.get_health() <= 29:
            self.set_health(self.get_health() - (0.1 * viral_load))
        elif 29 < self.get_health() < 50:
            self.set_health(self.get_health() - (1 * viral_load))
        else:
            self.set_health(self.get_health() - (2 * viral_load))

    def sleep(self):
        """
        Indicate patient go for a sleep and update his health value
        :return: None
        """
        self.set_health(self.get_health() + 5)

    def get_viral_load(self):
        """
        Calculate viral load value based on current health value of a patient
        :return: Type of float value indicate viral load from this patient emits in the air
        """
        return 5 + (((self.get_health() - 25) ** 2) / 62)

    def meet(self, other_patient):
        """
        Define meeting between two person("self" and "other_patient").
        :param other_patient: Reference to second patient object of type Patient
        """
        # Get viral load of two person("self" as person-A and "other_patient" as person-B) if they are contagious before they meet
        a_viral_load = self.get_viral_load() if self.is_contagious() else 0
        b_viral_load = other_patient.get_viral_load() if other_patient.is_contagious() else 0
        # If "self" is contagious then he/she infect "other_patient" with his viral load.
        if a_viral_load > 0:
            other_patient.infect(a_viral_load)
        # If "other_patient" is also contagious before this meeting then he/she infect "self" with his viral load.
        if b_viral_load > 0:
            self.infect(b_viral_load)


def run_simulation(days: int, meeting_probability: float, patient_zero_health: float):
    """
    Load patients from a file with default health values of 75.
    Then set the patient zero's heath value from a given 'patient_zero_health'
    Run simulation for a given no of 'days'.
    Each day calculate meeting probability between two people using a given 'meeting_probability'
    After end of the day check for contagious patients and put every patient to sleep.
    :param days: Type of integer value indicates simulation to be run for number of days
    :param meeting_probability: Type of fraction number between 0 to 1.0 indicates meeting probability between two people
    :param patient_zero_health: Type of integer or float value indicates first patient health value
    :return: A list of number of people contagious in each day
    """
    if days < 1:
        return
    assert 0.0 <= meeting_probability <= 1.0, "Meeting probability must be fraction number between 0 to 1 inclusive."
    assert 0 <= patient_zero_health <= 100, "Patient zero's health must be between 0 to 100 inclusive."
    # load patients from file and assign average health values to each.
    patients = load_patients(75)
    assert len(patients) > 0, "No patients found from input!!"
    # set patient zero's health value provided in the argument
    patients[0].set_health(patient_zero_health)
    infect_list = []
    # loop through no of days provided in the argument
    for day in range(days):
        count = 0
        # loop through all patients loaded from file to calculate meeting and its outcome between patient and his friends
        for patient in patients:
            # loop through all friends of a patient
            for friend in patient.get_friends():
                # Calculate meeting outcome at every meeting between a patient and his friend.
                if True if round(random.random(), 2) <= meeting_probability and meeting_probability > 0 else False:
                    patient.meet(friend)
        # loop through all patients loaded from file to calculate no of contagious people in a day
        for patient in patients:
            count += (1 if patient.is_contagious() else 0)
            patient.sleep()
        infect_list.append(count)
    return infect_list


def load_patients(initial_health: float):
    """
    This method load patient information from a file and
    create Patient's objects(inherited from Person object) with relations with his friends that is also a Patient objects.
    :return: A list of Patient objects
    """
    try:
        patient_file = open("a2_sample_set.txt", "r", buffering=1024, encoding="utf-8")
        # read file at once.
        patient_text = str(patient_file.read().strip())
        patient_file.close()
        # key: patient's name, value: patient object and his friend names as a tuple.
        patients = dict()
        for line in patient_text.split("\n"):
            name = line.strip().split(": ")[0].strip()
            # create patient object with initial health value.
            patient = Patient(name.split(" ")[0], name.split(" ")[1], initial_health)
            patients[patient.get_name()] = (patient, line.strip().split(": ")[1].split(", "))

        for key, val in patients.items():
            for friend_name in val[1]:
                friend = patients.get(friend_name)
                # add friend to person.
                val[0].add_friend(friend[0])
        # return list of patient objects from dictionary.
        return [item[0] for item in patients.values()]
    except IOError:
        print("Error: cannot find file or read data")


if __name__ == '__main__':
    print(run_simulation(4, 0.1, 25))
    test_result = run_simulation(15, 0, 49)
    print(test_result)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    print(run_simulation(50, 0, 0))
