from .PopulationBase import PopulationBase

class PopulationAgeRangeBased(PopulationBase):
    def __init__(self, ages, subpopulation_creator, people_creator, *args):
        """Creates a new population based on age range.
        Arguments:
            ages {list} -- Ages descriptions. Each element in this list must be an dict with
                           "description" and "size", when the description is an description
                           for this age range, and the size is the number of people in this
                           age range.
            subpopulation_creator {function} -- An function to create the sub populations for age range.
            people_creator {function} -- An function to create the peoples.
        """
        self.ages = []
        for age_description in ages:
            age_data = {
                "description": age_description["description"],
                "population": subpopulation_creator(people_creator, age_description["size"], *args),
                "size": age_description["size"]
            }
            self.ages.append(age_data)

    def count(self, counter_data, attribute):
        """Perform a count of an attribute in the population.
        Arguments:
            counter_data {any} -- The counter data.
            attribute {soss.attributes.AttributeBase} -- The attribute to count
        """
        for age in self.ages:
            age["population"].count(counter_data, attribute)

    def get_population_size(self):
        """Get the count of peoples in the population.
        Returns:
            int -- Returns the count of peoples in the population.
        """
        num = 0
        for age in self.ages:
            num += age["population"].get_population_size()
        return num

    # TODO: def get_sample(self, size, *args):