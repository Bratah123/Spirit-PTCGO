"""Buneary (POP9 #12)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="49c9d931-18cb-5fc0-b3c5-893d1b24caa5",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    display_name="Buneary",
    searchable_by=["Buneary", "Basic", "Buneary"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=427,
    abilities=[
        Attack(
            title="Dizzy Punch",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=2, per_heads=10)
        ),
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to Buneary by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=flip_protection(prevent=True)
        ),
    ]
)