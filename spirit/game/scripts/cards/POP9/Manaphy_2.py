"""Manaphy (POP9 #2)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import water_glow_snipe_drain
from spirit.game.card_effects.support_common import look_at_top


card = PokemonCardDef(
    guid="869e9abf-2bda-5596-868b-5f29ed0b1797",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="POP9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Attack(
            title="Dive",
            game_text="Look at the top 7 cards of your deck, choose 1 of them, and put it into your hand. Put the other cards back on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=look_at_top(7, take=1, rest='shuffle')
        ),
        Attack(
            title="Water Glow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Remove from Manaphy the number of damage counters equal to the damage you did to that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=water_glow_snipe_drain(20)
        ),
    ]
)