from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


class _DiamondForce(Passive):
    """During the opponent's next turn, while this Pokemon stays Active,
    prevent all damage done to your Pokemon by the opponent's Pokemon-EX."""
    def prevents_damage(self, calc, carrier):
        me = carrier_pokemon(carrier)
        att, target = calc.attacker, calc.target
        return bool(me is not None and is_in_active_spot(me) and calc.is_attack
                    and att is not None and target is not None
                    and att.owning_player_id != me.owning_player_id
                    and target.owning_player_id == me.owning_player_id and _is_ex(att))


async def _diamond_force(ctx):
    """100; shield your team from the opponent's Pokemon-EX next turn."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _DiamondForce())


card = PokemonCardDef(
    guid="95586126-4fb8-5120-b2f9-fdd654e1e119",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MDiancieEX.Name",
    display_name="M Diancie-EX",
    searchable_by=["M Diancie-EX", "MEGA", "EX", "MDiancieEX"],
    subtypes=["MEGA", "EX"],
    collector_number=44,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name",
    family_id=719,
    abilities=[
        Attack(
            title="Diamond Force",
            game_text="During your opponent's next turn, prevent all damage done to each of your Pok\u00e9mon from your opponent's Pok\u00e9mon-EX. (If this Pok\u00e9mon is no longer your Active Pok\u00e9mon, this effect ends.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_diamond_force,
        ),
    ],
)