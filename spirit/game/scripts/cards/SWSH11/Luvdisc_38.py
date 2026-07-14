from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def matching_look(ctx):
    """Each player reveals the top 2 cards of their deck, then draws those cards."""
    await ctx.draw_cards(2, player_id=ctx.player_id)
    await ctx.draw_cards(2, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="d4fd59cd-de2b-5e64-83f7-46e2ba727d47",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Matching Look",
            game_text="Each player reveals the top 2 cards of their deck, then draws those cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=matching_look,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)