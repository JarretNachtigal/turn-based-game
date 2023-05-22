
# this is the interface implemented by all concrete Strategy classes
class StrategyInterface:

    # all Strategy classes must implement this method
    def print_strategy():
        pass



# This is the Context class. It is the class that would be hypothetically refactored when implementing
# the strategy pattern
class Context:

    def __init__(self, strategy: StrategyInterface) -> None:
        self.strategy = strategy # would need setter/ getter

    # this is all that Context does on its end
    # this code is now abstracted from Context
    def execute_strategy(self):
        self.strategy.print_strategy()