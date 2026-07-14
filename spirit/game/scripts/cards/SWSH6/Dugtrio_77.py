from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import apply_protection


async def triple_heads(ctx):
    """Flip 3 coins, 60 damage per heads; all heads also shields the user next turn."""
    results = await ctx.flip_coins(3, "Triple Heads")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(60 * heads)
    if heads == 3:
        await apply_protection(ctx, prevent=True, effects_too=True)

card = PokemonCardDef(
    guid="7070e3c5-17cc-51d0-9a79-f938fafb8e1e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Rapid Strike", "Dugtrio"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=77,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Triple Heads",
            game_text="Flip 3 coins. This attack does 60 damage for each heads. If all of them are heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=triple_heads,
        ),
    ],
)