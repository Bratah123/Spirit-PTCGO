from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.content.definitions import def_for


def _named(card, *names):
    d = def_for(card.archetype_id)
    return getattr(d, "display_name", None) in names


async def _tag_team_spark(ctx):
    """20 more for each Energy attached to your Magmortar."""
    counts = [len(ctx.attached_energies(p)) for p in ctx.my_pokemon_in_play()
              if _named(p, "Magmortar")]
    await ctx.deal_damage(20 + 20 * (max(counts) if counts else 0))


async def _gigavolt(ctx):
    """60; heads +30, tails the opponent's Active is now Paralyzed."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    heads = bool(results and results[0])
    await ctx.deal_damage(90 if heads else 60)
    if not heads and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="4a7715e0-3b88-57d1-922c-286d5a6df451",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Tag Team Spark",
            game_text="This attack does 20 more damage for each Energy attached to your Magmortar.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=_tag_team_spark,
        ),
        Attack(
            title="Gigavolt",
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_gigavolt,
        ),
    ],
)