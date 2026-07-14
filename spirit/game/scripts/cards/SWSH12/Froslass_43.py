from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


def _played_candice(ctx):
    return ctx.played_trainer_this_turn("Candice") > 0


async def frosty_jail(ctx):
    """20+. If Candice was played from hand this turn, +90 damage and the
    opponent's Active Pokemon is now Paralyzed."""
    boosted = _played_candice(ctx)
    await ctx.deal_damage(110 if boosted else 20)
    if boosted:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="02297fec-5e45-54b1-a3d6-7b0fcd4eaf19",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Frosty Jail",
            game_text="If you played Candice from your hand during this turn, this attack does 90 more damage, and your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="+",
            effect=frosty_jail,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
