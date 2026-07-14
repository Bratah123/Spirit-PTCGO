from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import (
    ability_lock_passive,
    is_in_active_spot,
    opposing_pokemon,
)


def _neutralizing_gas_target(pokemon, carrier):
    return opposing_pokemon(pokemon, carrier) and is_in_active_spot(carrier)


card = PokemonCardDef(
    guid="bceaefbe-6be9-54ab-87a0-675ff554bf50",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianWeezing.Name",
    display_name="Galarian Weezing",
    searchable_by=["Galarian Weezing", "Stage 1", "GalarianWeezing"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH45",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Neutralizing Gas",
            game_text="As long as this Pokémon is in the Active Spot, your opponent's Pokémon in play have no Abilities, except for Neutralizing Gas.",
            passive=ability_lock_passive(_neutralizing_gas_target),
        ),
        Attack(
            title="Severe Poison",
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 4 damage counters instead of 1 on that Pokémon during Pokémon Checkup.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, counters=4),
        ),
    ],
)
