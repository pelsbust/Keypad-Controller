# The Finite State Machine is also represented on a graph (see FSM.jpg)
# The graph will be used for debugging and visualizing of the rule based system.

class FiniteStateMachine:
    # Agent is a KPC object
    def __init__(self, agent):
        self.agent = agent
        self.rules = []

    # add a new rule to the end of the FSM's rule list.
    def add_rule(self, rule):
        self.rules.append(rule)

    # query the agent for the next signal.
    def get_next_signal(self):
        # next_signal = self.agent.get_next_signal()
        pass

    
    def run_rules(self):

        pass

    def apply_rule(self):
        pass

    def fire_rule(self):
        pass

    def main_loop(self):
        pass

# Rule object to use in the FiniteStateMachine class
class Rule:
    def __init__(self):
        self.trig_state = None
        self.new_state = None
        self.trig_signal = None
        self.action = None