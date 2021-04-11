import math
import random
from .AttributeBase import AttributeBase

class DiseaseState(AttributeBase):
    def __init__(self, disease_name, has_disease_probability, know_has_disease_probability):
        """Creates a new instance of DiseaseState.
        Arguments:
            disease_name {str} -- disease name, only for hashing storage in People's.
            has_disease_probability {float} -- probability of a people has the disease.
            know_has_disease_probability {float} -- probability of a people with the disease
                                                    knows that they have the disease.
        Raises:
            ValueError: Raised when one of the probabilities parsed as arguments is not between
                        0 and 1 (including extrems).
        """
        if has_disease_probability < 0 or has_disease_probability > 1:
            raise ValueError("The probability must be a value between 0 and 1 (including extrems)")
        if know_has_disease_probability < 0 or know_has_disease_probability > 1:
            raise ValueError("The probability must be a value between 0 and 1 (including extrems)")
        self.disease_name = disease_name
        self.has_disease_probability = has_disease_probability
        self.know_has_disease_probability = know_has_disease_probability

    def new(self):
        """Creates a new disease state based on the probabilities.
        Returns:
            dict -- Returns a dict with information of a people has the disease
                    and if it known if has the disease.
        """
        prob_has = random.random()
        if prob_has < self.has_disease_probability:
            prob_known = random.random()
            known = prob_known < self.know_has_disease_probability
            return {
                "has": True,
                "know": known
            }
        return {
            "has": False,
            "know": False
        }

    def apply_to(self, people):
        """Apply a new disease state to a people.
        Arguments:
            people {soss.population.People} -- The people to set the new disease state attribute.
        """
        if not hasattr(people, 'diseases'):
            people.diseases = {}
        people.diseases[self.disease_name] = self.new()

    def get_from(self, people):
        """Get the disease state from a people. If the people has not the disease state,
        in the except block the program try to create this.
        Arguments:
            people {soss.population.People} -- The people to get the disease state attribute.
        Returns:
            dict -- the disease state for this people.
        """
        try:
            return people.diseases[self.disease_name]
        except KeyError:
            self.apply_to(people)
            return people.diseases[self.disease_name]
    
    def create_counter_data(self):
        """Create a new counter data for this disease state.
        Returns:
            list -- returns an list with two items. The fisrt is the count of the peoples
                    that has the disease, and the second is the count of peoples with the
                    disease and known this.
        """
        states = [0, 0]
        return states
    
    def counter_data_to_proportion(self, counter_data):
        """Converts the disease counter data to the proportion.
        Arguments:
            counter_data {list} -- The counter data for the disease.
        """
        size = counter_data[0] + counter_data[1]
        size_has = counter_data[0]
        counter_data[0] /= size
        counter_data[1] /= size_has

    def count_to(self, counter_data, people):
        """Count the attribute in the people to a specific counter data.
        Arguments:
            counter_data {list} -- the vote counter data to increment.
            people {soss.population.People} -- The people to get the disease attribute.
        """
        state = self.get_from(people)
        if state["has"]:
            counter_data[0] += 1
        if state["know"]:
            counter_data[1] += 1