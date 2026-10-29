from spirit.game.data_utils import PokemonCardDef, Attack, Ability
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
    guid="eadfb806-7ec6-564a-aaef-586e5c14d6ad",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic", "Chinchou"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=170,
    abilities=[
        Attack(
            title="Searching Light",
            game_text="Look at 1 of your face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_safety_check,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)