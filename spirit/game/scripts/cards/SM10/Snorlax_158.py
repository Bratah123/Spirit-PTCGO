from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    big_counter,
    lazy_eating,
)

card = PokemonCardDef(
    guid="df6622f5-283b-5337-ba43-18b5438d7d96",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Lazy Eating",
            game_text="Between turns, heal 10 damage from this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=lazy_eating
        ),
        Attack(
            title="Big Counter",
            game_text="If your opponent's Active Pok\u00e9mon is a TAG TEAM, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=big_counter
        ),
    ],
)