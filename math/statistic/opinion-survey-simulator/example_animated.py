# Import used modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import ImageMagickWriter
from soss.attributes import VoteGeneratorRule
from soss.population import PopulationAgeRangeGenreBased
from soss.confianceinterval import ProportionConservator, ProportionOptimist

# creates a new vote generator rule for a seven candidates election
vote_generator = VoteGeneratorRule([0.2992, 0.2156, 0.1526, 0.1303, 0.1097, 0.0799, 0.0127])
# creates a population description divided by age and genre
#
# observation: this data is based on Anápolis city in Goiás state
#              at Brazil and is get from IBGE 2010 census.
pop = PopulationAgeRangeGenreBased([
    {
        "description": "16 a 24",
        "size_male": 27196,
        "size_female": 26914
    },
    {
        "description": "25 a 34",
        "size_male": 28400,
        "size_female": 29417
    },
    {
        "description": "35 a 44",
        "size_male": 24142,
        "size_female": 26513
    },
    {
        "description": "45 a 59",
        "size_male": 25570,
        "size_female": 28788
    },
    {
        "description": "60+",
        "size_male": 14689,
        "size_female": 18573
    }
])
# create a counter data for census
data_census = vote_generator.create_counter_data()
# make an census for population
pop.count(data_census, vote_generator)
# convert the data to the proportion
vote_generator.counter_data_to_proportion(data_census)

# define the number of survey interations
num_interacoes = 0

# create a subplot
fig, ax = plt.subplots()
# create the x interval for seven candidates
x = range(0, len(data_census))
# create a initial y interval, used only for better figure limits
y_initial = []
for i in range(0, len(x)):
    if i % 2 == 0:
        y_initial.append(0)
    else:
        y_initial.append(0.5)
# create the plot data and labels
ax.plot(x, data_census, linewidth=1, color="blue", label="Votação com a população total")
line, = ax.plot(x, y_initial, linewidth=1, color="green", label="Pesquisa com 2.401 pessoas")
line_top_error, = ax.plot(x, y_initial, linewidth=1, color="red", label="Margem de erro")
line_bottom_error, = ax.plot(x, y_initial, linewidth=1, color="red")
# x tick labels
xlabels = []
for i in range(0, len(x)):
    xlabels.append(f"Candidato {i + 1}")
ax.set_xticks(x)
ax.set_xticklabels(xlabels, rotation=20, ha='right')
# change y ticks to percent notation
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
# set title
ax.set_title("Simulação de eleições e pesquisas eleitorais\n com confiabilidade de 95% e erro percentual\n de 2 pontos para mais ou para menos", wrap=True, pad=10)
ax.legend()
# set the x label
ax.set_xlabel("Pesquisa 0", labelpad=20)
# create the max error notation
error_text = ax.annotate("Erro Máximo: ", xy=(0, 0))
# adjust the layout 
fig.tight_layout()

# this function create a new sample 
# and make a statistical opinion survey
# for this sample
def new_sampling():
    # get a sample in population with 2401 peoples
    sample = pop.get_sample(2401)
    # create counter data
    data_sample = vote_generator.create_counter_data()
    # make the count in the sample
    sample.count(data_sample, vote_generator)
    # convert the data for the proportion
    vote_generator.counter_data_to_proportion(data_sample)
    # create a new confiance interval
    ic1 = ProportionConservator()
    e = ic1.get_error_to(sample, 0.95)
    # create a lower and upper error line data
    data_upper = []
    data_lower = []
    for i in data_sample:
        data_lower.append(i - e)
        data_upper.append(i + e)

    # TODO: implements this as confiance interval methods
    def largest_error(a, b):
        if len(a) != len(b):
            raise AssertionError("lists must be same size")
        max_error = 0
        for i in range(0, len(a)):
            error = abs(a[i] - b[i])
            if error > max_error:
                max_error = error
        return max_error
    # return created sample information
    return data_sample, data_upper, data_lower, largest_error(data_sample, data_census)

# initialize data
def init(): 
    sample, upper, lower, _ = new_sampling()
    line_top_error.set_ydata(upper)
    line_bottom_error.set_ydata(lower)
    line.set_ydata(sample)
    return line,

# animation frame 
def animate(i):
    # change the number of interations
    global num_interacoes
    print(num_interacoes)
    num_interacoes += 1
    # set the x label
    ax.set_xlabel(f"Pesquisa {num_interacoes}", labelpad=20)
    # get sample data
    sample, upper, lower, max_error = new_sampling()
    # set the error label
    error_text.set_text("Erro Máximo: {:,.2%}".format(max_error))
    # adjust the lines
    line_top_error.set_ydata(upper)
    line_bottom_error.set_ydata(lower)
    line.set_ydata(sample)
    # adjust the layout
    fig.tight_layout()
    return line, ax

# set the function animation
ani = animation.FuncAnimation(fig, animate, init_func=init, interval=200, blit=False, save_count=200)
# create animation writer to gif
writer = ImageMagickWriter(fps=4, metadata=dict(artist='Me'), bitrate=1800)
# save the animation as gif
ani.save("movie.gif", writer=writer)