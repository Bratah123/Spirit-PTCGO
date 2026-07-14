from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def tailwind_draw(ctx):
    await ctx.draw_cards(1)
    session = ctx.session
    going_second = ctx.player_id != session.first_player_id
    if going_second and session.turn_state.turn_number == 2:
        await ctx.draw_cards(3)

card = PokemonCardDef(
    guid="48f2a108-c0af-51ef-b085-cd51a5e52778",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    display_name="Fletchling",
    searchable_by=["Fletchling", "Basic", "Fletchling"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=661,
    abilities=[
        Attack(
            title="Tailwind Draw",
            game_text="Draw a card. If you go second and it's your first turn, draw 3 more cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tailwind_draw,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)