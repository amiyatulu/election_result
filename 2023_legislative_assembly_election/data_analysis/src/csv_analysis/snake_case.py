import re
def to_snake_case(text):
    # Replace multiple spaces with a single underscore using regex
    result = re.sub(r'\s+', '_', text)
    
    # Remove leading underscore (if any)
    result = result.lstrip('_')
    
    return result.lower()

def clean_candidate_name(name):
    # Remove leading number and trailing spaces
    cleaned_name = re.sub(r'^\d+\s*', '', name).rstrip()

    return cleaned_name

