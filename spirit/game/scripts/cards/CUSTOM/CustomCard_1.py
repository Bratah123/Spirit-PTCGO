from spirit.game.data_utils import PokemonCardDef, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import EffectContext

async def set_up(ctx: EffectContext):
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)

card = PokemonCardDef(
    guid="ee872288-f81c-4444-465a-42bc8ca232af",
    key="CUSTOM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CUSTOM.Name",
    collector_number=1,
    set_code="CUSTOM",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Ability(
            "Set Up",
            game_text="When you play this Pokemon from your hand onto your Bench, you may draw cards until you have 6 cards in your hand.",
            trigger=Triggers.ON_PLAY,
            effect=set_up,
        )
    ]
)