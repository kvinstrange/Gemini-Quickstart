import os

# Manually set the API key in the script
os.environ["GEMINI_API_KEY"] = "AIzaSyBH9Tq1e3A2f5OMSXV6y8sTPG6F5xK_ZBQ"  # Replace with your actual API key
print(os.getenv("GEMINI_API_KEY"))  # This should now print the API key
