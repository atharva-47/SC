import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')
distance = ctrl.Consequent(np.arange(0, 101, 1), 'distance')

speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 50])
speed['medium'] = fuzz.trimf(speed.universe, [30, 50, 70])
speed['fast'] = fuzz.trimf(speed.universe, [50, 100, 100])

distance['close'] = fuzz.trimf(distance.universe, [0, 0, 30])
distance['moderate'] = fuzz.trimf(distance.universe, [20, 40, 60])
distance['far'] = fuzz.trimf(distance.universe, [50, 100, 100])

rule1 = ctrl.Rule(speed['slow'], distance['close'])
rule2 = ctrl.Rule(speed['medium'], distance['moderate'])
rule3 = ctrl.Rule(speed['fast'], distance['far'])

distance_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
distance_sim = ctrl.ControlSystemSimulation(distance_ctrl)

distance_sim.input['speed'] = 60
distance_sim.compute()

print(f"Distance to Obstacle: {distance_sim.output['distance']:.2f}m")
