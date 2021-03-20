import math
import scipy.stats
from .ConfianceIntervalBase import ConfianceIntervalBase

class ProportionConservator(ConfianceIntervalBase):
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
        error = z / math.sqrt(4 * sample.get_sample_size())
        return error

    @staticmethod
    def get_sample_size(confiability = 0.95, error = 0.02):
        """Get a sample size for a determinated confiability and error range.
        Keyword Arguments:
            confiability {float} -- the confiability of the confiance interval, the 
            same of the probability of this reflect the reality (default: {0.95})
            error {float} -- the error range for the confiance interval creation (default: {0.02})
        Raises:
            ValueError: raised when confiability or error is not between 0 and one (including the extrems).
        Returns:
            int -- the count of peoples to create a sample to get a conservator
                   confiance interval with this confiability and this error.
        """
        if confiability < 0 or confiability > 1:
            raise ValueError("the confiability must be a value between 0 and 1");
        if error < 0 or error > 1:
            raise ValueError("the error must be a value between 0 and 1");
        prob = (1 - confiability) / 2
        z = abs(scipy.stats.norm(0, 1).ppf(prob))
        n = (z / error)**2 / 4
        return math.ceil(n)