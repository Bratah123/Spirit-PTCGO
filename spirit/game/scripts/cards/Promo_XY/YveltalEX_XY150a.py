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
    guid="7081745d-fdcf-53ee-92a1-cef9064d55bc",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalEX.Name",
    display_name="Yveltal-EX",
    searchable_by=["Yveltal-EX", "Basic", "EX", "YveltalEX"],
    subtypes=["Basic", "EX"],
    collector_number=213,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
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