"""STUB: effect not implemented — do not guess mechanics.
Shelgon (EX3 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import energy_guard_passive

card = PokemonCardDef(
    guid="2e0cff27-d6bd-570b-a351-c5c15cfbb9ee",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon",
    searchable_by=["Shelgon", "Stage 1", "Shelgon"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Energy Guard",
            game_text="As long as Shelgon has any basic Energy cards attached to it, damage done to Shelgon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=energy_guard_passive(10),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)