from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


async def _slap_of_misfortune(ctx):
    """Printed damage; whenever your opponent flips a coin during their next
    turn, treat it as tails. (Rides on this Pokemon as a temporary passive.)"""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _MisfortunePassive())


class _MisfortunePassive(Passive):
    """During the opponent's next turn, every coin they flip is tails."""

    def forces_coin_tails(self, player_id, carrier):
        return player_id != carrier.owning_player_id


card = PokemonCardDef(
    guid="242a8992-2fdb-57bf-8e56-8915dd4da213",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Sinister Suggestion",
            game_text="Whenever your opponent flips a coin during his or her next turn, treat it as tails.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_slap_of_misfortune,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
        ),
    ],
)