from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_metal_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


def _metal_links_condition(board, player_id, pokemon=None):
    discard = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    return bool(discard and any(_is_metal_energy(c) for c in discard.children)) and \
        bool(bench and bench.children)


async def _metal_links(ctx):
    """Attach a Metal Energy card from your discard pile to 1 of your Benched Pokemon."""
    cards = [c for c in ctx.discard_pile() if _is_metal_energy(c)]
    bench = ctx.my_bench()
    if not cards or not bench:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Metal Energy card")
    if not picks:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Attach it to which Benched Pokémon?")
    await ctx.attach_energy(picks[0], target or bench[0])


card = PokemonCardDef(
    guid="25ca850d-461d-5c44-97ee-ebfc21486864",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Metal Links",
            game_text="Once during your turn (before your attack), you may attach a Metal Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_metal_links_condition,
            effect=_metal_links,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)