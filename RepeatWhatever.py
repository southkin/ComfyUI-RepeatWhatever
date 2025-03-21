import torch
from typing import List, Any

class RepeatWhatever:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "items": ("ANY",),  # 어떤 타입이든 받을 수 있도록 설정
            }
        }

    RETURN_TYPES = ("ANY",)
    FUNCTION = "process"
    CATEGORY = "Custom"

    def process(self, items: List[Any]):
        """
        리스트를 순차적으로 하나씩 반환.
        """
        for item in items:
            yield (item,)

NODE_CLASS_MAPPINGS = {
    "RepeatWhatever": RepeatWhatever
}
