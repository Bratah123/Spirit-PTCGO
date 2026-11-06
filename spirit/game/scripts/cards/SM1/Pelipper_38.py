from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import apply_protection
from spirit.game.session.effects import full_stack


async def _fly_success(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


async def _courier(ctx):
    """Put 1 of your Benched Pokemon and all cards attached to it into your hand."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Put which Benched Pokémon into your hand?")
    if target is not None:
        await ctx.put_in_hand(full_stack(target), reveal=False)


card = PokemonCardDef(
    guid="ae533409-ddf6-5391-ab67-6de377239f51",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=278,
    abilities=[
        Attack(
            title="Courier",
            game_text="Put 1 of your Benched Pok\u00e9mon and all cards attached to it into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_courier,
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_or_nothing(then=_fly_success),
        ),
    ],
)