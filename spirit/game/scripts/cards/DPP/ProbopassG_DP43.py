"""STUB: effect not implemented — do not guess mechanics.
Probopass G (DPP #DP43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="87122d81-7bbf-5789-b31a-2b4e0f9246c1",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ProbopassG.Name",
    display_name="Probopass G",
    searchable_by=["Probopass G", "Basic", "SP", "ProbopassG"],
    subtypes=["Basic", "SP"],
    collector_number=43,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=476,
    abilities=[
        Attack(
            title="Nose Unit",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon that has any Pok\u00e9-Bodies. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Loud Snort",
            game_text="Probopass G's Retreat Cost is 0 until the end of your next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)