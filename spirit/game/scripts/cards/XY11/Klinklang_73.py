"""STUB: effect not implemented — do not guess mechanics.
Klinklang (XY11 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f760b93-7cb6-52ea-8283-0dadcdcfbd8d",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Heavy Bumper",
            game_text="Any damage done to this Pok\u00e9mon by an opponent's attack is reduced by 10 for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost (after applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gear Spinner",
            game_text="During your next turn, this Pok\u00e9mon's Gear Spinner attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)