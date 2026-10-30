"""Rotom (POP9 #5)."""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import poltergeist, type_shift_to_psychic


card = PokemonCardDef(
    guid="36343edc-1390-5d2f-9538-dc9bbdc8404f",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="POP9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Ability(
            title="Type Shift",
            game_text="Once during your turn (before your attack), you may use this power. Rotom's type is Psychic until the end of your turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            effect=type_shift_to_psychic()
        ),
        Attack(
            title="Poltergeist",
            game_text="Look at your opponent's hand. This attack does 30 damage plus 10 more damage for each Trainer, Supporter, and Stadium card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=poltergeist(30, 10)
        ),
    ]
)