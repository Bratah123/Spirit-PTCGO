from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn
from spirit.game.session.effects import full_stack


async def _returning_echo(ctx):
    """60; flip: tails, return this Pokemon and all cards attached to it to your hand."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and not results[0]:
        await ctx.put_in_hand(full_stack(ctx.attacker), reveal=False)


card = PokemonCardDef(
    guid="a934da46-f5cb-56e1-8626-cd0f919ec19b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Wave Amplification",
            game_text="During your next turn, this Pok\u00e9mon's Returning Echo attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(60, attack_title='Returning Echo'),
        ),
        Attack(
            title="Returning Echo",
            game_text="Flip a coin. If tails, return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=_returning_echo,
        ),
    ],
)