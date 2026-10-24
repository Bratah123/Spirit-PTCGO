from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import smokescreen_attack


_CONDITION_BY_NAME = {name: cond for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


def _busybody_condition(board, player_id, pokemon=None):
    return board.active_pokemon(player_id) is not None


async def _busybody(ctx):
    """From your hand: reveal this card, heal 10 damage and remove a Special
    Condition from your Active Pokemon, then discard this card."""
    await ctx.reveal_cards([ctx.source])
    active = ctx.my_active()
    if active is not None:
        await ctx.heal(10, active)
        names = [n for n in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
                 if n in _CONDITION_BY_NAME]
        if names:
            index = 0
            if len(names) > 1:
                index = await ctx.choose("Remove which Special Condition?", [str(n) for n in names])
            await ctx.cure_condition(active, _CONDITION_BY_NAME[names[index]])
    await ctx.discard_cards([ctx.source])


card = PokemonCardDef(
    guid="5925c064-7e2c-55cf-baa8-69c7f5df4113",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Ability(
            title="Busybody",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your hand, you may reveal it. If you do, heal 10 damage and remove a Special Condition from your Active Pok\u00e9mon. Then, discard this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            usable_from="hand",
            activation=Activations.ONCE_PER_TURN,
            condition=_busybody_condition,
            effect=_busybody,
        ),
        Attack(
            title="Hip Bump",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=smokescreen_attack(),
        ),
    ],
)