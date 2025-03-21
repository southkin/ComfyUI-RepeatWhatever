# __init__.py
import os
import sys
sys.path.append(os.path.dirname(__file__))

try:
    from RepeatWhatever import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except Exception as e:
    print("❌ RepeatWhatever 로딩 실패")
    print(e)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']