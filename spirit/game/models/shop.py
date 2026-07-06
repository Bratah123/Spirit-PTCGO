from typing import List, Dict, Any, Optional
from spirit.game.models.product import Product, make_shop_sku

class FeaturedProduct:
    """Models a featured product with associated banner URLs."""
    def __init__(self, product_id: str, image_url: str, asset_name: str = ""):
        self.product_id = product_id
        self.image_url = image_url
        self.asset_name = asset_name

    def serialize(self) -> Dict[str, Any]:
        urls = {}
        # Provide all common locales to prevent KeyNotFoundException on client
        for locale in ["en", "de", "fr", "it", "es", "ptb", "en_US", "default"]:
            urls[locale] = [self.image_url, self.asset_name]
        return {
            "productID": self.product_id,
            "urls": urls
        }

class Shop:
    """Models the entire Shop system."""
    def __init__(self):
        self.available_products: Dict[str, Product] = {}
        self.featured_products: List[FeaturedProduct] = []
        self.top_selling_products: List[str] = [] # List of GUIDs
        self.theme_deck_contents: Dict[str, List[str]] = {} # GUID -> List[GUID]
        self.sku_to_pack: Dict[str, str] = {}  # shop SKU GUID -> real collection product GUID

    def add_product(self, product: Product):
        self.available_products[product.guid] = product

    def add_as_sku(self, product: Product) -> Product:
        """Lists a shop-facing SKU alias (own GUID) and remembers the real product it grants.
        Keeps the owned collection GUID out of newArchetypes so it survives shop exit."""
        sku = make_shop_sku(product)
        self.available_products[sku.guid] = sku
        self.sku_to_pack[sku.guid] = product.guid
        return sku

    def resolve_product_guid(self, guid: str) -> str:
        """Maps a shop SKU GUID back to the real product GUID (identity if not a SKU)."""
        return self.sku_to_pack.get(guid, guid)

    def clear(self):
        self.available_products.clear()
        self.featured_products.clear()
        self.top_selling_products.clear()
        self.theme_deck_contents.clear()
        self.sku_to_pack.clear()

    def get_available_guids(self) -> List[str]:
        return list(self.available_products.keys())

    def get_price_map(self) -> Dict[str, Any]:
        return {guid: p.get_price_json() for guid, p in self.available_products.items()}

    def get_new_archetypes(self) -> List[Dict[str, Any]]:
        return [p.to_archetype_json() for p in self.available_products.values()]

    def get_featured_json(self) -> List[Dict[str, Any]]:
        return [fp.serialize() for fp in self.featured_products]

    def get_top_selling_json(self) -> List[Dict[str, Any]]:
        # Top selling is just a list of archetypes the client might not have
        return [self.available_products[guid].to_archetype_json() 
                for guid in self.top_selling_products if guid in self.available_products]
