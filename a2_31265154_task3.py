import matplotlib.pyplot as plt
from a2_31265154_task2 import *
"""
Topic:              Assignment 2 - Simulating disease spread
Task number:        3
Author:             Vivekkumar Vitthalbhai Chaudhari
Student ID:         31265154
Task Description:   Visualize virus spread over days through 2D plot graph.
Scenario A:         
    Input:          Days = 30, Meeting probability = 60% and Patient zero health points = 25
    Prediction:     The situation might get out of control very quickly.
    Outcome:        Prediction matched and virus spread out very quickly due to high gatherings and patient zero is quite unwell.
Scenario B:         
    Input:          Days = 60, Meeting probability = 25% and Patient zero health points = 49
    Prediction:     Sometime there is no outbreak but in unlucky situation virus begin to spread.
    Outcome:        Even though social distancing, virus begin to spread slowly at start and then speed up after few days. There is an outbreak. 
Scenario C:         
    Input:          Days = 90, Meeting probability = 18% and Patient zero health points = 40
    Prediction:     Due to social distancing restrictions on meetings, it is more likely that virus die out very quickly.
    Outcome:        Due to the limitation on gatherings virus die out quickly even though patient zero is contagious.
"""


def visual_curve(days: int, meeting_probability: float, patient_zero_health: float):
    """
    Plot the 2D curve using the values from the simulation showing Days vs number of contagious people.
    :param days: Type of integer value indicates simulation to be run for number of days
    :param meeting_probability: Type of fraction number between 0 to 1.0 indicates meeting probability between two people
    :param patient_zero_health: Type of integer or float value indicates first patient health value
    :return: None
    """
    if days < 1:
        return
    spread_list = run_simulation(days, meeting_probability, patient_zero_health)
    figure, axis = plt.subplots()
    axis.plot([n for n in range(days)], spread_list)
    axis.set_xlabel('Days')
    axis.set_ylabel('Count')
    plt.suptitle(f"Days vs number of contagious people\n Meeting prob: {meeting_probability * 100}%, Patient zero HP: {patient_zero_health * 1.0}")
    plt.show()


if __name__ == '__main__':
    print("Simulate disease spread over days")
    no_of_days = int(input("Enter number of days (> 0):"))
    meet_probability = float(input("Enter meeting probability (0 to 1.0):"))
    patient_zero_hp = float(input("Enter patient zero health (0 to 100.0):"))
    visual_curve(days=no_of_days, meeting_probability=meet_probability, patient_zero_health=patient_zero_hp)
