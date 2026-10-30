"""DP6 Legends Awakened — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp5_drifloon_61_delivery


card = PokemonCardDef(
    guid="52864342-ec22-59e0-a53a-9be3b9dca6b0",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    display_name="Swinub",
    searchable_by=["Swinub", "Basic", "Swinub"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=220,
    abilities=[
        Attack(
            title="Sniff Out",
            game_text="Flip a coin. If heads, put any 1 card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dp5_drifloon_61_delivery(),
        ),
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)