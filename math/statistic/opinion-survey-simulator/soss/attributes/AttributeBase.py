from abc import ABC, abstractmethod

class AttributeBase(ABC):
    @abstractmethod
    def new(self):
        """(Abstract) Method to be implemented to creates a new attribute.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def apply_to(self, people):
        """(Abstract) Method to be implemented to apply an attribute to a people.
        Arguments:
            people {soss.population.People} -- The people to set the attribute.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def get_from(self, people):
        """(Abstract) Method to be implemented to get attribute from a people.
        Arguments:
            people {soss.population.People} -- The people to get the attribute.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def create_counter_data(self):
        """(Abstract) Method to be implemented to create a new counter data.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def counter_data_to_proportion(self, counter_data):
        """(Abstract) Method to be implemented to convert the counter data to proportion.
        Arguments:
            counter_data {any} -- The counter data to convert.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def count_to(self, counter_data, people):
        """(Abstract) Method to be implemented to get the attribute from a people and 
        increment this in the counter data.
        Arguments:
            counter_data {any} -- The counter data to increment.
            people {soss.population.People} -- The people to get the attribute.
        Raises:
            NotImplementedError: abstract method.
        """
        raise NotImplementedError