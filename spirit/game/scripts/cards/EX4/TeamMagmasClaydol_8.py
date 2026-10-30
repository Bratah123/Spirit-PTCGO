"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Claydol (EX4 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.ex import magma_switch, poke_power_condition

card = PokemonCardDef(
    guid="2227965d-f845-5ff4-af4b-1284ebe843fd",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasClaydol.Name",
    display_name="Team Magma's Claydol",
    searchable_by=["Team Magma's Claydol", "Stage 1", "TeamMagmasClaydol"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Magma Switch",
            game_text="Once during your turn (before your attack), you may move an Energy card attached to your Pok\u00e9mon with Team Magma in its name to another of your Pok\u00e9mon. This power can't be used if Team Magma's Claydol is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=magma_switch(),
        ),
        Attack(
            title="Dark Hand",
            game_text="If you have more cards in your hand than your opponent, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(lambda ctx: ctx.hand_size(ctx.player_id) > ctx.hand_size(ctx.opponent_id), 20),
        ),
    ],
)