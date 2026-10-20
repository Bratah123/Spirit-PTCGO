from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _song_of_echoes(ctx):
    """Shuffle your hand into your deck; draw 1 per Benched Pokemon (both sides)."""
    n = len(ctx.my_bench()) + len(ctx.opponent_bench())
    hand = list(ctx.hand())
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    if n:
        await ctx.draw_cards(n)


card = PokemonCardDef(
    guid="4ab5c463-ea70-5a01-b14b-e3a412aeaaef",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Song of Echoes",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_song_of_echoes,
        ),
        Attack(
            title="Midnight Eyes",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)