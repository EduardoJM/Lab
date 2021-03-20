import math
from .People import People, GENRE_MALE, GENRE_FEMALE
from .PopulationBase import PopulationBase
from .PopulationRandom import PopulationRandom
from ..sample import PopulationSample

class PopulationAgeRangeGenreBased(PopulationBase):
    def __init__(self, age_genre_data):
        """Creates an new population based on age range and genre.
        Arguments:
            age_genre_data {list} -- The age genre data description. Each element in the list is an dict
                                     with the "description", "size_male", "size_female".
        """
        def people_creator(genre, age_range):
            p = People(genre)
            p.age_range = age_range
            return p
        self.ages = []
        for age in age_genre_data:
            age_object = {
                "description": age["description"],
                "size_male": age["size_male"],
                "size_female": age["size_female"],
                "population_male": PopulationRandom(age["size_male"], people_creator, GENRE_MALE, age["description"]),
                "population_female": PopulationRandom(age["size_female"], people_creator, GENRE_FEMALE, age["description"])
            }
            self.ages.append(age_object)
    
    def count(self, counter_data, attribute):
        """Perform a count of an attribute in the population.
        Arguments:
            counter_data {any} -- The counter data.
            attribute {soss.attributes.AttributeBase} -- The attribute to count.
        """
        for age in self.ages:
            age["population_male"].count(counter_data, attribute)
            age["population_female"].count(counter_data, attribute)

    def get_population_size(self):
        """Get the count of peoples in the population.
        Returns:
            int -- Returns the count of peoples in the population.
        """
        num = 0
        for age in self.ages:
            num += age["population_male"].get_population_size()
            num += age["population_female"].get_population_size()
        return num

    def get_sample(self, size, *args):
        """Get an sample in the population.
        Arguments:
            size {int} -- The size of the sample.
        Returns:
            [soss.sample.PopulationSample] -- Returns the sample.
        """
        sample = PopulationSample()
        population_size = self.get_population_size()
        for age in self.ages:
            male_proportion = (age["size_male"] / population_size)
            male_size = round(size * male_proportion)
            female_proportion = (age["size_female"] / population_size)
            female_size = round(size * female_proportion)
            sample_male = age["population_male"].get_sample(male_size)
            sample_female = age["population_female"].get_sample(female_size)
            sample.append_other(sample_male)
            sample.append_other(sample_female)
        return sample