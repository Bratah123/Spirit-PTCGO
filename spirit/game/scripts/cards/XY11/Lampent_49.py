"""STUB: effect not implemented — do not guess mechanics.
Lampent (XY11 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="73e05f42-db9e-5351-90a8-0ae8be539e7c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Mirror Mirror",
            game_text="Each player either draws or discards cards until that player has 4 cards in his or her hand. (Your opponent does this first.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flickering Flames",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)