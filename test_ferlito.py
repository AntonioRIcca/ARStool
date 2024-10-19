from dataclasses import dataclass
import numpy as np
import time

# Decorator to time functions
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)    # Call the function
        end_time = time.perf_counter()    # End the timer
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")  # Print execution time
        return result                     # Return the result of the function
    return wrapper

@dataclass
class ElementData:
    data: np.ndarray  # Data class to hold numpy array data for an element

class YourClass:
    def __init__(self, num_rows):
        self.elements_np = {}  # Dictionary to store numpy arrays for each element
        # Precompute sets for faster membership testing
        self.line_transformer_categories = set(mc['Line'] + mc['Transformer'])  # Set of line and transformer categories
        self.line_categories = set(mc['Line'])  # Set of line categories
        self.DC_elem_set = set(DC_elem)  # Set of DC elements
        self.dc_elem_pwm_set = set(DC_elem + ['PWM'])  # Set of DC elements plus 'PWM'
        self.sqrt3 = 3 ** 0.5  # Precompute square root of 3
        self.num_rows = num_rows  # Total number of rows (iterations)

        # Initialize elements_np and voltage arrays for each element
        self.initialize_elements()  # Call the initialization method

    def initialize_elements(self):
        # List comprehension to get all elements that are not nodes
        non_node_elements = [el for el in v if v[el]['category'] != 'Node']
        # List comprehension to get all elements that are nodes
        node_elements = [el for el in v if v[el]['category'] == 'Node']

        # Dictionary comprehension to initialize numpy arrays for non-node elements
        self.elements_np = {
            el: np.zeros(
                (self.num_rows, 4 if v[el]['category'] not in self.line_transformer_categories else 8)
            )  # 4 columns for terminal elements, 8 columns for lines/transformers
            for el in non_node_elements
        }

        # Initialize voltage arrays for node elements
        for el in node_elements:
            v[el]['lf']['v_array'] = np.zeros(self.num_rows)  # Preallocate voltage array for each node

    @timing_decorator  # Decorator to time the function
    def results_store_np(self, el, row):
        category = v[el]['category']  # Get the category of the element
        if category != 'Node':  # If the element is not a node
            if not v[el]['par']['out-of-service']:  # If the element is in service
                mcat = mcat_find(el)  # Find the master category of the element

                # Determine correction factors based on the category
                cf0 = self.sqrt3 if category in self.DC_elem_set else 1  # Correction factor for AC parts
                cf1 = self.sqrt3 if category in self.dc_elem_pwm_set else 1  # Correction factor for DC parts

                # Set the active element in the circuit
                self.dss.circuit.set_active_element(f"{mcat}.{el}")

                # Retrieve powers, voltages, and currents as numpy arrays
                powers = np.array(self.dss.cktelement.powers)  # Array of power values
                voltages = np.array(self.dss.cktelement.voltages_mag_ang)  # Array of voltage magnitudes and angles
                currents = np.array(self.dss.cktelement.currents_mag_ang)  # Array of current magnitudes and angles

                if category not in self.line_transformer_categories:  # If the element is a terminal element
                    # Calculate total active and reactive power by summing over phases
                    p = np.sum(powers[0:6:2])  # Sum of active powers at indices 0, 2, 4
                    q = np.sum(powers[1:6:2])  # Sum of reactive powers at indices 1, 3, 5

                    # Store the calculated values in the preallocated array
                    self.elements_np[el][row, :] = [
                        currents[0] * cf0,         # Current magnitude corrected by cf0
                        p,                         # Total active power
                        q,                         # Total reactive power
                        voltages[0] * self.sqrt3   # Voltage magnitude corrected by sqrt(3)
                    ]
                else:
                    # For lines and transformers
                    j = 6 if category in self.line_categories else 8  # Offset for terminal 1 data

                    # Indices for summing powers at terminal 0 (from indices 0 to 5)
                    indices_p0 = [2 * i for i in range(3)]            # Indices 0, 2, 4 for active power at terminal 0
                    indices_q0 = [2 * i + 1 for i in range(3)]        # Indices 1, 3, 5 for reactive power at terminal 0
                    # Indices for summing powers at terminal 1 (offset by j)
                    indices_p1 = [2 * i + j for i in range(3)]        # Indices for active power at terminal 1
                    indices_q1 = [2 * i + j + 1 for i in range(3)]    # Indices for reactive power at terminal 1

                    # Sum active and reactive powers at both terminals
                    p0 = np.sum(powers[indices_p0])   # Total active power at terminal 0
                    q0 = np.sum(powers[indices_q0])   # Total reactive power at terminal 0
                    p1 = -np.sum(powers[indices_p1])  # Negative sum of active power at terminal 1
                    q1 = -np.sum(powers[indices_q1])  # Negative sum of reactive power at terminal 1

                    # Store the calculated values in the preallocated array
                    self.elements_np[el][row, :] = [
                        currents[0] * cf0,          # Current at terminal 0 corrected by cf0
                        p0,                         # Active power at terminal 0
                        q0,                         # Reactive power at terminal 0
                        voltages[0] * self.sqrt3,   # Voltage at terminal 0 corrected by sqrt(3)
                        currents[j] * cf1,          # Current at terminal 1 corrected by cf1
                        p1,                         # Active power at terminal 1
                        q1,                         # Reactive power at terminal 1
                        voltages[j] * self.sqrt3    # Voltage at terminal 1 corrected by sqrt(3)
                    ]
            else:
                # If the element is out of service
                self.elements_np[el][row, :] = 0  # Set all values to zero
        else:
            # For nodes and source elements
            self.dss.circuit.set_active_bus(el)  # Set the active bus to the current element
            voltage = self.dss.cktelement.voltages_mag_ang[0] * self.sqrt3  # Calculate voltage magnitude
            v[el]['lf']['v_array'][row] = voltage  # Store voltage in the preallocated array

