import random

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def lost_claw(ctx):
    """70. Put a random card from your opponent's hand in the Lost Zone."""
    await ctx.deal_damage()
    hand = ctx.hand(ctx.opponent_id)
    if hand:
        await ctx.move_to_lost_zone([random.choice(hand)])


card = PokemonCardDef(
    guid="b8a98898-af7d-52a3-a682-ab6a0ff76dae",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=359,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Lost Claw",
            game_text="Put a random card from your opponent's hand in the Lost Zone.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=lost_claw,
        ),
    ],
)