"""STUB: effect not implemented — do not guess mechanics.
Jirachi (DP6 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="51632b0f-9a05-549d-9942-5e50de98c12a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="One Desire",
            game_text="Search your deck for any 1 card. Shuffle your deck, then put that card on top of your deck.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Doom Desire",
            game_text="Discard all Energy attached to Jirachi. The Defending Pok\u00e9mon is Knocked Out at the end of your opponent's next turn.",
            cost={PokemonTypes.METAL: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)