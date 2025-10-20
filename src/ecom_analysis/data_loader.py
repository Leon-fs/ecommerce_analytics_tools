def load_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def load_excel(file_path):
    import pandas as pd
    return pd.read_excel(file_path)

def load_json(file_path):
    import pandas as pd
    return pd.read_json(file_path)

def load_data(source_type, file_path):
    if source_type == 'csv':
        return load_csv(file_path)
    elif source_type == 'excel':
        return load_excel(file_path)
    elif source_type == 'json':
        return load_json(file_path)
    else:
        raise ValueError("Unsupported data source type. Please use 'csv', 'excel', or 'json'.")