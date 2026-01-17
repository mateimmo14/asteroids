import os
import sys

def get_high_score_path():
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller executable
        base_path = os.path.dirname(sys.executable)  # folder of the exe
    else:
        # Running as script
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, "high_score.txt")

def high_score(score,tank=False,hard=False):
    with open (get_high_score_path(), "w+") as f:
        f.seek(0)
        high_score = f.read()
        if high_score.strip() == "":
            if tank:
                score *= 1.5
            if hard:
                score *= 2
            f.write(str(score))
            return False
        elif int(high_score.strip()) > score:
            f.write(str(score))
            return True