from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID


async def _sinister_hand(ctx):
    """Move 1 damage counter from 1 of your opponent's Pokemon to another of their Pokemon."""
    pool = ctx.opponent_pokemon_in_play()
    damaged = [p for p in pool if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged or len(pool) < 2:
        return
    source = await ctx.choose_pokemon(damaged, "Choose a Pok\u00e9mon to move a damage counter from")
    if source is None:
        return
    dests = [p for p in pool if p is not source]
    await ctx.move_damage_counters(source, dests, max_count=1,
                                   prompt="Choose where to move the damage counter")


def _sinister_condition(board, player_id, pokemon=None):
    pool = _opp_pokemon(board, player_id)
    return len(pool) >= 2 and any(
        p.get_attribute(AttrID.HP, 0) < p.attribute_originals.get(AttrID.HP.value, 0) for p in pool)


def _opp_pokemon(board, player_id):
    return [p for pid in board.player_ids if pid != player_id for p in board.pokemon_in_play(pid)]


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="d37bb8ee-217f-513d-a591-8e6e477f75b9",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=104,
    set_code="BW10",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=477,
    abilities=[
        Ability(
            title="Sinister Hand",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_sinister_condition,
            effect=_sinister_hand,
        ),
        Attack(
            title="Shadow Punch",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=feint,
        ),
    ],
)