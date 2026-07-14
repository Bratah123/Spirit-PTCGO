from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def adversity_jaws(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None:
        types = defender.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.FIRE.value in types:
            await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="a177fbf6-57a4-5a7b-b119-2ba16d2db4b1",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=184,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=632,
    abilities=[
        Attack(
            title="Adversity Jaws",
            game_text="If your opponent's Active Pok\u00e9mon is a Fire Pok\u00e9mon, it is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=adversity_jaws,
        ),
    ],
)