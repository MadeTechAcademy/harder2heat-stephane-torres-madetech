def attribute_factory(desired_attribute: str, building_properties: dict) -> dict:
    value = building_properties.get(desired_attribute, False)
    if value == False:
        raise AttributeError(f'Attribute {desired_attribute} not found')
    return {desired_attribute: value}