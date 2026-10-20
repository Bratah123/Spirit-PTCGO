from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _flash_fire_condition(board, player_id, pokemon=None):
    return pokemon is not None and any(
        _is_fire_energy(e) for p in board.pokemon_in_play(player_id) if p is not pokemon
        for e in board.attached_energies(p))


async def _flash_fire(ctx):
    """Move a Fire Energy from 1 of your Pokemon to this Pokemon."""
    sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    await ctx.move_energy_freely(sources, [ctx.source], predicate=_is_fire_energy, max_count=1,
                                 prompt="Move a Fire Energy to this Pokémon")


card = PokemonCardDef(
    guid="f46d1d42-ff21-5633-84d5-0eaae89c57bb",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonEX.Name",
    display_name="Flareon-EX",
    searchable_by=["Flareon-EX", "Basic", "EX", "FlareonEX"],
    subtypes=["Basic", "EX"],
    collector_number=89,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Ability(
            title="Flash Fire",
            game_text="Once during your turn (before your attack), you may move a Fire Energy from 1 of your Pok\u00e9mon to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flash_fire_condition,
            effect=_flash_fire,
        ),
        Attack(
            title="Blaze Ball",
            game_text="This attack does 20 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.FIRE), 20, base=50),
        ),
    ],
)