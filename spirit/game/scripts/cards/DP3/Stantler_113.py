"""STUB: effect not implemented — do not guess mechanics.
Stantler (DP3 #113): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a73d1705-7638-5471-ab36-7a9b2d488b6f",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Frighten Horn",
            game_text="If the Defending Pok\u00e9mon isn't an Evolved Pok\u00e9mon, that Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)