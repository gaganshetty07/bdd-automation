import os
import shutil
import subprocess

def run_tests():
    reports_dir = "reports"
    screenshots_dir = "screenshots"

    # Ensure the reports and screenshots directories are clean
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
    os.makedirs(reports_dir)

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    print("Running BDD tests...")
    result = subprocess.run(["behave"], shell=True)

    if result.returncode == 0:
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Check reports for details.")

if __name__ == "__main__":
    run_tests()
