from listener import Listener

# This will *probably* never have anything in it...
class AbstractGrade(Listener):
  pass

# DDR 6th-8th mix "dance points" grading. This is IMO one of the
# fairest grading algorithms and definitely one of the most common.
class DancePointsGrade(AbstractGrade):
  def __init__(self):
    self.score = 0
    self.arrow_count = 0
    self.hold_count = 0
    self.inc = { "V": 2, "P": 2, "G": 1, "B": -4, "M": -8 }

  def ok_hold(self):
    self.hold_count += 1
    self.score += 6

  def broke_hold(self):
    self.hold_count += 1

  def stepped(self, cur_time, rating, combo):
    self.arrow_count += 1
    self.score += self.inc.get(rating, 0)

  def grade(self, failed):
    max_score = float(2 * self.arrow_count + 6 * self.hold_count)

    if failed == True: return "E"
    elif max_score == 0: return "?"
    elif self.score / max_score >= 1.00: return "AAA"
    elif self.score / max_score >= 0.93: return "AA"
    elif self.score / max_score >= 0.80: return "A"
    elif self.score / max_score >= 0.65: return "B"
    elif self.score / max_score >= 0.45: return "C"
    else: return "D"

# Appropriate for endless mode, it doesn't return E on failure (since
# endless mode always ends in a failure).
class EndlessGrade(DancePointsGrade):
  def grade(self, failed): return DancePointsGrade.grade(self, False)

grades = [DancePointsGrade, EndlessGrade]
grade_opt = [(0, "Dance Points"), (1, "Endless")]
