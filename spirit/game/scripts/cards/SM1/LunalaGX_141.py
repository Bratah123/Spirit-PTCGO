from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.passives_common import healing_block_passive
from spirit.game.session.passives import carrier_pokemon
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.content.definitions import subtypes_for


def _is_psychic_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


def _transfer_condition(board, player_id, pokemon=None):
    mine = list(board.pokemon_in_play(player_id))
    return len(mine) > 1 and any(_is_psychic_energy(c) for p in mine for c in p.children)


async def _psychic_transfer(ctx):
    """Move a Psychic Energy from 1 of your Pokemon to another of your Pokemon."""
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=_is_psychic_energy, max_count=1)


async def _moongeist_beam(ctx):
    """120; the Defending Pokemon can't be healed during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and defender.parent is not None and not ctx.effects_blocked(defender):
        ctx.add_passive_through_opponents_turn(
            defender, healing_block_passive(lambda t, c: t is carrier_pokemon(c)))


async def _lunar_fall(ctx):
    """Knock Out 1 of your opponent's Basic Pokemon that isn't a Pokemon-GX."""
    pool = [p for p in ctx.opponent_pokemon_in_play()
            if is_basic_pokemon(p) and "GX" not in subtypes_for(p.archetype_id)
            and not ctx.effects_blocked(p)]
    if not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(
        pool, "Knock Out which Basic Pokémon?")
    if target is not None:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="0a9b38e8-a326-5799-b25c-c6ec9e2525fa",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LunalaGX.Name",
    display_name="Lunala-GX",
    searchable_by=["Lunala-GX", "Stage 2", "GX", "LunalaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=141,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Psychic Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Psychic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_transfer_condition,
            effect=_psychic_transfer,
        ),
        Attack(
            title="Moongeist Beam",
            game_text="The Defending Pok\u00e9mon can't be healed during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=120,
            effect=_moongeist_beam,
        ),
        Attack(
            title="Lunar Fall-GX",
            game_text="Knock Out 1 of your opponent's Basic Pok\u00e9mon that isn't a Pok\u00e9mon-GX. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=_lunar_fall,
        ),
    ],
)