import random


class GeneticAlgorithm:
    def __init__(self, objects, etalon):
        self.objects = objects
        self.population = []
        self.reference = etalon

    def fit(self, max_epoch, min_error=0):
        self.generate_population()
        #self.print_res()

        epoch_count = 0
        error, arg_min = self.population_assessment()

        min = error
        while epoch_count < max_epoch and min_error < error:
            count_best = len(self.population) - 1
            s = self.choose_best(count_best)
            self.population = self.mutate(self.crossingover(s))

            epoch_count += 1
            error, chr = self.population_assessment()

            if error < min:
                min = error
                arg_min = chr

        return arg_min, min

    def generate_population(self):
        random.seed()
        n = len(self.objects)
        chromosomes_count = random.randint(4, 7)

        population = []
        for i in range(chromosomes_count):
            a = random.randint(1, 2 ** n)
            individual = GeneticAlgorithm.bitfield(a)[0:n]
            individual += [0] * (n - len(individual))
            population.append(individual)

        self.population = population

    @staticmethod
    def bitfield(i):
        return [int(digit) for digit in bin(i)[2:]]

    def target_function(self, chromosome):
        error = 0
        for i, gen in enumerate(chromosome):
            if gen == 0:
                continue

            for j, o in enumerate(self.objects[i]):
                error += (abs(o - self.reference[j]))

        return error / 10

    def population_assessment(self):
        target_marks = list(map(self.target_function, self.population))
        m = min(target_marks)
        return m, self.population[target_marks.index(m)]

    def choose_best(self, count_best):
        s = sorted(self.population, key=lambda chromosome: self.target_function(chromosome))
        return s[0:count_best]

    def crossingover(self, population):
        genes_count = len(population[0])
        s0_h1 = population[0][0:genes_count // 2]
        s0_h2 = population[0][genes_count // 2:]

        other = population[1:]
        other_h1 = []
        other_h2 = []

        for i, c in enumerate(other):
            other_h1.append(c[0:len(c) // 2])
            other_h2.append(c[len(c) // 2:])

        res = []
        for i in other_h2:
            new_chromosome = s0_h1 + i
            res.append(new_chromosome)

        for i in other_h1:
            new_chromosome = i + s0_h2
            res.append(new_chromosome)

        if len(res) > len(population) + 1:
            res = res[0: len(population) + 1]

        return res

    def mutate(self, population):
        for i in population:
            j = random.randint(0, len(population[0]) - 1)
            i[j] = 1 if i[j] == 0 else 0
            if 1 not in i:
                i[j] = 1

        return population

    def print_res(self):
        for i in self.population:
            print(i, self.target_function(i))
