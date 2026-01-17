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
