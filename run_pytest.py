# https://github.com/badprog/badprog_leetcode_python

import subprocess
import pathlib
import os
import sys

root = pathlib.Path(__file__).parent # /workspace

# Generator expression
projects = sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("p_")) # [PosixPath('/workspace/p_1_two_sum'), PosixPath('/workspace/p_2_add_two_numbers')] 

# Empty dictionary for future results
results = {}

# Main loop
for proj in projects:
    print(f"\n=== Running Pytest for {proj.name} ===")
    tests = proj / "tests" # tests/ folder

    env = os.environ.copy() # each sub-proj uses its own env
    env["PYTHONPATH"] = str(proj) # need to convert the posix path into a string

    # -v = verbose, display tests name
    # --maxfail=1, stop all other tests from 1 sub-project, if one failed
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v", "--cov=src", "--tb=short", "--maxfail=1", str(tests)],
        env=env
    )
    results[proj.name] = (result.returncode == 0) # store the result of each sub-project True or False
    print("results = {}", results)
    
    # Stop all other tests from next sub-projects, if one test failed
    if not results[proj.name]:
        print(f"\n❌ Pytest failed for {proj.name}, stopping execution.")
        sys.exit(1)
        

# Final result
print("\n=== Pytest Summary ===")
all_ok = True
for name, ok in results.items():
    status = "✅ PASSED" if ok else "❌ FAILED"
    print(f"{name}: {status}")
    if not ok:
        all_ok = False

#
if not all_ok:
    sys.exit(1)
