"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Camerupt (EX4 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import flame_ball
from spirit.game.card_effects.ex import overheat_attach, poke_power_condition

card = PokemonCardDef(
    guid="6e7bed09-cf6c-5b12-b01e-6a10bbeb1ddb",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasCamerupt.Name",
    display_name="Team Magma's Camerupt",
    searchable_by=["Team Magma's Camerupt", "Stage 1", "TeamMagmasCamerupt"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Overheat",
            game_text="Once during your turn (before your attack), you may search your discard pile for a basic Energy card and attach it to Team Magma's Camerupt. Put 2 damage counters on Team Mamga's Camerupt. This power can't be used if Team Magma's Camerupt is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=overheat_attach(),
        ),
        Attack(
            title="Flame Ball",
            game_text="You may move a Fire Energy card attached to Team Magma's Camerupt to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=flame_ball(),
        ),
    ],
)