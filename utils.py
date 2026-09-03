import json
from pathlib import Path

def multiply(a, b):
    return a * b

def read_json(path):
    """传入路径，读取json"""
    path = Path(path)

    try:
        with open(path, 'r',encoding="utf-8") as f:
            data =  json.load(f)

    except FileNotFoundError:
        print("文件不存在")
    except json.JSONDecodeError:
        print("JSON 格式错误")
    else:
        return data
    finally:
        print("结束")

def write_json(path, data):
    """传入目标路径和python数据写入JSON文件"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w',encoding= "utf-8") as f:
        json.dump(data, f,ensure_ascii=False, indent=4)