"""STUB: effect not implemented — do not guess mechanics.
Pangoro (Promo_XY #XY50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcff5285-5bf5-58ff-811c-ecc1b0c9719e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1", "Pangoro"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=675,
    abilities=[
        Ability(
            title="Benevolent Boss",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, it gets +20 HP for each of your Benched Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crazy Knuckle",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)