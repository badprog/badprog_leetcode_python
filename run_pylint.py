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
    print(f"\n=== Running Pylint for {proj.name} ===")
    # tests = proj / "tests" # tests/ folder
    all_files = list(proj.glob("src/*.py")) + list(proj.glob("tests/*.py"))
    
    print("all_files = {}", all_files)

    if not all_files:
        print(f"No Python files found in {proj.name}/src or {proj.name}/tests")
        results[proj.name] = False
        sys.exit(1)


    env = os.environ.copy() # each sub-proj uses its own env
    env["PYTHONPATH"] = str(proj) # need to convert the posix path into a string

    # -v = verbose, display names
    result = subprocess.run(
        [sys.executable, "-m", "pylint", "--disable=C,R,W", "--fail-under=8.0", "--verbose", *all_files],
        # [sys.executable, "-m", "pylint", "--output-format=text", "--fail-under=8.0", "--verbose", *all_files],
        env=env,
        capture_output=True, # catch standard and error output
        text=True, # output as strings instead of bytes
    )
    
    #
    print(result.stdout)
    
    #
    if result.stderr:
        print(result.stderr)
    results[proj.name] = (result.returncode == 0) # store the result of each sub-project True or False
    # print("results = {}", results)
    
    # Stop all other tests from next sub-projects, if one test failed
    if not results[proj.name]:
        print(f"\n❌ Pylint failed for {proj.name}, stopping execution.")
        sys.exit(1)
        

# Final result
print("\n=== Pylint Summary ===")
all_ok = True
for name, ok in results.items():
    status = "✅ PASSED" if ok else "❌ FAILED"
    print(f"{name}: {status}")
    if not ok:
        all_ok = False

#
if not all_ok:
    sys.exit(1)
