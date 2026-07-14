from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import effective_max_hp
from spirit.game.card_effects.attacks_common import damage_per, count_hand


def painful_spoons_condition(board, player_id, pokemon):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    opp_pokemon = board.pokemon_in_play(opponent)
    if len(opp_pokemon) < 2:
        return False
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in opp_pokemon)


async def painful_spoons(ctx):
    """Move up to 2 damage counters from 1 of your opponent's Pokemon to another."""
    damaged = [
        p for p in ctx.opponent_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not damaged:
        return
    source = await ctx.choose_pokemon(
        damaged, "Choose 1 of your opponent's Pokémon to move damage counters from"
    )
    if source is None:
        return
    targets = [p for p in ctx.opponent_pokemon_in_play() if p is not source]
    if not targets:
        return
    dest = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to move the damage counters to"
    )
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=2)


card = PokemonCardDef(
    guid="83366c0e-ddc2-5065-b76d-ddb9dea45513",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantAlakazam.Name",
    display_name="Radiant Alakazam",
    searchable_by=["Radiant Alakazam", "Basic", "Radiant", "RadiantAlakazam"],
    subtypes=["Basic", "Radiant"],
    collector_number=59,
    set_code="SWSH12",
    rarity=Rarities.RareRadiant,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=65,
    abilities=[
        Ability(
            title="Painful Spoons",
            game_text="Once during your turn, you may move up to 2 damage counters from 1 of your opponent's Pok\u00e9mon to another of their Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=painful_spoons_condition,
            effect=painful_spoons,
        ),
        Attack(
            title="Mind Ruler",
            game_text="This attack does 20 damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_hand("opponent"), 20),
        ),
    ],
)