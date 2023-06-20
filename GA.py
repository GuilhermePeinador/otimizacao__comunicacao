'''

##          ###    ########   ######
##         ## ##   ##     ## ##    ##
##        ##   ##  ##     ## ##             Federal University de Santa Catarina
##       ##     ## ########   ######        Laboratory of Applications and Research in Space
##       ######### ##   ##         ##       Orbital Mechanics Division
##       ##     ## ##    ##  ##    ##
######## ##     ## ##     ##  ######

Título do Algoritmo: Algoritmo Genético acoplado ao propagador orbital
Autor: Guilherme Peinador Gomes

'''

from propagador import propagador_orbital
from Periodo_Orbital import periodo_orbital
from comunicacao import calculacomunicacao
import pygad
from datetime import datetime

def fitness_func(ga_instance, solution, solution_idx):
    #raan  = solution[0] #Raan
    inc  = solution[0]  #Inclinação
    alt = solution[1]   #SMA

    dt = 10

    input_string = ' 11/10/2022 18:00:00'
    data = datetime.strptime(input_string, " %m/%d/%Y %H:%M:%S")
    df = propagador_orbital(data, alt, 0.002, 0, 0.0, 0.0, 30, 50, dt, 3.0, 0.1, 0.1, 0.2)  # (data, semi_eixo, excentricidade, Raan, argumento_perigeu, anomalia_verdadeira,
                                    # inclinacao, num_orbitas, delt, massa, largura, comprimento, altura)

    from comunicacao import calculacomunicacao
    df2 = calculacomunicacao(df)

    df2 = df2[0:-1]
    index = df2["Contato"].tolist()

    tempo_comunicacao_simulacao = index.count(1)
    tempo_comunicacao_total = tempo_comunicacao_simulacao * dt
    tempo_voo = len(index) * dt

    print("teste ", solution," fitness ", tempo_comunicacao_total/tempo_voo)

    del df

    return  tempo_comunicacao_total/tempo_voo # GA maximiza


last_fitness = 0

def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=5,
                       num_parents_mating=5,
                       fitness_func=fitness_func,
                       sol_per_pop=5,
                       keep_elitism=3,
                       num_genes=1,
                       gene_space=[{"low": 30, "high": 110}],                           #{"low": 0, "high": 360},,{"low":6878, "high": 6978},
                       mutation_type="random",
                       mutation_percent_genes=100,
                       mutation_by_replacement=True,
                       save_solutions=True,
                       on_generation=on_generation)

ga_instance.run()
ga_instance.plot_fitness()
solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

filename = '50 órbitas 30-100, 6878-6978'
ga_instance.save(filename=filename)

ga_instance.plot_genes(plot_type="scatter")
#ga_instance.plot_genes(graph_type="boxplot")
ga_instance.plot_genes(graph_type="histogram")
ga_instance.plot_new_solution_rate(plot_type="scatter")