import torch
from typing import List, Any

class RepeatWhatever:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "items": ("ANY",),  # 모든 타입을 받도록 설정
            }
        }

    RETURN_TYPES = ("ANY",)
    FUNCTION = "process"
    CATEGORY = "Custom"

    def process(self, items: List[Any]):
        """
        리스트에서 요소를 하나씩 반환.
        """
        for item in items:
            yield (item,)

# ✅ ComfyUI가 인식할 수 있도록 노드 등록
NODE_CLASS_MAPPINGS = {
    "RepeatWhatever": RepeatWhatever
}

# ✅ 선택 사항: 노드를 특정 카테고리에 표시
NODE_DISPLAY_NAME_MAPPINGS = {
    "RepeatWhatever": "🌀 Repeat Whatever"
}
