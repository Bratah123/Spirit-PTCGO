from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _safety_check(ctx):
    """Look at 1 of your face-down Prize cards."""
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(area.children) if area else []
    if not prizes:
        return
    idx = await ctx.choose("Look at which Prize card?",
                           [str(i + 1) for i in range(len(prizes))]) if len(prizes) > 1 else 0
    card = prizes[idx or 0]
    await ctx.session.prompt_view_cards(ctx.player_id, ctx.source.entity_id, [card],
                                        prompt="Your Prize card")


card = PokemonCardDef(
    guid="fe77e47b-363b-5605-adc0-33394cc78cd5",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    display_name="Patrat",
    searchable_by=["Patrat", "Basic", "Patrat"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=504,
    abilities=[
        Attack(
            title="Safety Check",
            game_text="Look at 1 of your face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_safety_check,
        ),
    ],
)