"""DP2 Mysterious Treasures — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import soliciting_nectar


card = PokemonCardDef(
    guid="c3378682-c639-5fd2-bf02-f17dad7ac315",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    display_name="Surskit",
    searchable_by=["Surskit", "Basic", "Surskit"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=283,
    abilities=[
        Attack(
            title="Sleep Inducer",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. The new Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=soliciting_nectar(),
        ),
    ],
)