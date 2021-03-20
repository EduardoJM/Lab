import math
import random
from .AttributeBase import AttributeBase

class VoteGeneratorRule(AttributeBase):
    def __init__(self, probabilities):
        """Creates a new instance of the VoteGeneratorRule for creating votations simulations.
        Arguments:
            probabilities {list} -- an probabilities list, with one probability (a value between 0 and 1, 
            including the extrems) for each candidate.
        Raises:
            ValueError: raised when one of the probabilities is not between 0 and one (including the extrems).
        """
        self.probabilities = probabilities
        self.candidates = len(self.probabilities)
        self.rule = []
        accumulative = 0
        for i in range(0, self.candidates):
            p = self.probabilities[i]
            if p < 0 or p > 1:
                raise ValueError("The probability must be an value between 0 and 1.")
            num = math.floor(p * 100)
            self.rule.append(num + accumulative)
            accumulative += num
        
    def new(self):
        """Create a new vote, based on the probabilities of get votes.
        Returns:
            int -- return the candidate index that receives the vote.
        """
        random_vote = random.randint(0, 100)
        for i in range(0, self.candidates):
            if random_vote <= self.rule[i]:
                return i
        return 0

    def apply_to(self, people):
        """Apply a new vote to a people.
        Arguments:
            people {soss.population.People} -- The people to set the new vote attribute.
        """
        people.vote = self.new()

    def get_from(self, people):
        """Get vote from a people if the people has this attribute. If the people has not
        an vote attribute, the except block try to apply a new vote to this people and
        return it.
        Arguments:
            people {soss.population.People} -- The people to get the vote attribute.
        Returns:
            int -- return the candidate index that receives the vote.
        """
        try:
            return people.vote
        except AttributeError:
            self.apply_to(people)
            return people.vote

    def create_counter_data(self):
        """Creates a new vote counter data.
        Returns:
            list -- returns an empty vote counter data.
        """
        candidates_array = []
        for _ in range(0, self.candidates):
            candidates_array.append(0)
        return candidates_array

    def counter_data_to_proportion(self, counter_data):
        """Converts the vote counter data to the proportion. This is an helper method that only
        divide all the items in the vote counter data list by the size.
        Arguments:
            counter_data {list} -- the vote counter data.
        """
        size = 0
        for i in counter_data:
            size += i
        for i in range(0, len(counter_data)):
            counter_data[i] /= size

    def count_to(self, counter_data, people):
        """Count the attribute in the people to a specific counter data.
        Arguments:
            counter_data {list} -- the vote counter data to increment.
            people {soss.population.People} -- The people to get the vote attribute.
        """
        index = self.get_from(people)
        counter_data[index] += 1