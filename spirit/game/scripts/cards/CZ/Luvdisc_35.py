from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def emotional_draw(ctx):
    """Shuffle your hand into your deck. Then, draw 5 cards."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(5)


card = PokemonCardDef(
    guid="0367b96d-ec56-5b5f-96f8-e5ee7689be85",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="CZ",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Attack(
            title="Emotional Draw",
            game_text="Shuffle your hand into your deck. Then, draw 5 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=emotional_draw,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)