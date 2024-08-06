def attribute_factory(desired_attribute: str, building_properties: dict) -> dict:
    value = building_properties.get(desired_attribute, None)
    if value == None:
        raise AttributeError(f'Attribute {desired_attribute} not found')
    return {desired_attribute: value}