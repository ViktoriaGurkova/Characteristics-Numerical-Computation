import logging

from network_params import Params
from state_functional import StateConfig
from pretty_state import pretty_state

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('app.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)


def log_network_configuration(params: Params) -> None:
    # TODO: расписать параметры системы
    logger.debug('Network configuration:')
    logger.debug(f'lambda 1 = {params.lambda1}')
    logger.debug(f'lambda 2 = {params.lambda2}')
    logger.debug(f'mu = {params.mu}')
    logger.debug(f'servers number = {params.servers_number}')
    logger.debug(f'fragments numbers = {params.fragments_numbers}')
    logger.debug(f'queues capacities = {params.queues_capacities}')


def log_message(message: str) -> None:
    logger.debug('\n' + message)


def log_event(event: str) -> None:
    logger.debug('\n<===' + event + '===>')


def log_lost_demand() -> None:
    logger.debug('Queue is full - demand is lost')


def log_state(current_state: list) -> None:
    logger.debug('\n' + '=' * 120 + '\n')
    logger.debug('Consider state ' + pretty_state(current_state))


def log_state_config(state_config: StateConfig) -> None:
    logger.debug(f'Queue 1 size = {state_config.q1}')
    logger.debug(f'Queue 2 size = {state_config.q2}')
    logger.debug(f'Servers state = {state_config.servers}')
    logger.debug(f'Free servers number = {state_config.free_servers_number}')


def log_arrival_in_queue(lambda_: float, state: tuple, class_id: int) -> None:
    logger.debug(f'Arrival of the {class_id} class demand to '
                 f'the queue with rate {lambda_} and '
                 f'transition to state  {pretty_state(state)}')


def log_arrival_on_servers(lambda_: float, state: tuple, class_id: int) -> None:
    logger.debug(f'Arrival of the {class_id} class demand '
                 f'with rate {lambda_} and '
                 f'immediate start of its service and  '
                 f'transition to state {pretty_state(state)}')


def log_leaving_demand(mu: float, state: tuple, class_id: int) -> None:
    logger.debug(f'Service completion of whole '
                 f'{class_id} class demand with rate {mu} and '
                 f'transition to state {pretty_state(state)}')


def log_leaving_fragment(leave_rate: float, state: tuple, class_id: int) -> None:
    logger.debug(f'Service completion of '
                 f'{class_id} class demand fragment with '
                 f'rate {leave_rate} and '
                 f'transition to state {pretty_state(state)}')
