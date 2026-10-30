from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    draw_if_opponent_evolved,
    eclipse_type_change,
    named_partner_condition,
)


card = PokemonCardDef(
    guid="aa4ce394-efcf-5732-a423-a8a6ca5bb26b",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Solar Eclipse",
            game_text="Once during your turn (before your attack), if Lunatone is in play, you may use this power. Until the end of your turn, Solrock's type is Fire. This power can't be used if Solrock is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=named_partner_condition("Lunatone"),
            effect=eclipse_type_change(PokemonTypes.FIRE),
        ),
        Attack(
            title="Cosmic Draw",
            game_text="If your opponent has any Evolved Pok\u00e9mon in play, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_if_opponent_evolved(3),
        ),
        Attack(
            title="Solar Blast",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
