from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def shatter(ctx):
    """20 damage, then discard a Stadium in play."""
    await ctx.deal_damage()
    await ctx.discard_stadium()

card = PokemonCardDef(
    guid="c7c4b87d-f07b-5a0c-9485-cb50203669fb",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    display_name="Vigoroth",
    searchable_by=["Vigoroth", "Stage 1", "Single Strike", "Vigoroth"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=130,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    family_id=287,
    abilities=[
        Attack(
            title="Shatter",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=shatter,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)