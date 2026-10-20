from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.trainers import is_dragon_pokemon


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _turboblaze_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return (board.active_pokemon(player_id) is pokemon and bool(hand) and any(_is_fire_energy(c) for c in hand.children)
            and any(is_dragon_pokemon(p) for p in board.pokemon_in_play(player_id)))


async def _turboblaze(ctx):
    """Attach a Fire Energy card from your hand to 1 of your Dragon Pokemon."""
    pool = [c for c in ctx.hand() if _is_fire_energy(c)]
    dragons = [p for p in ctx.my_pokemon_in_play() if is_dragon_pokemon(p)]
    if not pool or not dragons:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Fire Energy")
    target = dragons[0] if len(dragons) == 1 else await ctx.choose_pokemon(dragons, "Attach to which Dragon Pokémon?")
    if picks and target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="cd15f85a-c663-5439-ac69-1d0249dd1de4",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic", "Reshiram"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=643,
    abilities=[
        Ability(
            title="Turboblaze",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may attach a Fire Energy card from your hand to 1 of your Dragon Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_turboblaze_condition,
            effect=_turboblaze,
        ),
        Attack(
            title="Bright Wing",
            game_text="Discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)