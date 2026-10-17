"""STUB: effect not implemented — do not guess mechanics.
Florges-EX (XY4 #116): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03f7a0e9-3f22-5771-ae19-dbe5c94384cf",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesEX.Name",
    display_name="Florges-EX",
    searchable_by=["Florges-EX", "Basic", "EX", "FlorgesEX"],
    subtypes=["Basic", "EX"],
    collector_number=116,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=671,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bright Garden",
            game_text="This attack does 20 damage times the number of Grass Pok\u00e9mon and Fairy Pok\u00e9mon you have in play.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)