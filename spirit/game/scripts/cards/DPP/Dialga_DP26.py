"""DP4 Great Encounters — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.dp import flash_cannon_devolve


card = PokemonCardDef(
    guid="6d8adb61-40d7-5926-a140-b3ef8fe3e3c6",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Time Bellow",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=draw_attack(1),
        ),
        Attack(
            title="Flash Cannon",
            game_text="You may return all Energy cards attached to Dialga to your hand. If you do, remove the highest Stage Evolution card from the Defending Pok\u00e9mon and shuffle that card into your opponent's deck.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=flash_cannon_devolve(),
        ),
    ],
)