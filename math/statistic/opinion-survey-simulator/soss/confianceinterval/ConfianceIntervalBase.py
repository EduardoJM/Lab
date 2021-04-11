from abc import ABC, abstractmethod

class ConfianceIntervalBase(ABC):
    @abstractmethod
    def get_error_to(self, sample, confiability = 0.95):
        """(Abstract) Method to be implemented to get error range for a sample with a confiability.
        Arguments:
            sample {soss.sample.PopulationSample} -- the sample to get the confiance interval error.
        Keyword Arguments:
            confiability {float} -- the confiability of the confiance interval, the 
            same of the probability of this reflect the reality (default: {0.95})
        """
        raise NotImplementedError