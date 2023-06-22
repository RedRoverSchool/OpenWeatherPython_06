from __future__ import annotations
from pydantic import ValidationError


def validator_pydantic(data, model):
    try:
        model.update_forward_refs()
        validated_data = model(**data)
    except ValidationError as e:
        print(e)
        raise Exception("API response is incorrect")
    else:
        return validated_data
