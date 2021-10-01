from typing import List


def destCity(self, paths: List[List[str]]) -> str:
    """
    哈希表
    根据终点站的定义，终点站不会出现在 cityA 中，因为存在从 cityA 出发的线路，所以终点站只会出现在 cityB 中。
    据此，我们可以遍历 cityB，返回不在 cityA 中的城市，即为答案。
    """
    city_a = {path[0] for path in paths}
    for path in paths:
        if path[1] not in city_a:
            return path[1]
    