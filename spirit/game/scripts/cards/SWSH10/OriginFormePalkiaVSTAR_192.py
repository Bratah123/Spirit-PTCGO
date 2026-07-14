from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench
from spirit.game.card_effects.support_common import distribute_energy, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_water_pokemon


def _is_water_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def star_portal(ctx):
    pool = [c for c in ctx.discard_pile() if _is_water_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 3, minimum=1,
        prompt="Choose up to 3 Water Energy cards to attach from your discard pile.",
    )
    if not picks:
        return
    targets = [p for p in ctx.my_pokemon_in_play() if is_water_pokemon(p)]
    if not targets:
        return
    await distribute_energy(ctx, picks, targets)


def _star_portal_condition(board, player_id, pokemon=None):
    return requires_discard(_is_water_energy)(board, player_id, pokemon) and \
        any(is_water_pokemon(p) for p in board.pokemon_in_play(player_id))


subspace_swell = damage_per(count_bench("both"), 20, base=60)

card = PokemonCardDef(
    guid="10c0a177-9b69-5844-9358-871d2eb9e71f",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaVSTAR.Name",
    display_name="Origin Forme Palkia VSTAR",
    searchable_by=["Origin Forme Palkia VSTAR", "VSTAR", "OriginFormePalkiaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=192,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaV.Name",
    family_id=484,
    abilities=[
        Ability(
            title="Star Portal",
            game_text="During your turn, you may attach up to 3 Water Energy cards from your discard pile to your Water Pok\u00e9mon in any way you like. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=star_portal,
            condition=_star_portal_condition,
        ),
        Attack(
            title="Subspace Swell",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="+",
            effect=subspace_swell,
        ),
    ],
)