```python
import datetime
from player_data import PlayerData

class Metrics:
    def __init__(self):
        self.player_data = PlayerData()

    def enchanted_daily_adventures(self):
        today = datetime.date.today()
        daily_players = self.player_data.get_daily_players(today)
        return len(daily_players)

    def reten_sorcery_rate(self, days):
        today = datetime.date.today()
        start_date = today - datetime.timedelta(days=days)
        players_then = self.player_data.get_daily_players(start_date)
        players_now = self.player_data.get_daily_players(today)

        retained_players = [player for player in players_then if player in players_now]
        if players_then:
            return len(retained_players) / len(players_then)
        else:
            return 0

    def player_enchantments(self):
        enchantments = self.player_data.get_all_enchantments()
        enchantment_counts = {enchantment: enchantments.count(enchantment) for enchantment in set(enchantments)}
        return enchantment_counts
```