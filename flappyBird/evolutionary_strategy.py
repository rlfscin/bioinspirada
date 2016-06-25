import mutation
import parent_selection
import recombination
import survivor_selection
import sys
from copy import deepcopy
from individual import Individual
from setup import (CHILDREN_POP_RATIO,
                   MAX_ITERATIONS,
                   MUTATION_FN,
                   NUM_MUTATION_TRIALS,
                   PARENT_SELECTION_FN,
                   POPULATION_SIZE,
                   RECOMBINATION_FN,
                   SURVIVOR_SELECTION_FN)

class Evo_Strategy:
    def __init__(self):
        if NUM_MUTATION_TRIALS < 1:
            raise Exception("NUM_MUTATION_TRIALS must be at elast 1")

        self.mutation = getattr(sys.modules['mutation'], MUTATION_FN)
        self.parent_selection = getattr(sys.modules['parent_selection'], 
                                        PARENT_SELECTION_FN)
        self.recombination = getattr(sys.modules['recombination'], 
                                     RECOMBINATION_FN)
        self.survivor_selection = getattr(sys.modules['survivor_selection'], 
                                          SURVIVOR_SELECTION_FN)

        self.population = self.generate_random_pop(POPULATION_SIZE)
        self.solution = None


    def evolve(self):
        it_num = 0

        while it_num < MAX_ITERATIONS:
            print "Iteration #" + str(it_num) + ":"
            self.iteration()
            it_num += 1

        return self.solution


    def iteration(self):
        children = list()

        while len(children) < CHILDREN_POP_RATIO * POPULATION_SIZE:
            print "   Child #" + str(len(children)+1) + ":"
            # Select parents
            parents = self.parent_selection(self.population)

            # Generate a child
            child = self.recombination(parents[0], parents[1])
            if self.solution is None or child > self.solution:
                self.solution = deepcopy(child)
            
            # Generate NUM_MUTATION_TRIALS mutated versions of the child
            trials = list()
            for i in range(0, NUM_MUTATION_TRIALS):
                print "      Mutation #" + str(i+1)
                trials.append(self.mutation(child))
            
            # Add the most fit mutation to the children list
            best_mutation = max(trials)
            children.append(best_mutation)


        self.population = self.survivor_selection(self.population, children)
        if self.solution is None or self.population[0] > self.solution:
            self.solution = deepcopy(self.population[0])


    def generate_random_pop(self, pop_size):
        return [Individual() for i in range(pop_size)]