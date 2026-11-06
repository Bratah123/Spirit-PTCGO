from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.session.effects import is_basic_pokemon


async def _head_walking(ctx):
    """Put a Basic Pokemon from your opponent's discard pile onto their Bench; 3 counters on it."""
    pool = [c for c in ctx.discard_pile(ctx.opponent_id) if is_basic_pokemon(c)]
    if not pool:
        return
    pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Pokémon")
    if pick and await ctx.bench_pokemon(pick[0]):
        await ctx.place_damage_counters(3, [pick[0]])


card = PokemonCardDef(
    guid="aee6d470-2aa7-52b0-bcb3-7bea61321ffb",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name",
    display_name="Grumpig",
    searchable_by=["Grumpig", "Stage 1", "Grumpig"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    family_id=325,
    abilities=[
        Attack(
            title="Head Walking",
            game_text="Put a Basic Pok\u00e9mon from your opponent's discard pile onto his or her Bench. Then, put 3 damage counters on that Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_head_walking,
        ),
        Attack(
            title="Knock Back",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)