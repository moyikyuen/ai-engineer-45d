import json
from pathlib import Path

def read_json(path):
    """传入路径，读取 JSON"""
    path = Path(path)
    try:
        with open(path,"r",encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("文件不存在")
        return None
    except json.JSONDecodeError:
        print("JSON 格式错误")
        return None

    except Exception as e:
        print("发生错误：",e)
        return None

    else:
        print("输出成功")
        return data

    finally:
        print("结束")

def write_json(path, data):
    """传入路径和 Python 数据，写入 JSON"""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

