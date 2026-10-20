from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon
from spirit.game.content.definitions import def_for


async def push_down(ctx):
    await ctx.deal_damage()
    opp_active = ctx.opponent_active()
    if opp_active is None or not ctx.opponent_bench() or ctx.effects_blocked(opp_active):
        return
    if await ctx.ask_yes_no("Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


def _scales(calc, carrier):
    return calc.target is carrier_pokemon(carrier) and calc.attacker is not None and _is_ex(calc.attacker)


card = PokemonCardDef(
    guid="89f53a55-ce14-5739-a560-c45f609b0163",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Miraculous Scales",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon-EX.",
            passive=prevent_damage_when(_scales),
        ),
        Attack(
            title="Whirlwind",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=push_down,
        ),
    ],
)