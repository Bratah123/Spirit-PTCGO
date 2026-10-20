from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


async def _purifying_flame(ctx):
    """Printed damage; remove all Special Conditions from this Pokemon."""
    await ctx.deal_damage()
    await ctx.cure_all_conditions(ctx.attacker)


def _named(pokemon, name):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return getattr(d, "display_name", "") == name


card = PokemonCardDef(
    guid="4c650db8-5a77-5431-8c39-a94d5dbddf06",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic", "Reshiram"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Purifying Flame",
            game_text="Remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_purifying_flame,
        ),
        Attack(
            title="Fusion Flare",
            game_text="If Zekrom is on your Bench, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: any(_named(p, "Zekrom") for p in ctx.my_bench()), 40),
        ),
    ],
)