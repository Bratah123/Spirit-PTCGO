from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import psychic_60_plus
from spirit.game.card_effects.sm7 import (
    shadow_shield_passive,
)


card = PokemonCardDef(
    guid="50280326-6540-5fd4-9c09-e71bd2617609",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala",
    searchable_by=["Lunala", "Stage 2", "Lunala"],
    subtypes=["Stage 2"],
    collector_number=70,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=792,
    abilities=[
        Ability(
            title="Shadow Shield",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=shadow_shield_passive,
        ),
        Attack(
            title="Full Moon Ray",
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=psychic_60_plus,
        ),
    ],
)