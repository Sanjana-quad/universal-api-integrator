def safe_get(d: dict, key: str, default=None):
    return d.get(key, default)
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()
    result.update(dict2)
    return result
def chunk_list(lst: list, chunk_size: int) -> list:
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]