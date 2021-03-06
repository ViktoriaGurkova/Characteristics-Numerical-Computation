from pprint import pprint

from calculations import Calculations
from network_params import Params
from performance_measures_storage import PerformanceMeasuresStorage
from states_policy import StatesPolicy
from states_policy import get_policed_states, get_strategy

if __name__ == '__main__':
    params = Params(mu=3, lambda1=.5, lambda2=1,
                    servers_number=5,
                    fragments_numbers=[2, 3],
                    queues_capacities=[1, 1])
    calculations = Calculations(params)

    all_states = calculations.get_all_states()
    states_with_policy = get_policed_states(all_states, params)
    print("All states where policy is possible:")
    pprint(states_with_policy)

    strategies = get_strategy(states_with_policy)
    states_policy = StatesPolicy(tuple(), states_with_policy, params)
    states_policy.print_adjacent_states()

    storage = PerformanceMeasuresStorage()
    print()

    for strategy in strategies:
        states_policy.strategy = strategy
        print(strategy)
        calculations = Calculations(params)
        calculations.calculate(states_policy)
        performance_measures = calculations.performance_measures
        print(performance_measures, "\n")

        storage.append(strategy, performance_measures)

    print(storage)
    print()
    storage.show_difference()

    print("executed")
