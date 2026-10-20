"""STUB: effect not implemented — do not guess mechanics.
Pyroar (Promo_XY #XY26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2eeeb7a7-f2be-5a79-bfc3-271ac56b4287",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=668,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Royal Flare",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)