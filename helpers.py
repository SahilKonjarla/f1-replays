import sys

class Helpers:
    def __init__(self):
        pass

    def print_usage(self):
        print("""
        Usage: python app.py [OPTIONS]
    
        Options:
          --year,  -y  <YEAR>           Specify the season year (default: 2025)
          --round, -ro <ROUND>          Specify the round number (default: 1)
    
          --sprint-qualifying, -sq   Use Sprint Qualifying session (SQ)
          --sprint, -s               Use Sprint session (S)
          --qualifying, -q           Use Qualifying session (Q)
          --race, -r                 Use Race session (R)
    
        Examples:
          python run.py --year 2023 --round 5 --qualifying
          python run.py -sq --year 2024 -ro 8
          python run.py -ro -y -r
          python run.py --round 14 -q --year 2021
        """
        )

    def safe_flag(self, args, flag):
        if flag not in args:
            return None

        idx = args.index(flag)
        if idx + 1 >= len(args):
            return None

        value = args[idx + 1]

        if value.lstrip("-").isdigit():
            return int(value)

        return None