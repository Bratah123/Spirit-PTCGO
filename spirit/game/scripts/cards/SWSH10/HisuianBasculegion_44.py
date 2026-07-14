from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _grudge_dive(ctx):
    if ctx.kos_suffered_last_turn() > 0:
        await ctx.deal_damage(120)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    else:
        await ctx.deal_damage(30)

card = PokemonCardDef(
    guid="867c3aa1-5afc-5774-9c6a-4be592e4bdc5",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculegion.Name",
    display_name="Hisuian Basculegion",
    searchable_by=["Hisuian Basculegion", "Stage 1", "HisuianBasculegion"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    family_id=550,
    abilities=[
        Attack(
            title="Grudge Dive",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack from your opponent's Pok\u00e9mon during their last turn, this attack does 90 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="+",
            effect=_grudge_dive,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)