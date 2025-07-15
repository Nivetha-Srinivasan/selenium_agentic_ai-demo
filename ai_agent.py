def suggest_fix(error_message):
    print("🤖 AI Agent analyzing error...")
    if "no such element" in error_message:
        return "Try updating the element ID or selector."
    return "Check credentials or page load timing."
