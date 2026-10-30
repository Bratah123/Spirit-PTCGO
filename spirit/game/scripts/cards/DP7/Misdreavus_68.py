"""STUB: effect not implemented — do not guess mechanics.
Misdreavus (DP7 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="27e88686-3359-53e8-a2a8-d0feddc0fbc1",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic", "Misdreavus"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=200,
    abilities=[
        Attack(
            title="Lullaby",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Nightmare Feast",
            game_text="If the Defending Pok\u00e9mon is Asleep, this attack does 50 damage and remove 5 damage counters from Misdreavus. If the Defending Pok\u00e9mon is not Asleep, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)