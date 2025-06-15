def run_division_calculator():
    if len(sys.argv) != 4:
        print("Usage: python main.py divide <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[2]
    denominator = sys.argv[3]
    result = safe_divide(numerator, denominator)
    print(result)