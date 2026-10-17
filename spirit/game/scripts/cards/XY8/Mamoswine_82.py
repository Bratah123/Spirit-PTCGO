"""STUB: effect not implemented — do not guess mechanics.
Mamoswine (XY8 #82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6988e9da-fd28-5a5f-aae6-26263ed0d768",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name",
    display_name="Mamoswine",
    searchable_by=["Mamoswine", "Stage 2", "Mamoswine"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to this Pok\u00e9mon by attacks from your opponent's Fire or Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Primordial Boom",
            game_text="If you have a Stadium card in play, this attack does 40 more damage. If your opponent has a Stadium card in play, heal 40 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)