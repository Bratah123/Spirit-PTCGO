from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _LockedOn(Passive):
    """Attack damage to this Pokemon is increased by 120 (after W/R)."""
    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.amount > 0 and calc.target is carrier_pokemon(carrier):
            calc.amount += 120


async def _lock_on(ctx):
    """The Defending Pokemon can't retreat during the opponent's next turn;
    during your next turn attack damage to it is increased by 120."""
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    ctx.lock_retreat(d)
    ctx.add_passive_through_own_next_turn(d, _LockedOn())


card = PokemonCardDef(
    guid="743a3746-c99a-583f-8c66-5ba0cb80ec23",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ClawitzerBREAK.Name",
    display_name="Clawitzer BREAK",
    searchable_by=["Clawitzer BREAK", "BREAK", "ClawitzerBREAK"],
    subtypes=["BREAK"],
    collector_number=35,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    family_id=692,
    abilities=[
        Attack(
            title="Lock-On",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn. During your next turn, any damage done to that Pok\u00e9mon by attacks is increased by 120 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_lock_on,
        ),
    ],
)