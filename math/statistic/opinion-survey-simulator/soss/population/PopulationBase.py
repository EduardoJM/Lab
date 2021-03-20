from abc import ABC, abstractmethod

class PopulationBase(ABC):
    @abstractmethod
    def count(self, counter_data, attribute):
        """(Abstract) Method to be implemented to perform a count of an attribute in the population.
        Arguments:
            counter_data {any} -- The counter data.
            attribute {soss.attributes.AttributeBase} -- The attribute.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def get_population_size(self):
        """(Abstract) Method to be implemented to get the count of peoples in population.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def get_sample(self, size, *args):
        """(Abstract) Method to get an sample in the population.
        Arguments:
            size {int} -- The sample size.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError