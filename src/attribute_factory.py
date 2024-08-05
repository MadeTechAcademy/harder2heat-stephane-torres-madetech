def attribute_factory(desired_attribute: str, building_properties: dict) -> dict:
    return {desired_attribute: building_properties.get(desired_attribute)}