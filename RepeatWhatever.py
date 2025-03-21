from typing import List, Any

class RepeatWhatever:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "items": ("LIST",),
            }
        }

    RETURN_TYPES = ("ANY",)
    FUNCTION = "process"
    CATEGORY = "RepeatWhatever"

    def process(self, items: List[Any]):
        for item in items:
            yield (item,)

NODE_CLASS_MAPPINGS = {
    "RepeatWhatever": RepeatWhatever
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RepeatWhatever": "🔁 RepeatWhatever"
}