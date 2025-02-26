# Soft Drink Vending Machine

## Overview
This project implements a simulation of a Soft Drink Vending Machine, demonstrating the principles of Theory of Computing through practical application. The vending machine is designed to handle various states, transitions, and operations typical of real-world vending machines.

## Features
- Multiple beverage selection options (Soda 🥤, Juice Box 🧃, Beer 🍺, Canned Drink 🥫)
- Coin/Note acceptance and validation (10, 20, 40, 50, 100, 200, 500, 1000 shillings)
- Change calculation and dispensing
- Modern GUI with animated dispensing system
- Real-time status display and error handling
- State-based operation system using Finite State Machine
- Visual feedback for all operations
- Drink counter and collection tray

## Technical Details
The vending machine implementation is based on:
- Finite State Machine (FSM) principles with 6 distinct states
- State transitions and event handling using Python's Enum class
- Input validation and processing for money handling
- Tkinter-based modern GUI with custom styling
- Object-oriented design with separation of concerns

## Project Structure
```
soft-drink-vending-machine/
├── main.py                    # Application entry point
├── vending_machine.py         # Core FSM implementation
├── vending_machine_gui.py     # GUI implementation
└── README.md                  # Documentation
```

## Requirements
- Python 3.6 or higher
- Tkinter (usually comes with Python)
- Windows/Linux/MacOS compatible

## Setup Instructions
1. Clone the repository
```bash
git clone [repository-url]
cd soft-drink-vending-machine
```

2. Ensure Python and Tkinter are installed
```bash
python --version  # Should be 3.6 or higher
python -c "import tkinter; tkinter._test()"  # Should open a test window
```

3. Run the application
```bash
python main.py
```

## State Machine Design
The vending machine operates using the following states:
1. S0 (0 shillings) - Initial state, waiting for money
2. S10 (10 shillings) - After first coin insertion
3. S20 (20 shillings) - Accumulating money
4. S30 (30 shillings) - Accumulating money
5. S40 (40 shillings) - Near required amount
6. S50 (50+ shillings) - Accepting state (ready to dispense)

## Usage
1. Launch the application using `python main.py`
2. Insert money using the denomination buttons:
   - Available denominations: 10, 20, 40, 50, 100, 200, 500, 1000 shillings
   - Current amount is displayed in real-time
3. Select your desired beverage from the four options:
   - Soda (🥤)
   - Juice Box (🧃)
   - Beer (🍺)
   - Canned Drink (🥫)
4. Click "Dispense Drink" when ready (enabled at 50+ shillings)
5. Collect your drink from the dispensing area
6. Collect any change by clicking "Return Change"

## Error Handling
- Insufficient funds notification (less than 50 shillings)
- Invalid coin rejection (denominations not in accepted list)
- Clear visual feedback for all operations
- State validation before dispensing
- Graceful error recovery with user-friendly messages

## GUI Features
- Two-column layout design
- Real-time amount display
- Animated dispensing mechanism
- Custom-styled buttons and controls
- Modern color scheme
- Visual drink selection
- Drink counter display
- Collection tray animation

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## License
MIT License


## Acknowledgments
- Theory of Computing course materials
- Python Tkinter documentation
- FSM implementation guidelines
- Modern GUI design principles
