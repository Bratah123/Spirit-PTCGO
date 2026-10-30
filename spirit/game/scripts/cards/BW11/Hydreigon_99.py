from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


def _is_darkness_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS.value)


def _dark_trance_condition(board, player_id, pokemon=None):
    mine = board.pokemon_in_play(player_id)
    return len(mine) >= 2 and any(_is_darkness_energy(c) for p in mine for c in p.children)


async def _dark_trance(ctx):
    """Move a Darkness Energy attached to 1 of your Pokemon to another of your Pokemon."""
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=_is_darkness_energy, max_count=1,
                                 prompt="Choose a Darkness Energy to move")


card = PokemonCardDef(
    guid="d733bc85-8881-5043-ad3a-da3d3dee2ec8",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=99,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Dark Trance",
            game_text="As often as you like during your turn (before your attack), you may move a Darkness Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_dark_trance_condition,
            effect=_dark_trance,
        ),
        Attack(
            title="Dragonblast",
            game_text="Discard 2 Darkness Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.DARKNESS),
        ),
    ],
)