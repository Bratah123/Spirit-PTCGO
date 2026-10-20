from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive


async def _six_feet_under(ctx):
    """Once during your turn, you may Knock Out this Pokemon. If you do, put 3
    damage counters on your opponent's Pokemon in any way you like."""
    if await ctx.knock_out(ctx.source):
        await ctx.place_damage_counters(3)


class _MisfortunePassive(Passive):
    """During the opponent's next turn, every coin they flip is tails."""

    def forces_coin_tails(self, player_id, carrier):
        return player_id != carrier.owning_player_id


async def _slap_of_misfortune(ctx):
    """Printed damage; whenever your opponent flips a coin during their next
    turn, treat it as tails. (Rides on this Pokemon as a temporary passive.)"""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _MisfortunePassive())


card = PokemonCardDef(
    guid="c1fc68e0-bf75-58f5-b996-62812748985a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Team Plasma", "Cofagrigus"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=56,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Six Feet Under",
            game_text="Once during your turn (before your attack) you may Knock Out this Pok\u00e9mon. If you do, put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=_six_feet_under,
        ),
        Attack(
            title="Slap of Misfortune",
            game_text="Whenever your opponent flips a coin during his or her next turn, treat it as tails.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=_slap_of_misfortune,
        ),
    ],
)