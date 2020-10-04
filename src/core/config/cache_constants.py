
class CacheManagementConstants:

    def __init__(self):
        self.elevation_item_cache_config = ElevationItemCacheConfig()

class ElevationItemCacheConfig:
    key = "elevation_"
    expires = 86400
