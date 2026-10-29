"""STUB: effect not implemented — do not guess mechanics.
Shining Genesect (SL #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.sl import energy_reload, energy_reload_condition

card = PokemonCardDef(
    guid="c2ab2388-8d93-5255-9415-d669e729b781",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningGenesect.Name",
    display_name="Shining Genesect",
    searchable_by=["Shining Genesect", "Basic", "ShiningGenesect"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SL",
    rarity=Rarities.Shining,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Ability(
            title="Energy Reload",
            game_text="Once during your turn (before your attack), you may move a Grass Energy from 1 of your other Pok\u00e9mon to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=energy_reload_condition,
            effect=energy_reload,
        ),
        Attack(
            title="Gaia Blaster",
            game_text="This attack does 20 more damage times the amount of Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.GRASS), 20, base=50),
        ),
    ],
)