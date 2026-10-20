from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_dark_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS.value)


def _dark_impulse_condition(board, player_id, pokemon=None):
    discard = board.find_player_area(player_id, "discard")
    return board.active_pokemon(player_id) is not None and bool(
        discard and any(_is_dark_energy(c) for c in discard.children))


async def _dark_impulse(ctx):
    """Attach a Darkness Energy card from your discard pile to your Active Pokemon."""
    cards = [c for c in ctx.discard_pile() if _is_dark_energy(c)]
    active = ctx.my_active()
    if not cards or active is None:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Darkness Energy card")
    if picks:
        await ctx.attach_energy(picks[0], active)


card = PokemonCardDef(
    guid="7e1c3a15-943c-591b-b2a7-074ca85ea8c7",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=74,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Dark Impulse",
            game_text="Once during your turn (before your attack), you may attach a Darkness Energy card from your discard pile to your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_dark_impulse_condition,
            effect=_dark_impulse,
        ),
        Attack(
            title="Crazy Headbutt",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)