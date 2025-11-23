class HockeyTeam:
    def __init__(self, name, games, wins, draws, losses):
        self.name = name
        self.games = games
        self.wins = wins
        self.draws = draws
        self.losses = losses

    def total_points(self):
        return self.wins * 2 + self.draws

    def win_percent(self):
        if self.games == 0:
            return 0
        return (self.wins / self.games) * 100



class JuniorHockeyTeam(HockeyTeam):
    def __init__(self, name, games, wins, draws, losses, age_group):
        super().__init__(name, games, wins, draws, losses)
        self.age_group = age_group



import numpy as np

def analyze_scores(scores):
    scores_array = np.array(scores)
    avg = np.mean(scores_array)
    mx = np.max(scores_array)
    mn = np.min(scores_array)
    return avg, mx, mn




print("--- Hokkei natizhelerin taldau zhüiesi ---")

team_name = input("Komanda atawy: ")
games = int(input("Oiyndar sany: "))
wins = int(input("Zhenister: "))
draws = int(input("Ten oiyndar: "))
losses = int(input("Zhenilister: "))

team = HockeyTeam(team_name, games, wins, draws, losses)

print("\n--- Komanda natizhesi ---")
print("Komanda:", team.name)
print("Upai:", team.total_points())
print(f"Zhenis paiyzy: {team.win_percent():.1f}%")


print("\n--- Gol taldau (NumPy) ---")
scores_input = input("Gol sanin engiziniz (мысалы: 3 1 4 2): ")
scores = list(map(int, scores_input.split()))

avg, mx, mn = analyze_scores(scores)

print("Orta gol sany:", avg)
print("En joğarı gol:", mx)
print("En tomen gol:", mn)
