import tkinter as tk
from tkinter import messagebox, ttk
from vending_machine import VendingMachine

class VendingMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Soft Drink Vending Machine")
        self.root.geometry("1000x700")  # Increased window size
        self.root.configure(bg="#2C3E50")
        
        self.machine = VendingMachine()
        self.style = ttk.Style()  # Make style a class instance variable
        self._setup_styles()
        self._create_main_layout()
    
    def _setup_styles(self):
        """Configure custom styles for widgets"""
        # Color scheme
        self.colors = {
            'bg_dark': '#1E272E',        # Dark background
            'bg_medium': '#2C3A47',      # Medium background
            'accent1': '#0BE881',        # Green accent
            'accent2': '#FF3F34',        # Red accent
            'text_light': '#F8EFBA',     # Light text
            'text_dark': '#1E272E',      # Dark text
            'button_hover': '#05C46B',   # Button hover
            'money_btn': '#3C40C6',      # Money button color
            'tray': '#485460'            # Collection tray color
        }
        
        # Money button style
        self.style.configure(
            "Money.TButton",
            padding=10,
            relief="raised",
            background=self.colors['money_btn'],
            foreground=self.colors['text_dark'],
            font=("Arial", 11, "bold")
        )
        
        # Action button styles
        self.style.configure(
            "Dispense.TButton",
            padding=12,
            background=self.colors['accent1'],
            foreground=self.colors['text_dark'],
            font=("Arial", 12, "bold")
        )
        
        self.style.configure(
            "Change.TButton",
            padding=12,
            background=self.colors['accent2'],
            foreground=self.colors['text_dark'],
            font=("Arial", 12, "bold")
        )
        
        # Frame styles
        self.style.configure(
            "Panel.TLabelframe",
            background=self.colors['bg_medium'],
            padding=15
        )
        
        self.style.configure(
            "Panel.TLabelframe.Label",
            font=("Arial", 12, "bold"),
            foreground=self.colors['text_light'],
            background=self.colors['bg_medium']
        )
    
    def _create_main_layout(self):
        """Create the main two-column layout"""
        # Main container with two columns
        main_container = ttk.Frame(self.root, padding="10")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left column (Control Panel)
        left_column = ttk.Frame(main_container, padding="5")
        left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Right column (Dispensing Area)
        right_column = ttk.Frame(main_container, padding="5")
        right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create sections
        self._create_display_panel(left_column)
        self._create_money_panel(left_column)
        self._create_drink_selection(left_column)
        self._create_control_buttons(left_column)
        self._create_dispensing_area(right_column)
    
    def _create_display_panel(self, parent):
        """Create the display panel in the left column"""
        display_frame = ttk.LabelFrame(
            parent,
            text="Display",
            style="Panel.TLabelframe"
        )
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.amount_label = ttk.Label(
            display_frame,
            text="Insert KShs. 50 or more",
            font=("Arial", 14),
            foreground=self.colors['text_light'],
            background=self.colors['bg_medium']
        )
        self.amount_label.pack(pady=5)
        
        self.current_amount_label = ttk.Label(
            display_frame,
            text="Current: KShs. 0",
            font=("Arial", 18, "bold"),
            foreground=self.colors['accent1'],
            background=self.colors['bg_medium']
        )
        self.current_amount_label.pack(pady=5)
    
    def _create_money_panel(self, parent):
        """Create the money insertion panel"""
        money_frame = ttk.LabelFrame(
            parent,
            text="Insert Money",
            style="Panel.TLabelframe"
        )
        money_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Configure grid
        for i in range(2):
            money_frame.grid_columnconfigure(i, weight=1)
        
        # Create denomination buttons in 4x2 grid
        denominations = self.machine.acceptable_denominations
        for i, amount in enumerate(denominations):
            btn = ttk.Button(
                money_frame,
                text=f"KShs. {amount}",
                style="Money.TButton",
                command=lambda d=amount: self.insert_money(d)
            )
            btn.grid(
                row=i // 2,
                column=i % 2,
                padx=5,
                pady=5,
                sticky="nsew"
            )
    
    def _create_drink_selection(self, parent):
        """Create the drink selection panel"""
        selection_frame = ttk.LabelFrame(
            parent,
            text="Select Your Drink",
            style="Panel.TLabelframe"
        )
        selection_frame.pack(fill=tk.X, pady=(0, 10))
        
        drinks_frame = ttk.Frame(selection_frame, style="Panel.TLabelframe")
        drinks_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Updated drink options with custom colors
        drinks = [
            ("Soda", "🥤", 50, "#FF9FF3"),      # Pink
            ("Juice Box", "🧃", 50, "#FFC048"),  # Orange
            ("Beer", "🍺", 50, "#FFDD59"),       # Yellow
            ("Canned Drink", "🥫", 50, "#FF5E57") # Red
        ]
        
        self.selected_drink = tk.StringVar(value="🥤")
        for i, (name, icon, price, color) in enumerate(drinks):
            rb = ttk.Radiobutton(
                drinks_frame,
                text=f"{icon} {name}\nKShs. {price}",
                value=icon,
                variable=self.selected_drink,
                padding="10",
                style=f"Drink{i}.TRadiobutton"
            )
            # Configure style for each drink option using self.style
            self.style.configure(
                f"Drink{i}.TRadiobutton",
                background=self.colors['bg_medium'],
                foreground=color,
                font=("Arial", 11, "bold")
            )
            rb.grid(row=0, column=i, padx=10, pady=5)
    
    def _create_control_buttons(self, parent):
        """Create the control buttons panel"""
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.dispense_btn = ttk.Button(
            button_frame,
            text="Dispense Drink",
            style="Dispense.TButton",
            command=self.dispense_drink,
            state="disabled"
        )
        self.dispense_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.change_btn = ttk.Button(
            button_frame,
            text="Return Change",
            style="Change.TButton",
            command=self.return_change
        )
        self.change_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
    
    def _create_dispensing_area(self, parent):
        """Create the dispensing area in the right column"""
        dispense_frame = ttk.LabelFrame(
            parent,
            text="Dispensing Area",
            style="Panel.TLabelframe"
        )
        dispense_frame.pack(fill=tk.BOTH, expand=True)
        
        # Drinks counter at the top
        self.drinks_label = ttk.Label(
            dispense_frame,
            text="Drinks dispensed:",
            font=("Arial", 12),
            background=self.colors['bg_medium'],
            foreground=self.colors['text_light']
        )
        self.drinks_label.pack(pady=10)
        
        # Main dispensing canvas
        self.dispense_canvas = tk.Canvas(
            dispense_frame,
            width=450,
            height=400,
            bg=self.colors['bg_dark'],
            highlightthickness=0
        )
        self.dispense_canvas.pack(pady=10, padx=10)
        
        # Create collection tray
        self._create_collection_tray()
    
    def _create_collection_tray(self):
        """Create the collection tray at the bottom of dispensing area"""
        # Draw tray outline with gradient effect
        self.dispense_canvas.create_rectangle(
            50, 350, 400, 380,
            fill=self.colors['tray'],
            outline=self.colors['text_light'],
            width=2
        )
        
        # Add tray label with shadow effect
        self.dispense_canvas.create_text(
            227, 367,  # Shadow position
            text="Collection Tray",
            fill=self.colors['bg_dark'],
            font=("Arial", 10, "bold")
        )
        self.dispense_canvas.create_text(
            225, 365,  # Main text position
            text="Collection Tray",
            fill=self.colors['text_light'],
            font=("Arial", 10, "bold")
        )
    
    def insert_money(self, denomination):
        """Handle money insertion"""
        if self.machine.insert_money(denomination):
            self._animate_coin(denomination)
            self._update_display()
    
    def dispense_drink(self):
        """Handle drink dispensing"""
        selected_drink = self.selected_drink.get()
        if self.machine.dispense_drink(selected_drink):
            self._animate_dispensing()
            self._update_display()
    
    def return_change(self):
        """Handle returning change"""
        change = self.machine.return_change()
        if change > 0:
            messagebox.showinfo(
                "Change Returned",
                f"Please collect your change: KShs. {change}"
            )
        self._update_display()
    
    def _animate_coin(self, denomination):
        """Animate coin insertion"""
        x = 200  # Center of canvas
        
        # Create coin with gradient effect
        coin = self.dispense_canvas.create_oval(
            x-20, 0, x+20, 40,
            fill="#FFD700",
            outline="#DAA520",
            width=2
        )
        # Add shine effect
        shine = self.dispense_canvas.create_oval(
            x-15, 5, x-5, 15,
            fill="white",
            outline=""
        )
        text = self.dispense_canvas.create_text(
            x, 20,
            text=str(denomination),
            fill=self.colors['text_dark'],
            font=("Arial", 11, "bold")
        )
        
        def move_coin(y=0):
            if y < 160:
                for item in [coin, shine, text]:
                    self.dispense_canvas.move(item, 0, 5)
                self.root.after(50, move_coin, y + 5)
            else:
                for item in [coin, shine, text]:
                    self.dispense_canvas.delete(item)
        
        move_coin()
    
    def _animate_dispensing(self):
        """Animate drink dispensing"""
        x = 200  # Center of canvas
        
        # Get selected drink icon
        drink_icon = self.selected_drink.get()
        
        # Create drink icon
        drink = self.dispense_canvas.create_text(
            x, 0,
            text=drink_icon,
            font=("TkDefaultFont", 36),
            fill="white"
        )
        
        def move_drink(y=0):
            if y < 160:
                self.dispense_canvas.move(drink, 0, 5)
                self.root.after(50, move_drink, y + 5)
            else:
                self.dispense_canvas.delete(drink)
                # Show message about collected drink
                messagebox.showinfo(
                    "Drink Dispensed",
                    f"Please collect your drink! {drink_icon}"
                )
        
        move_drink()
    
    def _update_display(self):
        """Update all display elements"""
        # Update amount display
        self.current_amount_label.config(
            text=f"Current: KShs. {self.machine.current_amount}"
        )
        
        # Update drinks count with details
        drinks_text = "Drinks dispensed:\n"
        for icon, count in self.machine.drinks_dispensed.items():
            if count > 0:
                drinks_text += f"{icon}: {count}\n"
        self.drinks_label.config(text=drinks_text)
        
        # Update dispense button state
        if self.machine.can_dispense_drink():
            self.dispense_btn.config(state="normal")
            self.amount_label.config(text="Ready to dispense drink")
        else:
            self.dispense_btn.config(state="disabled")
            remaining = 50 - self.machine.current_amount
            if remaining > 0:
                self.amount_label.config(text=f"Insert KShs. {remaining} more")
            else:
                self.amount_label.config(text="Insert KShs. 50 or more")

def main():
    root = tk.Tk()
    app = VendingMachineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 