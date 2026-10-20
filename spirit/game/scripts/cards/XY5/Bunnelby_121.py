from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import mill_attack


async def _rototiller(ctx):
    """Shuffle a card from your discard pile into your deck."""
    cards = list(ctx.discard_pile())
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a card to shuffle into your deck")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = PokemonCardDef(
    guid="3c22761e-f127-577f-a8b1-553445779489",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    display_name="Bunnelby",
    searchable_by=["Bunnelby", "Basic", "Bunnelby"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=659,
    abilities=[
        ancient_trait('Ω Barrage'),
        Attack(
            title="Burrow",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Rototiller",
            game_text="Shuffle a card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_rototiller,
        ),
    ],
)