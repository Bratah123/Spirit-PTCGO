from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _dream_of_memories(ctx):
    """Shuffle 3 cards from your discard pile into your deck."""
    cards = list(ctx.discard_pile())
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 3, minimum=min(3, len(cards)),
                                   prompt="Choose 3 cards to shuffle into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = PokemonCardDef(
    guid="d35e6b5e-bd05-52ad-9962-bdc4496abd67",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name",
    display_name="Musharna",
    searchable_by=["Musharna", "Stage 1", "Musharna"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    family_id=517,
    abilities=[
        Attack(
            title="Dream of Memories",
            game_text="Shuffle 3 cards from your discard pile into your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_dream_of_memories,
        ),
        Attack(
            title="Dream Dance",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
    ],
)