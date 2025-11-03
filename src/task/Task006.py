
"""
Write code to check if a test case passed or failed
expected_title= "Dashboard"
actual_title= "Dashboard"

"""

expected_title = "Dashboard"
actual_title = "dashboard "


if expected_title.strip().lower() == actual_title.strip().lower():
    print("✅ Test Passed: Title Matched")
else:
    print("❌ Test Failed : Title mismatched")