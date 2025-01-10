import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Step 1: Define input (AC speed) and output (room temperature)
ac_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'ac_speed')        # AC speed (0% to 100%)
temperature = ctrl.Consequent(np.arange(10, 41, 1), 'temperature')  # Room temperature (10°C to 40°C)

# Step 2: Define membership functions for AC speed
ac_speed['low'] = fuzz.trimf(ac_speed.universe, [0, 0, 50])       # Low speed: 0% to 50%
ac_speed['medium'] = fuzz.trimf(ac_speed.universe, [30, 50, 70])  # Medium speed: 30% to 70%
ac_speed['high'] = fuzz.trimf(ac_speed.universe, [50, 100, 100])  # High speed: 50% to 100%

# Step 3: Define membership functions for room temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [10, 10, 20])       # Cold: 10°C to 20°C
temperature['comfortable'] = fuzz.trimf(temperature.universe, [15, 25, 30]) # Comfortable: 15°C to 30°C
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 40, 40])         # Hot: 25°C to 40°C

# Step 4: Define fuzzy rules
rule1 = ctrl.Rule(ac_speed['low'], temperature['cold'])           # If AC speed is low, room is cold
rule2 = ctrl.Rule(ac_speed['medium'], temperature['comfortable']) # If AC speed is medium, room is comfortable
rule3 = ctrl.Rule(ac_speed['high'], temperature['hot'])           # If AC speed is high, room is hot

# Step 5: Create the control system
temp_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
temp_sim = ctrl.ControlSystemSimulation(temp_ctrl)

# Step 6: Set input AC speed and compute output
temp_sim.input['ac_speed'] = 60  # Example: AC speed is 60%
temp_sim.compute()               # Compute the output

# Step 7: Print the result
print(f"Room Temperature: {temp_sim.output['temperature']:.2f}°C")
