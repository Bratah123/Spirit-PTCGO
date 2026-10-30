"""DP5 Majestic Dawn — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp3_wooper_118_splatter


card = PokemonCardDef(
    guid="84c0199f-af4c-5e46-bfbf-67e35d95532b",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic", "Piplup"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(
            title="Splatter",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1},
            effect=dp3_wooper_118_splatter(),
        ),
    ],
)