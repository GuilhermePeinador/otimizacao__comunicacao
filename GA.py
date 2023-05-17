from propagador import propagador_orbital
from Periodo_Orbital import periodo_orbital
from comunicacao import calculacomunicacao



def Calc_Coefs(k, i, tc):
    df = propagador_orbital(data, 7000.0, 0.002, k, 0.0, 0.0, i, 10, 10, 3.0, 0.1, 0.1, 0.2)
    # (data, semi_eixo, excentricidade, Raan, argumento_perigeu, anomalia_verdadeira, inclinacao, num_orbitas, delt, massa, largura, comprimento, altura)

    df2 = calculacomunicacao(df)
    df2 = df2[0:-1]
    index = df2["Contato"].tolist()

    tempo_comunicacao_simulacao = index.count(1)
    tempo_comunicacao_total = tempo_comunicacao_simulacao * 10

    return


def fitness_func(solution, solution_idx):
    k  = solution[0] #Raan
    i  = solution[1] #Inclinação
    tc = solution[2] #Tempo de comunicação

     = Calc_Coefs(k, i, tc)


    return  # GA maximiza


last_fitness = 0

def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=70,
                       num_parents_mating=30,
                       fitness_func=fitness_func,
                       sol_per_pop=50,
                       num_genes=2,
                       gene_space=[{"low": 0, "high": 0.3}, {"low": 0.05, "high": 2.}],
                       mutation_by_replacement=True,
                       on_generation=on_generation,
                       save_solutions=True)

ga_instance.run()
#ga_instance.plot_fitness()
#ga_instance.plot_genes(graph_type="boxplot")
#ga_instance.plot_genes(graph_type="histogram", solutions='all')

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
