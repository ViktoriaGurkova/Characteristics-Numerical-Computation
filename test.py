import unittest

from calculations import Calculations
from network_params import Params
from states_policy import StatesPolicy, get_policed_states


def get_performance_measures(params):
    calculations = Calculations(params)
    strategy = (0, 0, 0, 0)
    all_states = calculations.get_all_states()
    states_with_policy = get_policed_states(all_states, params)
    states_policy = StatesPolicy(strategy, states_with_policy, params)
    calculations.calculate(states_policy)
    print(calculations.performance_measures)
    return calculations.performance_measures


# TODO: fix
class TestStates(unittest.TestCase):

    def test_case1(self):
        params = Params(lambda1=1, lambda2=1, mu=3, servers_number=4,
                        fragments_numbers=[2, 3], queues_capacities=[5, 5])
        test_data = {
            "params": params,
            "expected_rt": 1.7832,
            "expected_fp": 0.1122
        }

        self.compare_results(test_data)

    def test_case2(self):
        params = Params(lambda1=1.5, lambda2=1.5, mu=3.5, servers_number=7,
                        fragments_numbers=[5, 2], queues_capacities=[8, 8])
        test_data = {
            "params": params,
            "expected_rt": 1.9515,
            "expected_fp": 0.0630
        }

        self.compare_results(test_data)

    def compare_results(self, data):
        result = get_performance_measures(data["params"])
        self.assertAlmostEqual(result.response_time, data["expected_rt"], places=3)
        self.assertAlmostEqual(result.failure_probability, data["expected_fp"], places=3)


if __name__ == '__main__':
    unittest.main()
