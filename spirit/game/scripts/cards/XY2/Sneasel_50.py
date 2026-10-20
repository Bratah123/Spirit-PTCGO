from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _flash_claw(ctx):
    """Your opponent discards a card from their hand."""
    if ctx.hand(ctx.opponent_id):
        await ctx.discard_from_hand(1, minimum=1, player_id=ctx.opponent_id,
                                    prompt="Choose a card to discard")


card = PokemonCardDef(
    guid="6f2860af-3ec0-5796-9f67-db5c1ca8f9bd",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=215,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flash Claw",
            game_text="Your opponent discards a card from his or her hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=_flash_claw,
        ),
    ],
)