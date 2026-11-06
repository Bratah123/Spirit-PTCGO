from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.content.definitions import def_for


def _is_fossil_item(card):
    return is_item_card(card) and "Fossil" in getattr(def_for(card.archetype_id), "display_name", "")


async def _fossil_hunt(ctx):
    """Put 2 Item cards that have Fossil in their names from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if _is_fossil_item(c)]
    n = min(2, len(pool))
    if n:
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Fossil Item cards")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="aafd4ab5-ea68-50dc-a998-9ba88b0fee1f",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Team Plasma", "Relicanth"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=24,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=369,
    abilities=[
        Attack(
            title="Fossil Hunt",
            game_text="Put 2 Item cards that have Fossil in their names from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_fossil_hunt,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)