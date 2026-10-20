from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_damage


async def _hypno_headbutt(ctx):
    """60; you may do 30 more damage. If you do, this Pokemon is now Asleep."""
    if await ctx.ask_yes_no("Do 30 more damage? If you do, this Pokémon is now Asleep."):
        await ctx.deal_damage(90)
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    else:
        await ctx.deal_damage(60)


card = PokemonCardDef(
    guid="3f0e703b-e730-595d-97a6-e82c46e11947",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Attack(
            title="Double Headbutt",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Hypno Headbutt",
            game_text="You may do 30 more damage. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=_hypno_headbutt,
        ),
    ],
)