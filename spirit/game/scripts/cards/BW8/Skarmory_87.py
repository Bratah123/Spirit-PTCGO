from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.session.effects import is_team_plasma_card


async def _cargo_jet(ctx):
    """Discard a Team Plasma card from your hand. If you do, draw 3 cards."""
    if not any(is_team_plasma_card(c) for c in ctx.hand()):
        return
    gone = await ctx.discard_from_hand(1, minimum=0, predicate=is_team_plasma_card,
                                       prompt="Discard a Team Plasma card to draw 3")
    if gone:
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="5f8d8774-009b-5313-a7dc-a0674fbf47be",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Team Plasma", "Skarmory"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=87,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title="Cargo Jet",
            game_text="Discard a Team Plasma card from your hand. if you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_cargo_jet,
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)