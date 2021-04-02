import math

class PopulationSample:
    def __init__(self):
        """Create a new population sample.
        """
        self.peoples = []
    
    def append(self, people):
        """Append a people in this sample.
        Arguments:
            people {soss.population.People} -- The people to append.
        """
        self.peoples.append(people)

    def append_other(self, other_sample):
        """Append the peoples from other sample in this sample.
        Arguments:
            other_sample {soss.sample.PopulationSample} -- Other sample to append peoples to this.
        """
        for people in other_sample.peoples:
            self.append(people)

    def get_sample_size(self):
        """Get the count of peoples in the sample.
        Returns:
            int -- Returns the count of peoples in the sample.
        """
        return len(self.peoples)

    def count(self, counter_data, attribute):
        """Perform a count of an attribute in the sample.
        Arguments:
            counter_data {any} -- The initialized counter data.
            attribute {soss.attributes.AttributeBase} -- The attribute to count.
        """
        for people in self.peoples:
            attribute.count_to(counter_data, people)