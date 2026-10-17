"""STUB: effect not implemented — do not guess mechanics.
Xerneas (XY1 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="283fcc93-0244-5f24-a6b6-2b3ec80822f1",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=716,
    abilities=[
        Attack(
            title="Geomancy",
            game_text="Choose 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a Fairy Energy card and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Spear",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)