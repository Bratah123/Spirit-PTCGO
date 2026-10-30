"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Lanturn (EX4 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import auxiliary_light, poke_power_condition

card = PokemonCardDef(
    guid="2740d15d-f303-58be-9d0e-c52f8e91c460",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasLanturn.Name",
    display_name="Team Aqua's Lanturn",
    searchable_by=["Team Aqua's Lanturn", "Stage 1", "TeamAquasLanturn"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasChinchou.Name",
    family_id=170,
    abilities=[
        Ability(
            title="Auxiliary Light",
            game_text="Once during your turn (before your attack), you may attach a basic Energy card from your hand to Team Aqua's Lanturn. Put 2 damage counters on Team Aqua's Lanturn. This power can't be used if Team Aqua's Lanturn is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=auxiliary_light(),
        ),
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)