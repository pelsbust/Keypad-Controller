# The Finite State Machine is also represented on a graph (see FSM.jpg)
# The graph will be used for debugging and visualizing of the rule based system.

class FiniteStateMachine:
    # Agent is a KPC object
    def __init__(self, agent):
        self.agent = agent
        self.fsm_state = None
        self.current_signal = None
        # Array of rule objects
        self.rules = []
        self.states = ["state_init", "state_read", "verify", "active", "change_password", "led", "led_time", "logout"]

        rules_dict = {
            # state_init
            (self.states[0], not None): True,
            # state_read
            (self.states[1], range(0, 9 + 1)): True,
            # verify
            (self.states[2], "*"): True,
            # active
            (self.states[3], "Y"): True,
            # change_password1
            (self.states[4], "*"): True,
            # change_password2 (type twice)
            (self.states[4], range(0, 9 + 1)): True,
            # led_time
            (self.states[7]): True,
        }

    # add a new rule to the end of the FSM's rule list.
    # Rule(trig_state, new_state, trig_signal)
    def add_rule(self, state):
        states = ["state_init", "state_read", "verify", "active", "change_password", "led", "led_time", "logout"]

        # Inputing the password
        self.rules.append(Rule(self.states[0], self.states[1], self.is_digit()))
        # Verify the password
        self.rules.append(Rule(self.states[1], self.states[2], "*"))
        # Verified and now active state
        self.rules.append(Rule(self.states[2], self.states[3], "Y"))
        # Not verified and hence is reset
        self.rules.append(Rule(self.states[2], self.states[0], not "Y"))
        # Password change
        self.rules.append(Rule(self.states[3], self.states[4], "*"))
        # Read a new password
        self.rules.append(Rule(self.states[4], self.states[1], self.is_digit()))
        # Reset to active-state if not a digit.
        self.rules.append(Rule(self.states[4], self.states[3], not self.is_digit()))
        # Led
        self.rules.append(Rule(self.states[3], self.states[5], self.is_first_five_digit()))
        # Duration state
        self.rules.append(Rule(self.states[5], self.states[6], "*"))
        # Duration
        self.rules.append(Rule(self.states[6], self.states[6], self.is_digit()))
        # Back to active state
        self.rules.append(Rule(self.states[6], self.states[3], "*"))
        # Logout (If you want to start again you may after the FSM is done)
        self.rules.append(Rule(self.states[3], self.states[7], "#"))


    # query the agent for the next signal.
    def get_next_signal(self):
        self.current_signal = self.agent.get_next_signal()

    # Rememeber the right order of the rules!
    def run_rules(self):
        for rule in self.rules:
            if self.apply_rule(rule):
                self.fire_rule(rule)

    # Check whether the conditions of a rule are met or not. Return boolean.
    def apply_rule(self, rule):
        states = ["state_init", "state_read", "verify", "active", "change_password", "led", "led_time", "logout"]
        state_dict = {
            self.states[0]: "",
            self.states[1]: "",
            self.states[2]: "",
            self.states[3]: "",
            self.states[4]: "",
            self.states[5]: "",
            self.states[6]: "",
            self.states[7]: "",
            self.states[8]: "",
        }
        # Check the self.fsm_state.
        temp = state_dict(self.fsm_state)

    def fire_rule(self, rule):
        pass

    def main_loop(self):
        pass

    def is_valid_state(self, state):
        if state in self.states:
            return True
        return False


# Rule object to use in the FiniteStateMachine class
class Rule:

    # Remember to call agent's action!
    def __init__(self, trig_state, new_state, trig_signal):
        self.state1 = trig_state
        self.state2 = new_state         # If the rule fires we change the state and call an appropriate action.
        self.signal = trig_signal



    def check_rule_exists(self, fsm_state, current_signal):
        states = ["state_init", "state_read", "verify", "active", "change_password", "led_time"]

        # Remember to implement the else action: to reset the state!
        # Not finished yet





