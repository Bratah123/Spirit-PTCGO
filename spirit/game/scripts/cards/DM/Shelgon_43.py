from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dm import (
    energy_guard_passive,
)

card = PokemonCardDef(
    guid="40c412be-a53f-5d70-85b0-c8b26461de78",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon",
    searchable_by=["Shelgon", "Stage 1", "Shelgon"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Energy Guard",
            game_text="If this Pok\u00e9mon has any basic Energy attached to it, it takes 20 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=energy_guard_passive,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)