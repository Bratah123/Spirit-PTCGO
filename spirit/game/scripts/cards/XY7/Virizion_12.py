from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.attacks_common import bonus_if, count_prizes_remaining


async def _bail_out(ctx):
    """Put 2 Pokemon from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not pool:
        return
    n = min(2, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Pokémon")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


_mine = count_prizes_remaining('mine')
_theirs = count_prizes_remaining('opponent')


def _behind(ctx):
    return _mine(ctx) > _theirs(ctx)


card = PokemonCardDef(
    guid="3cebc353-5dd1-5d65-84ac-c75fd8705fef",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic", "Virizion"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Bail Out",
            game_text="Put 2 Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            effect=_bail_out,
        ),
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards left than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_behind, 80),
        ),
    ],
)