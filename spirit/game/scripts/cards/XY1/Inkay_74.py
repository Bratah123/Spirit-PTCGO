"""STUB: effect not implemented — do not guess mechanics.
Inkay (XY1 #74): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed0be64c-c5c0-58ef-8f90-847e563c0c78",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic", "Inkay"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=686,
    abilities=[
        Ability(
            title="Upside-Down Evolution",
            game_text="Once during your turn, (before your attack), if this Pok\u00e9mon is Confused, you may search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Confusion Wave",
            game_text="Both Active Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)