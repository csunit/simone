from typing import Dict, List, Tuple, Set

EPSILON = "ε"


class NFA():

    def __init__(
            self, states: Set[str], alphabet: Set[str], initial_state: str,
            final_states: Set[str],
            transitions: Dict[Tuple[str, str], Set[str]]) -> None:
        self._states = states
        self._alphabet = alphabet  # | set(EPSILON)
        self._transitions = transitions
        self._initial_state = initial_state
        self._final_states = final_states

    def transition_table(self) -> Dict[Tuple[str, str], Set[str]]:
        return self._transitions

    def states(self) -> List[str]:
        return sorted(self._states)

    def initial_state(self) -> str:
        return self._initial_state

    def final_states(self) -> Set[str]:
        return self._final_states

    def alphabet(self) -> List[str]:
        return sorted(self._alphabet)

    def add_symbol(self, symbol: str) -> None:
        self._alphabet.add(symbol)

    def remove_symbol(self, symbol: str) -> None:
        if symbol in self._alphabet:
            self._alphabet.remove(symbol)
        else:
            raise KeyError("Symbol {} does not exist".format(symbol))

    def add_state(self, state: str) -> None:
        self._states.add(state)

    def remove_state(self, state: str) -> None:
        if state in self._states:
            self._states.remove(state)
        else:
            raise KeyError("State {} does not exist".format(state))

    def make_state_final(self, state: str) -> None:
        if state in self._states:
            self._final_states.add(state)
        else:
            raise KeyError("State {} does not exist".format(state))

    def set_transition(
            self, state: str, symbol: str, next_states: Set[str]) -> None:
        if next_states <= self._states:
            self._transitions[(state, symbol)] = next_states
        else:
            states = ", ".join(next_states - self._states)
            raise KeyError("State(s) {} do not exist".format(states))

    def accept(self, string: str) -> bool:
        current_state = self._initial_state
        for symbol in string:
            try:
                next_state = self._transitions[current_state, symbol]
                if len(next_state) > 1:
                    raise RuntimeError("Automata is non-deterministic")
                else:
                    current_state = next(iter(next_state))
            except KeyError:
                return False
        return current_state in self._final_states
