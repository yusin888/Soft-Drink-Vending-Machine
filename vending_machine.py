from enum import Enum
from typing import Optional, List, Dict

class State(Enum):
    """States representing the vending machine's accumulated money"""
    S0 = 0    # 0 shillings
    S10 = 10  # 10 shillings
    S20 = 20  # 20 shillings
    S30 = 30  # 30 shillings
    S40 = 40  # 40 shillings
    S50 = 50  # 50+ shillings (accepting state)

class VendingMachine:
    def __init__(self):
        # Define the acceptable denominations (Σ - input alphabet)
        self.acceptable_denominations = [10, 20, 40, 50, 100, 200, 500, 1000]
        
        # Initialize state variables
        self.current_amount = 0
        self.current_state = State.S0
        self.drinks_dispensed = {
            "🥤": 0,  # Soda
            "🧃": 0,  # Juice Box
            "🍺": 0,  # Beer
            "🥫": 0   # Canned Drink
        }
        
        # Initialize transition table (δ - transition function)
        self._initialize_transitions()
    
    def _initialize_transitions(self):
        """Initialize the state transition table"""
        self.transitions: Dict[State, Dict[int, State]] = {
            State.S0: {},
            State.S10: {},
            State.S20: {},
            State.S30: {},
            State.S40: {},
            State.S50: {}
        }
        
        # Define transitions for each state and input
        for state in State:
            for denomination in self.acceptable_denominations:
                new_amount = state.value + denomination
                # Find appropriate next state
                if new_amount >= 50:
                    self.transitions[state][denomination] = State.S50
                else:
                    # Find closest state without exceeding amount
                    next_state = max(
                        (s for s in State if s.value <= new_amount),
                        key=lambda s: s.value  # Compare by value instead of State object
                    )
                    self.transitions[state][denomination] = next_state
    
    def insert_money(self, denomination: int) -> bool:
        """Handle money insertion and state transition"""
        if denomination not in self.acceptable_denominations:
            return False
            
        # Get next state from transition table
        current_state = State(min(50, self.current_amount))
        next_state = self.transitions[current_state][denomination]
        
        # Update machine state
        self.current_amount += denomination
        self.current_state = next_state
        return True
    
    def can_dispense_drink(self) -> bool:
        """Check if machine is in an accepting state"""
        return self.current_state == State.S50 or self.current_amount >= 50
    
    def dispense_drink(self, drink_icon: str) -> bool:
        """Attempt to dispense a drink"""
        if not self.can_dispense_drink():
            return False
            
        self.current_amount -= 50
        self.drinks_dispensed[drink_icon] += 1
        
        # Update state after dispensing
        self.current_state = State(min(50, self.current_amount))
        return True
    
    def return_change(self) -> int:
        """Return change and reset to initial state"""
        change = self.current_amount
        self.current_amount = 0
        self.current_state = State.S0
        return change
    
    def get_current_state(self) -> str:
        """Get string representation of current state"""
        if self.current_state == State.S50:
            return "READY_TO_DISPENSE"
        return f"WAITING_{self.current_state.value}" 