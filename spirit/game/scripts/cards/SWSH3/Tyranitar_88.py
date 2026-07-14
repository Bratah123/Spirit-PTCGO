from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack


async def bedrock_breaker(ctx):
    """120 damage, then discard a Stadium in play."""
    await ctx.deal_damage()
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="468abb32-1857-5933-8013-64a5b15d51f7",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Bedrock Breaker",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=bedrock_breaker,
        ),
        Attack(
            title="Mountain Swing",
            game_text="Discard the top 5 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=mill_attack(5, opponent=False),
        ),
    ],
)
