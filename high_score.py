def high_score(score):
    with open ("high_score.txt", "w+") as f:
        f.seek(0)
        high_score = f.read()
        if high_score.strip() == "":
            f.write(str(score))
            return False
        elif int(high_score.strip()) > score:
            f.write(str(score))
            return True