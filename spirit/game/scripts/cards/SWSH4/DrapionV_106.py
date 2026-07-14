from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def hazardous_claws(ctx):
    await ctx.discard_energy_from(ctx.attacker, 2)
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="a3c8239a-9cab-5b89-8e23-57b72bd6ccfc",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionV.Name",
    display_name="Drapion V",
    searchable_by=["Drapion V", "Basic", "V", "DrapionV"],
    subtypes=["Basic", "V"],
    collector_number=106,
    set_code="SWSH4",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=452,
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Hazardous Claws",
            game_text="Discard 2 Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=hazardous_claws,
        ),
    ],
)