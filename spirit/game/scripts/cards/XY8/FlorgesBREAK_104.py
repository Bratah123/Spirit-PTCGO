from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions
from spirit.game.session.passives import effective_max_hp


def _breeze_condition(board, player_id, pokemon=None):
    a = board.active_pokemon(player_id)
    return a is not None and (effective_max_hp(board, a) > a.get_attribute(AttrID.HP, 0)
                              or bool(a.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))


async def _floral_breeze(ctx):
    """Heal 30 damage and remove a Special Condition from your Active Pokemon."""
    a = ctx.my_active()
    if a is None:
        return
    await ctx.heal(30, a)
    current = list(a.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    for cond in SpecialConditions:
        if CLIENT_SPECIAL_CONDITION_NAMES.get(cond) in current:
            await ctx.cure_condition(a, cond)
            break


card = PokemonCardDef(
    guid="be2e5392-8dcd-541f-adf8-153aa68d25bf",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesBREAK.Name",
    display_name="Florges BREAK",
    searchable_by=["Florges BREAK", "BREAK", "FlorgesBREAK"],
    subtypes=["BREAK"],
    collector_number=104,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Floral Breeze",
            game_text="Once during your turn (before your attack), you may heal 30 damage and remove a Special Condition from your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_breeze_condition,
            effect=_floral_breeze,
        ),
    ],
)