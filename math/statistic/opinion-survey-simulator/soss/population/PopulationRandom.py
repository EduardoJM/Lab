import random
from .PopulationBase import PopulationBase
from ..sample import PopulationSample

class PopulationRandom(PopulationBase):
    def __init__(self, size, people_creator, *args):
        """Create a new random population.
        Arguments:
            size {int} -- The size of the population.
            people_creator {function} -- Function to create peoples. The *args was send to
                                         the people_creator function
        """
        self.size = size
        self.peoples = []
        for _ in range(0, self.size):
            self.peoples.append(people_creator(*args))
            
    def count(self, counter_data, attribute):
        """Perform a count of an attribute in the population.
        Arguments:
            counter_data {any} -- The counter data.
            attribute {soss.attributes.AttributeBase} -- The attribute to count.
        """
        for people in self.peoples:
            attribute.count_to(counter_data, people)

    def get_population_size(self):
        """Get the count of peoples in the population.
        Returns:
            int -- Returns the count of peoples in the population.
        """
        return len(self.peoples)

    def get_sample(self, size, *args):
        """Get an sample in the population.
        Arguments:
            size {int} -- The size of the sample.
        Raises:
            AssertionError: Raised if the sample size is larger than the population size.
        Returns:
            [soss.sample.PopulationSample] -- Returns the sample.
        """
        sample = PopulationSample()
        if size > self.size:
            raise AssertionError("the sample size is larger than the population size")
        computed = []
        for _ in range(0, size):
            num = random.randint(0, self.size - 1)
            while num in computed:
                num = random.randint(0, self.size - 1)
            computed.append(num)
            sample.append(self.peoples[num])
        return sample