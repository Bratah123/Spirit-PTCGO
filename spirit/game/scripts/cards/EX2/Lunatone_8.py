from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    draw_if_opponent_evolved,
    eclipse_type_change,
    named_partner_condition,
)


card = PokemonCardDef(
    guid="f406b8a7-d272-51fa-b846-64a5020396c9",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=337,
    abilities=[
        Ability(
            title="Lunar Eclipse",
            game_text="Once during your turn (before your attack), if Solrock is in play, you may use this power. Until the end of your turn, Lunatone's type is Darkness. This power can't be used if Lunatone is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=named_partner_condition("Solrock"),
            effect=eclipse_type_change(PokemonTypes.DARKNESS),
        ),
        Attack(
            title="Cosmic Draw",
            game_text="If your opponent has any Evolved Pok\u00e9mon in play, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_if_opponent_evolved(3),
        ),
        Attack(
            title="Lunar Blast",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
