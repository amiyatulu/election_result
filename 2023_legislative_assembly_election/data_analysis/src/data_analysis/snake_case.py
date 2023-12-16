def to_snake_case(text):
    # Replace spaces with underscores
    text = text.replace(' ', '_')
    
    # Replace uppercase letters with lowercase and prepend with underscore
    result = ''.join(['_' + char.lower() if char.isupper() else char for char in text])
    
    # Remove leading underscore (if any)
    result = result.lstrip('_')
    
    return result