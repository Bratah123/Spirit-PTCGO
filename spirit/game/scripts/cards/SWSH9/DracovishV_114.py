from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def slosh_n_crash(ctx):
    """Before damage: discard all Tools from the opponent's Active. If any
    were discarded this way, this attack does 120 more damage."""
    defender = ctx.defender
    bonus = 0
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [c for c in defender.children
                 if c.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
        if tools:
            await ctx.discard_cards(tools)
            bonus = 120
    await ctx.deal_damage(60 + bonus)


card = PokemonCardDef(
    guid="257ca341-0fbd-543d-9343-145c83692f52",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DracovishV.Name",
    display_name="Dracovish V",
    searchable_by=["Dracovish V", "Basic", "V", "DracovishV"],
    subtypes=["Basic", "V"],
    collector_number=114,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=882,
    abilities=[
        Attack(
            title="Slosh 'n' Crash",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon. If you discarded a Pok\u00e9mon Tool in this way, this attack does 120 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="+",
            effect=slosh_n_crash,
        ),
        Attack(
            title="Dragon Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Dragon Strike.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 2},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)