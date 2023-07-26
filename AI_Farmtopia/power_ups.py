```python
import json
from .ai_components import AIComponentSchema

class PowerUp:
    def __init__(self, name, effect, cost):
        self.name = name
        self.effect = effect
        self.cost = cost

    def apply_effect(self, playerData):
        self.effect(playerData)

class PowerUpStore:
    def __init__(self):
        self.power_ups = []

    def load_power_ups(self, filename):
        with open(filename, 'r') as f:
            power_up_data = json.load(f)
            for power_up in power_up_data:
                self.power_ups.append(PowerUp(**power_up))

    def purchase_power_up(self, power_up_name, playerData):
        for power_up in self.power_ups:
            if power_up.name == power_up_name:
                if playerData['coins'] >= power_up.cost:
                    playerData['coins'] -= power_up.cost
                    power_up.apply_effect(playerData)
                    return True
        return False

def purchasePowerUp(power_up_name, playerData):
    store = PowerUpStore()
    store.load_power_ups('power_ups.json')
    success = store.purchase_power_up(power_up_name, playerData)
    if success:
        updatePlayer(playerData)
        updateMonetization({'type': 'purchase', 'item': power_up_name})
    return success
```