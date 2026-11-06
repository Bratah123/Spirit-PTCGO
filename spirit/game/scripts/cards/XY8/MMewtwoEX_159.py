from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _vanishing_strike(ctx):
    """150+; with any Stadium in play, +50 and ignores Resistance and effects on the Defending Pokemon."""
    if ctx.stadium_in_play() is None:
        await ctx.deal_damage()
        return
    await ctx.deal_damage(ctx.ability.damage + 50, ignore_resistance=True, ignore_target_effects=True)


card = PokemonCardDef(
    guid="b8b2c1f7-fcfe-5273-9087-70aab8aecd1b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MMewtwoEX.Name",
    display_name="M Mewtwo-EX",
    searchable_by=["M Mewtwo-EX", "MEGA", "EX", "MMewtwoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=159,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Vanishing Strike",
            game_text="If there is any Stadium card in play, this attack does 50 more damage, and this attack's damage isn't affected by Resistance or any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            damage_operator="+",
            effect=_vanishing_strike,
        ),
    ],
)