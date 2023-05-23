from propagador import propagador_orbital
from Periodo_Orbital import periodo_orbital
from comunicacao import calculacomunicacao
import pygad
from datetime import datetime

'''def Fitness(x):

    Rann = x[0]
    Inclinacao = x[1]
    Elevacao = x[2] + 6378

    dt = 10

    input_string = ' 11/10/2022 18:00:00'
    data = datetime.strptime(input_string, " %m/%d/%Y %H:%M:%S")
    df = propagador_orbital(data, Elevacao, 0.002, Raan, 0.0, 0.0, Inclinacao, NOrb, dt, 3.0, 0.1, 0.1, 0.2) #(data, semi_eixo, excentricidade, Raan, argumento_perigeu, anomalia_verdadeira,
                                                # inclinacao, num_orbitas, delt, massa, largura, comprimento, altura)

    from comunicacao import CalculaComuni
    df2 = CalculaComuni(df)

    df2 = df2[0:-1]
    index = df2["Contato"].tolist()
    Tempo = df2["Tempo"].tolist()

    tempo_comunicacao_simulacao = index.count(1)
    tempo_comunicacao_total = tempo_comunicacao_simulacao*dt
    tempo_voo = len(index)*dt

    return tempo_comunicacao_total/tempo_voo'''

def fitness_func(solution, solution_idx):
    raan  = solution[0] #Raan
    inc  = solution[1]  #Inclinação
    alt = solution[2]   #SMA

    dt = 10

    input_string = ' 11/10/2022 18:00:00'
    data = datetime.strptime(input_string, " %m/%d/%Y %H:%M:%S")
    df = propagador_orbital(data, alt, 0.002, raan, 0.0, 0.0, inc, 10, dt, 3.0, 0.1, 0.1,
                            0.2)  # (data, semi_eixo, excentricidade, Raan, argumento_perigeu, anomalia_verdadeira,
                                    # inclinacao, num_orbitas, delt, massa, largura, comprimento, altura)

    from comunicacao import calculacomunicacao
    df2 = calculacomunicacao(df)

    df2 = df2[0:-1]
    index = df2["Contato"].tolist()

    tempo_comunicacao_simulacao = index.count(1)
    tempo_comunicacao_total = tempo_comunicacao_simulacao * dt
    tempo_voo = len(index) * dt

    return  tempo_comunicacao_total/tempo_voo # GA maximiza


last_fitness = 0

def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1] - last_fitness))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]


ga_instance = pygad.GA(num_generations=5,
                       num_parents_mating=3,
                       fitness_func=fitness_func,
                       sol_per_pop=5,
                       num_genes=3,
                       gene_space=[{"low": 0, "high": 360} , [30, 50, 98] , {"low":6778, "high": 8000}],
                       mutation_percent_genes= 70,
                       mutation_by_replacement=True,
                       on_generation=on_generation )

ga_instance.run()
#ga_instance.plot_fitness()
#ga_instance.plot_genes(graph_type="boxplot")
#ga_instance.plot_genes(graph_type="histogram", solutions='all')

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)

print("Solution", solution)
print(f"Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
