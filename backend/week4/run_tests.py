import subprocess

def run_tests():
    result = subprocess.run(['python', 'manage.py', 'test', 'week4.tests.test_integration'], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Tests failed. Potential regression detected.")
    else:
        print("All tests passed. No regressions detected.")

if __name__ == "__main__":
    run_tests()