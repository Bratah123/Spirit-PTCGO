from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    electricannon,
    stealthy_body_passive,
)

card = PokemonCardDef(
    guid="f95a8fbe-8c31-57a7-bebf-37bda0203f3c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Ability(
            title="Stealthy Body",
            game_text="If there is any Stadium card in play, this Pok\u00e9mon has no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=stealthy_body_passive
        ),
        Attack(
            title="Electricannon",
            game_text="You may discard all Lightning Energy from this Pok\u00e9mon. If you do, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=electricannon
        ),
    ],
)