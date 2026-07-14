from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


async def shadow_cyclone(ctx):
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench(), max_count=1)

card = PokemonCardDef(
    guid="e68113fe-632e-5312-90d9-5ef9bd1be86b",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkV.Name",
    display_name="Hisuian Zoroark V",
    searchable_by=["Hisuian Zoroark V", "Basic", "V", "HisuianZoroarkV"],
    subtypes=["Basic", "V"],
    collector_number=146,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=571,
    abilities=[
        Attack(
            title="Void Return",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={},
            damage=30,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Shadow Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=shadow_cyclone,
        ),
    ],
)