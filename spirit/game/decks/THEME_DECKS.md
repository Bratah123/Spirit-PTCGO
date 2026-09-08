# Scripted deck products

Create a `.py` file anywhere under `spirit/game/scripts/products/` and export a
`product` object. No central registration list or packet-handler change is needed.

The repository includes one active reference product:
[Water Practice](../scripts/products/custom/water_practice.py). It loads automatically
and demonstrates `ThemeDeckDef`, `DeckEntry`, product metadata, artwork selection,
and explicit Theme eligibility using cards already included in the repository.

| Water Practice | Contents |
| --- | --- |
| Pokemon | 16, featuring the Sobble and Chewtle evolution lines |
| Trainers | 22 |
| Basic Water Energy | 22 |
| Product GUID | `6ade6e18-f382-42bd-a2ea-18244f23f8f4` |

Copy that script to a new filename, assign a new unique product GUID, and edit its
name, description and contents to create your own deck. `key="CUSTOM_DECKS"` groups
these products; multiple deck products may share the key, but each needs its own GUID.

## API

| API | Behavior |
| --- | --- |
| `DeckEntry(card, count=1)` | A card GUID or `SET/collector_number` reference and its quantity |
| `ThemeDeckDef(..., contents=[...], theme_legal=True)` | A fixed deck product whose exact list is approved for Theme play |
| `DeckDef(..., contents=[...])` | A fixed deck product without Theme eligibility |
| `resolve_contents(card_registry)` | Returns the expanded list of card GUIDs |
| `validate_definition(card_registry)` | Returns readable definition errors; an empty list means valid |

Both definition classes accept the usual product `guid`, `key`, `name`,
`catalog_id`, and extra `attributes`, plus optional `description` and `image_name`.
`image_url` remains supported; choose either it or `image_name`.

The loader checks valid, unique product GUIDs, known and unambiguous card references,
positive integer quantities, exactly 60 cards, at least one Basic Pokemon, and the
four-copy name limit. Basic Energy is exempt from the copy limit. Multiple printings
with the same set and collector number require an explicit GUID.

The Theme format is available automatically. A saved deck qualifies only when its
card GUIDs and quantities match an approved list. Card order and GUID letter case
do not matter; changing a printing or quantity removes eligibility. Normal
validation still applies, including ownership where the caller requests it. Theme
matchmaking also rejects invalid lists.

## Validate and install

Run `python -m spirit.tools.check_products` from the repository root. It validates
the complete catalog and prints the loaded deck products. To check a separate
script directory, add `--scripts-dir <directory>`.

Water Practice uses `image_name="_default_deckbox"`, backed by the bundled
`spirit/assets/products/custom_pcds/_default_deckbox.png`. For custom artwork, add
a PNG to that directory and set `image_name` to its lowercase basename without
the extension. The existing asset pipeline builds the `pcdBoxes` bundle on startup.
Restart the server after adding product scripts or artwork, then reconnect the client.

Use the admin dashboard's Shop tab to enable the product GUID and configure its
price, currency and featured status. Deck definitions do not automatically add shop
listings. Existing code redemption and collection-grant APIs can grant the same GUID.

Opening an owned deck consumes one product and grants its exact card quantities in
one database transaction. Cards inherit the consumed product's tradability;
nontradable copies are consumed first. The same transaction creates a saved deck.
Reopening the product grants the cards again and preserves the existing saved copy,
including player edits. Opening pushes updated collection and deck-list payloads.

The contents preview uses the same resolved list as opening and validation. Attribute
201640 is encoded as a Protobuf UUID so the client constructs its required
`ArchetypeID`. Shop aliases retain that real-product reference, so previewing does
not depend on the shop alias GUID.

## Reloads and retiring products

Server code can call `reload_products()` from `spirit.packets.handlers.data_sync`.
A successful load replaces the catalog and invalidates the shop and derived payload
caches. A broken script rejects the entire new catalog and retains the previous
one. `ProductLoader.load_all(strict=True)` raises a detailed error for tooling.
Already connected clients may need to reconnect to refresh their cached archetypes.

Set `theme_legal=False` to retire a Theme deck while preserving its preview and
opening behavior. Disabling its shop listing only affects purchasing, not Theme
eligibility. Keep published products available for accounts that still own unopened
copies; use a new product GUID when publishing a different card list.
