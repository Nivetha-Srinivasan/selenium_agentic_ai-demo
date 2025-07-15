import subprocess
import traceback
from login_page import run_login_test
from ai_agent import suggest_fix
from git import Repo

def commit_and_push_changes():
    repo = Repo("https://github.com/Nivetha-Srinivasan/selenium_agentic_ai-demo")
    repo.git.add(update=True)
    repo.index.commit("🔧 AI Agent: Applied fix to login test")
    origin = repo.remote(name="origin")
    origin.push()
    print("📤 Changes pushed to GitHub")

def main():
    success = run_login_test()
    if not success:
        error = traceback.format_exc()
        fix = suggest_fix(error)
        print("💡 Suggested fix:", fix)

        # Simulate fix (in real case, modify the script)
        with open("login_test.py", "a") as f:
            f.write(f"\n# AI Suggestion: {fix}\n")

        commit_and_push_changes()

if __name__ == "__main__":
    main()
