"""STUB: effect not implemented — do not guess mechanics.
Gyarados-EX (XY9 #114): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8179ebd4-038b-5229-b7f1-09031b229ceb",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name",
    display_name="Gyarados-EX",
    searchable_by=["Gyarados-EX", "Basic", "EX", "GyaradosEX"],
    subtypes=["Basic", "EX"],
    collector_number=114,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=130,
    abilities=[
        Attack(
            title="Stormy Seas",
            game_text="Flip a coin until you get tails. For each heads, search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Splash Burn",
            game_text="This attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)