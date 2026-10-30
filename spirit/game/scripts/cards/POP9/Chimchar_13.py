"""Chimchar (POP9 #13)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import partner_bonus_condition, pin_missile


card = PokemonCardDef(
    guid="1da86946-0538-5050-ba54-baee23afc99d",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    display_name="Chimchar",
    searchable_by=["Chimchar", "Basic", "Chimchar"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Serial Swipes",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=pin_missile(4, 10)
        ),
        Attack(
            title="Sleepy",
            game_text="If you have Piplup in play, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=partner_bonus_condition('Piplup', 20, SpecialConditions.ASLEEP)
        ),
    ]
)