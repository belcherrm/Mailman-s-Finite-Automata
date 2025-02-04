def get_easy_dfa():
    """
    Returns an easy DFA configuration.
    - 3 states: A (start), B, C (accepting)
    - Input symbols: 'a', 'b'
    - Deterministic transitions
    """
    dfa = {
        "states": ["A", "B", "C"],  # DFA states
        "alphabet": ["a", "b"],  # Allowed inputs
        "start_state": "A",  # Initial state
        "accept_states": ["C"],  # Accepting states (mail delivered)
        "transitions": {
            "A": {"a": "B", "b": "A"},  # 'a' moves to B, 'b' stays in A
            "B": {"a": "B", "b": "C"},  # 'b' moves to C (accepting), 'a' stays in B
            "C": {"a": "C", "b": "C"}   # Stays in accepting state
        }
    }
    return dfa