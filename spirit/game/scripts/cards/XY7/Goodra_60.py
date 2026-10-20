"""STUB: effect not implemented — do not guess mechanics.
Goodra (XY7 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1d9b19c-7e4c-5131-b59a-fbde46b87acf",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=60,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Liquid Blow",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each Colorless in its Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shining Breath",
            game_text="During your opponent's next turn, this Pok\u00e9mon can't be affected by any Special Conditions.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)