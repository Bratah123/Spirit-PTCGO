from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per


async def shadow_cyclone(ctx):
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench(), max_count=1)


def _both_actives_energy(ctx):
    total = 0
    for p in (ctx.attacker, ctx.defender):
        if p is not None:
            total += len(ctx.attached_energies(p))
    return total


card = PokemonCardDef(
    guid="d62e3e34-f82d-587c-b12e-4a9f1a8d08b8",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalEX.Name",
    display_name="Yveltal-EX",
    searchable_by=["Yveltal-EX", "Basic", "EX", "YveltalEX"],
    subtypes=["Basic", "EX"],
    collector_number=144,
    set_code="XY1",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Evil Ball",
            game_text="This attack does 20 more damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(_both_actives_energy, 20, base=20),
        ),
        Attack(
            title="Y Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=shadow_cyclone,
        ),
    ],
)