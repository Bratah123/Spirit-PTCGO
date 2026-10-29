from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    harmonics_passive,
)

card = PokemonCardDef(
    guid="6666eb92-1c45-553f-8d1f-0b73aa85f4ff",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primarina.Name",
    display_name="Primarina",
    searchable_by=["Primarina", "Stage 2", "Primarina"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=728,
    abilities=[
        Ability(
            title="Harmonics",
            game_text="Whenever you attach an Energy card from your hand to 1 of your Pok\u00e9mon, except with an attack, Ability, or Trainer card, attach up to 2 Energy cards to that Pok\u00e9mon instead of 1.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=harmonics_passive
        ),
        Attack(
            title="Hypno Splash",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)