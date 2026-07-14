from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.pokemon import is_energy_card


def _is_darkness_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and not is_special_energy(card) and PokemonTypes.DARKNESS.value in types


def _dark_squall_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_darkness_energy_card(c) for c in hand.children)


async def dark_squall(ctx):
    """As often as you like: attach a Darkness Energy card from hand to 1 of your Pokemon."""
    energies = [c for c in ctx.hand() if _is_darkness_energy_card(c)]
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose a Darkness Energy card to attach")
    if not picked:
        return
    targets = ctx.my_pokemon_in_play()
    target = await ctx.choose_pokemon(targets, "Choose the Pokémon to attach it to")
    if target is not None:
        await ctx.attach_energy(picked[0], target)


card = PokemonCardDef(
    guid="570ffde2-d8d8-5985-92d7-79ad7505b434",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=110,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Dark Squall",
            game_text="As often as you like during your turn, you may attach a Darkness Energy card from your hand to 1 of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_dark_squall_condition,
            effect=dark_squall,
        ),
        Attack(
            title="Pitch-Black Fangs",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)