import pandas as pd
import numpy as np
from scipy.stats import ks_2samp, chi2_contingency
from scipy.spatial.distance import jensenshannon

class DataDriftMonitor:

    def __init__(self, reference_data, current_data):
        self.reference = reference_data
        self.current = current_data

    def ks_test(self, column):
        stat, p_value = ks_2samp(
            self.reference[column],
            self.current[column]
        )
        return stat, p_value

    def psi(self, column, bins=10):
        ref_counts, bin_edges = np.histogram(self.reference[column], bins=bins)
        curr_counts, _ = np.histogram(self.current[column], bins=bin_edges)

        ref_perc = ref_counts / len(self.reference)
        curr_perc = curr_counts / len(self.current)

        psi = np.sum((ref_perc - curr_perc) * np.log((ref_perc + 1e-6) / (curr_perc + 1e-6)))
        return psi

    def jensen_shannon(self, column, bins=10):
        ref_counts, bin_edges = np.histogram(self.reference[column], bins=bins)
        curr_counts, _ = np.histogram(self.current[column], bins=bin_edges)

        ref_perc = ref_counts / ref_counts.sum()
        curr_perc = curr_counts / curr_counts.sum()

        return jensenshannon(ref_perc, curr_perc)