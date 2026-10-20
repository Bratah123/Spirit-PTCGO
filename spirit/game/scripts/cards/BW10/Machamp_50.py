from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand, bonus_if, has_tool


async def knock_off(ctx):
    """discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="bb956d45-f8a7-528e-8460-56c212d438bb",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=knock_off,
        ),
        Attack(
            title="Reinforced Lariat",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: has_tool(ctx.attacker), 40),
        ),
    ],
)