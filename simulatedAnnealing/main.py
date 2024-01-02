# Implementation of the Simulated Annealing Algorithm fo solving the traveling salesman problem

import math
import random


def euclideanDistance(point1: float, point2: float) -> float:
    '''Calculate the euclidean distance between two points'''
    
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def totalDistance(tour, cities):
    '''calculate total distance of a tour'''

    total = 0

    for i in range(len(tour) - 1):
        total += euclideanDistance(cities[tour[i]], cities[tour[i + 1]])
    
    total += euclideanDistance(cities[tour[-1]], cities[tour[0]]) # return to the starting city

    return total

def simulatedAnnealing(cities, initialTemperature = 1000, coolingRate=0.003, numIterations=10000):
    '''Simulated Annealing algorithm'''
    
    
    numCities = len(cities)
    currentTour = random.sample(range(numCities), numCities) # initial random tour
    currentCost = totalDistance(currentTour, cities)
    bestTour = currentTour.copy()
    bestCost = currentCost

    temperature = initialTemperature

    for i in range(numIterations):
        # generate a new tour by swapping two random cities
        newTour = currentTour.copy()
        idx1, idx2 = random.sample(range(numCities), 2)
        newTour[idx1], newTour[idx2] = newTour[idx2], newTour[idx1]

        # calculate the cost of the new tour
        newCost = totalDistance(newTour, cities)

        # decide wether to accept the new tour
        if newCost < currentCost or random.random() < math.exp((currentCost - newCost) / temperature):
            currentTour = newTour
            currentCost = newCost

        # update the best cost if applicable
        if currentCost < bestCost:
            bestTour = currentTour.copy()
            bestCost = currentCost

        # cool down the temperature
        temperature *= 1 - coolingRate

        # print iteration and cost information every 100 itetations
        if i % 100 == 0:
            print(f"Iteration {i}: Best Cost = {bestCost}")

    return bestTour, bestCost

# Example usage

if __name__ == "__main__":
    #Example citie (coordinates)
    cities = [
    (0, 0), (1, 4), (3, 2), (5, 6), (7, 3),
    (2, 8), (9, 5), (4, 7), (6, 1), (8, 9),
    (10, 12), (11, 14), (13, 15), (15, 11), (17, 13),
    (12, 18), (19, 16), (14, 20), (16, 10), (18, 19)
    ]

    bestTour, bestCost = simulatedAnnealing(cities)

    print(f"Best tour: {bestTour}")
    print(f"Best cost: {bestCost}")
