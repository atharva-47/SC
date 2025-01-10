import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'food_quality')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

food_quality['bad'] = fuzz.trimf(food_quality.universe, [0, 0, 5])
food_quality['decent'] = fuzz.trimf(food_quality.universe, [0, 5, 10])
food_quality['great'] = fuzz.trimf(food_quality.universe, [5, 10, 10])

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 10])
tip['medium'] = fuzz.trimf(tip.universe, [5, 15, 20])
tip['high'] = fuzz.trimf(tip.universe, [15, 25, 25])

rule1 = ctrl.Rule(service['poor'] | food_quality['bad'], tip['low'])
rule2 = ctrl.Rule(service['average'] & food_quality['decent'], tip['medium'])
rule3 = ctrl.Rule(service['excellent'] | food_quality['great'], tip['high'])

tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tip_sim = ctrl.ControlSystemSimulation(tip_ctrl)

tip_sim.input['service'] = 8
tip_sim.input['food_quality'] = 7
tip_sim.compute()

print(f"Tip Percentage: {tip_sim.output['tip']:.2f}%")
