from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import effective_max_hp


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


def _damaged(board, p):
    return effective_max_hp(board, p) > p.get_attribute(AttrID.HP, 0)


def _wormadam_first_condition(board, player_id, pokemon=None):
    mine = list(board.pokemon_in_play(player_id))
    return len(mine) > 1 and any(_named(p, "Wormadam") and _damaged(board, p) for p in mine)


async def _wormadam_first(ctx):
    """Move 1 damage counter from 1 of your Wormadam to another of your Pokemon."""
    srcs = [p for p in ctx.my_pokemon_in_play() if _named(p, "Wormadam") and _damaged(ctx.board, p)]
    if not srcs:
        return
    src = srcs[0] if len(srcs) == 1 else await ctx.choose_pokemon(srcs, "Move a counter from which Wormadam?")
    dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
    if src is not None and dests:
        await ctx.move_damage_counters(src, dests, max_count=1)


card = PokemonCardDef(
    guid="364d0364-661b-56cd-b813-732258b681f4",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name",
    display_name="Mothim",
    searchable_by=["Mothim", "Stage 1", "Mothim"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=412,
    abilities=[
        Ability(
            title="Wormadam First",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Wormadam to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_wormadam_first_condition,
            effect=_wormadam_first,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)