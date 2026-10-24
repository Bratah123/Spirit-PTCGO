from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_discard
from spirit.game.card_effects.pokemon import is_energy_card


def _is_special_energy(card):
    return is_energy_card(card) and bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


async def _plentiful_placement(ctx):
    """Put 4 damage counters on 1 of your opponent's Pokemon."""
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pok\u00e9mon to put 4 damage counters on")
    if target is not None:
        await ctx.deal_damage(40, target=target, as_counters=True)


card = PokemonCardDef(
    guid="85000b67-5c40-5c30-9ac7-46eb725be203",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Shadow Steal",
            game_text="Does 50 damage times the number of Special Energy cards in your opponent's discard pile.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_discard('opponent', _is_special_energy), 50),
        ),
        Attack(
            title="Plentiful Placement",
            game_text="Put 4 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_plentiful_placement,
        ),
    ],
)