from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_type_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _fling(ctx):
    """Put 3 Fire Energy cards from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if is_energy_card(c) and _is_type_energy(c)]
    n = min(3, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 3 Fire Energy cards")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="0825d732-7ca9-51a1-8fdb-797fecb108e6",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage", "Stage 1", "Simisage"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    family_id=511,
    abilities=[
        Attack(
            title="Fire Fling",
            game_text="Put 3 Fire Energy cards from your discard pile into your hand.",
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