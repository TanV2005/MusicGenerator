def apply_prompt_settings(prompt):
    settings = {
        "temperature": 0.8
    }

    prompt = prompt.lower()

    if "happy" in prompt:
        settings["temperature"] = 1.1
    elif "sad" in prompt:
        settings["temperature"] = 0.5
    elif "energetic" in prompt:
        settings["temperature"] = 1.3
    elif "calm" in prompt:
        settings["temperature"] = 0.6

    return settings