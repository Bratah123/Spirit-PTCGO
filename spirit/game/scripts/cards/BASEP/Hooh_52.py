from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def sacred_wing(ctx):
    """Flip: heads 60, tails 20 (Sacred Wing)."""
    results = await ctx.flip_coins(1, "Sacred Wing")
    await ctx.deal_damage(60 if results and results[0] else 20)


card = PokemonCardDef(
    guid="85fb2b2f-ba11-51d6-8379-a116872c1f50",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Wing",
            game_text="Flip a coin. If tails, this attack's base damage is 20 instead of 60.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=sacred_wing,
        ),
    ],
)
