from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_type_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _fling(ctx):
    """Put 3 Water Energy cards from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if is_energy_card(c) and _is_type_energy(c)]
    n = min(3, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 3 Water Energy cards")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="cb9f855c-bdb4-5dd0-86fb-4482054a9df4",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Water Fling",
            game_text="Put 3 Water Energy from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_fling,
        ),
        Attack(
            title="Hand Fling",
            game_text="This attack does 10 damage times the number of cards in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=damage_per(lambda ctx: len(ctx.hand()), 10),
        ),
    ],
)