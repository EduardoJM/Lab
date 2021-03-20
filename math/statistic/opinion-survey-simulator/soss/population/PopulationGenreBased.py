import math
from .People import GENRE_MALE, GENRE_FEMALE
from .PopulationBase import PopulationBase

class PopulationGenreBased(PopulationBase):
    def __init__(self, size, male_proportion, subpopulation_creator, people_creator, *args):
        """Creates a new population based on the genre.
        Arguments:
            size {int} -- The size of the population.
            male_proportion {float} -- The proportion of male peoples in the population.
            subpopulation_creator {function} -- The subpopulation for genre creator.
            people_creator {function} -- The people creator.
        Raises:
            ValueError: Raised when male_proportion is not an valid value between 0 and 1.
        """
        if male_proportion < 0 or male_proportion > 1:
            raise ValueError("Proportion must be a value between 0 and 1.")
        self.size = size
        self.male_proportion = male_proportion
        self.size_male = math.ceil(self.size * male_proportion)
        self.size_female = self.size - self.size_male
        self.males = subpopulation_creator(people_creator, self.size_male, GENRE_MALE, *args)
        self.females = subpopulation_creator(people_creator, self.size_female, GENRE_FEMALE, *args)

    def count(self, counter_data, attribute):
        """Perform a count of an attribute in the population.
        Arguments:
            counter_data {any} -- The counter data.
            attribute {soss.attributes.AttributeBase} -- The attribute to count
        """
        self.males.count(counter_data, attribute)
        self.females.count(counter_data, attribute)

    def get_population_size(self):
        """Get the count of peoples in the population.
        Returns:
            int -- Returns the count of peoples in the population.
        """
        return self.males.get_population_size() + self.females.get_population_size()

    # TODO: def get_sample(self, size, *args):