from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    poison_sacs_passive,
    toxic_secretion,
)

card = PokemonCardDef(
    guid="3f49dfd1-db04-5a34-af88-ea711b0bb2af",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Poison Sacs",
            game_text="The Special Condition Poisoned is not removed when your opponent's Pok\u00e9mon evolve or devolve.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=poison_sacs_passive,
        ),
        Attack(
            title="Toxic Secretion",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=toxic_secretion,
        ),
    ],
)