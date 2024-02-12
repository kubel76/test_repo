import random
from math import log2


def generate_cup_schedule(teams: list) -> list:
  """
  Генерує розклад турніру та виводить кожну стадію
  та результати жеребкування.

  :param teams: Список команд у турнірі.
  :return: Команда(и), яка(і) залишилася в кінці кожного раунду.
  """
  rounds = 1
  stage_count = int(log2(len(teams)))

  while len(teams) > 1:
    team_quantity: int = len(teams)
    print(f"{teams}, стадія: {get_round_name(rounds, stage_count)}")

    # проводимо жеребкування команд в залежності від кількості
    random.shuffle(teams)

    if team_quantity % 2 == 0:
      paired_tuples: list[tuple] = [
        (teams[i], teams[i + 1]) for i in range(0, team_quantity, 2)
      ]
    else:
      # відкидаємо непарну команду
      spare_team: str = teams.pop()
      paired_tuples: list[tuple] = [
        (teams[i], teams[i + 1]) for i in range(0, team_quantity - 1, 2)
      ]
      # додаємо відкинуту команду в кінець зжеребкованого списку
      paired_tuples.append(spare_team)

    print(f"Результати жеребкування: {paired_tuples}")
    # Беремо список команд, які зрандомились у функції
    teams = random_next(paired_tuples)
    rounds += 1

  return teams


def random_next(teams: list) -> list:
  """
  Вибирає випадковим чином команди, які переходять до наступного раунду.

  :param teams: Список команд, що брали участь у жеребкуванні.
  :return: Команди, які перейшли до наступного раунду.

  Потрібна лише як приклад в реальному проекті дані будуть братися з БД
  """
  next_teams: list = [random.choice(pair) for pair in teams]
  if len(next_teams) > 1:
    print(f"Команди в наступному раунді: {next_teams}")
    return next_teams
  print(f"Переможець: {next_teams}")
  return next_teams


def get_round_name(round_number: int, total_rounds: int) -> str:
  """
  Визначає назву стадії турніру на основі номера раунду
  та загальної кількості раундів.

  :param round_number: Номер поточного раунду.
  :param total_rounds: Загальна кількість раундів у турнірі.
  :return: Назва стадії турніру.
  """
  if round_number == total_rounds:
    return "Фінал"
  elif round_number == total_rounds - 1:
    return "1/2"
  elif round_number == total_rounds - 2:
    return "1/4"
  elif round_number == total_rounds - 3:
    return "1/8"
  elif round_number == total_rounds - 4:
    return "1/16"
  elif round_number == total_rounds - 5:
    return "1/32"
  elif round_number == total_rounds - 6:
    return "1/64"
  elif round_number == total_rounds - 7:
    return "1/128"
  elif round_number == total_rounds - 8:
    return "1/256"
  else:
    return f"Раунд {round_number} Суперфінал"


list_teams = ["a", "b", "c", "d", "e", "f", "g", "i", "k"]
generate_cup_schedule(list_teams)
