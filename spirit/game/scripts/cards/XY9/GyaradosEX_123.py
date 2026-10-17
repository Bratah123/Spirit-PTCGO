"""STUB: effect not implemented — do not guess mechanics.
Gyarados-EX (XY9 #123): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54ed1484-3877-5761-81a1-05ae766d0c16",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name",
    display_name="Gyarados-EX",
    searchable_by=["Gyarados-EX", "Basic", "EX", "GyaradosEX"],
    subtypes=["Basic", "EX"],
    collector_number=123,
    set_code="XY9",
    rarity=Rarities.RareSecret,
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