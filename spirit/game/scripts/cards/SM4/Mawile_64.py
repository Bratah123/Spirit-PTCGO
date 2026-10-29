from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


async def cut_down(ctx):
    """Printed damage; flip a coin, heads: discard an Energy from the opponent's Active."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Muddy Acid")
    if not heads[0]:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose an Energy to discard from the Defending Pokémon.",
    )


card = PokemonCardDef(
    guid="9ed86894-e067-5366-bd7b-538d9e2e61fa",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=303,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=cut_down,
        ),
    ],
)