from RouteManager import RouteManager
from Route import Route

import numpy as np


class GeneticAlgorithmSolver:
    def __init__(self, cities, population_size=20, mutation_rate=0.05, tournament_size=5, elitism=True):
        self.cities = cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elitism = elitism

    def solve(self, rm):
        rm = self.evolve(rm)
        for i in range(100):
            rm = self.evolve(rm)
        return rm

    def evolve(self, routes):
        # YOUR CODE HERE
        new_routes = RouteManager(self.cities, self.population_size)
        # fitness_values_for_each_route = {}
        # for i in routes.routes:
        #     fitness_values_for_each_route[i.__str__()] = i.calc_fitness()
        if not self.elitism:
            for i in range(0, new_routes.population_size):
                chosen1 = self.tournament(routes)
                chosen2 = self.tournament(routes)
                new_routes.set_route(i, self.crossover(chosen1, chosen2))

            for i in new_routes.routes:
                self.mutate(i)
        else:
            new_routes.set_route(0, routes.find_best_route()) # added the best path at the begining of the because of the elitism
            for i in range(1, new_routes.population_size):   # for loop starts from 1 in order to keep the fittest route
                chosen1 = self.tournament(routes)
                chosen2 = self.tournament(routes)
                new_routes.set_route(i, self.crossover(chosen1, chosen2))

            for i in new_routes.routes[1:]:  # in order to keep fittest route we dont change it by mutation
                self.mutate(i)

        return new_routes

    def crossover(self, route_1, route_2):
        # YOUR CODE HERE
        result = Route(self.cities)
        start_pos = np.random.randint(route_1.__len__())
        end_pos = np.random.randint(route_2.__len__())

        start = min(start_pos, end_pos)
        end = max(start_pos, end_pos)

        for i in range(start, end):
            result.assign_city(i, route_1.get_city(i))
        for i in range(route_2.__len__()):
            if not result.__contains__(route_2.get_city(i)):
                stop = True
                x = 0
                while x < result.__len__() and stop is not False:
                    if not result.get_city(x):
                        result.assign_city(x, route_2.get_city(i))
                        stop = False
                    x += 1
        return result

    def mutate(self, route):
        # YOUR CODE HERE
        for i in range(route.__len__()):
            if np.random.sample() < self.mutation_rate:
                random_location = np.random.randint(route.__len__())

                temp_city = route.get_city(i)
                temp_city2 = route.get_city(random_location)

                route.assign_city(random_location, temp_city)
                route.assign_city(i, temp_city2)

    def tournament(self, routes):
        # YOUR CODE HERE
        tournament_routes = RouteManager(self.cities, self.tournament_size)
        count = 0
        for i in np.random.randint(0, routes.population_size,size=self.tournament_size):
            tournament_routes.set_route(count, routes.get_route(i))
            count += 1
        return tournament_routes.find_best_route()
