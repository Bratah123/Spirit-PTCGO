"""Turtwig (POP9 #17)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import heal_self_after_damage, partner_bonus_condition


card = PokemonCardDef(
    guid="74e3b07c-b275-5d6c-b911-ad816cbca154",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=387,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Remove 1 damage counter from Turtwig.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=heal_self_after_damage(1)
        ),
        Attack(
            title="Parboil",
            game_text="If you have Chimchar in play, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=partner_bonus_condition('Chimchar', 20, SpecialConditions.BURNED)
        ),
    ]
)