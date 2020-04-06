import utils
import GA

objects, reference = utils.load_data("input.txt")
ga = GA.GeneticAlgorithm(objects, reference)
res = ga.fit(100)

print(res)