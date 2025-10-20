def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def load_config(config_file):
    """Loads configuration from a given file."""
    import json
    with open(config_file, 'r') as file:
        return json.load(file)

def save_results(results, output_file):
    """Saves results to a specified output file."""
    import json
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)