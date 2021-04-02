import math
import scipy.stats
from .ConfianceIntervalBase import ConfianceIntervalBase

class ProportionOptimist(ConfianceIntervalBase):
    def __init__(self, proportion):
        """creates a new instance of the ProportionOptimist confiance interval.
        Arguments:
            proportion {float} -- the proportion of the data to create the confiance interval.
        """
        self.proportion = proportion

    def get_error_to(self, sample, confiability = 0.95):
        """Get error range for a sample with a confiability.
        Arguments:
            sample {soss.sample.PopulationSample} -- the sample to get the confiance interval error.
        Keyword Arguments:
            confiability {float} -- the confiability of the confiance interval, the 
            same of the probability of this reflect the reality (default: {0.95})
        Raises:
            ValueError: raised when confiability is not between 0 and one (including the extrems).
        Returns:
            float -- the error (+\-) for the confiance interval.
        """
        if confiability < 0 or confiability > 1:
            raise ValueError("the confiability must be a value between 0 and 1")
        prob = (1 - confiability) / 2
        z = abs(scipy.stats.norm(0, 1).ppf(prob))
        size = sample.get_sample_size()
        if type(self.proportion) == list:
            result = []
            for num in self.proportion:
                error = z * math.sqrt(num * (1 - num) / size)
                result.append(error)
            return result
        return z * math.sqrt(self.proportion * (1 - self.proportion) / size)