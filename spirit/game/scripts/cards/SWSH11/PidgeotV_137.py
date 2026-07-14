from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.card_effects.attacks_common import bonus_if


def _on_bench(board, player_id, pokemon):
    return not in_active_spot(board, player_id, pokemon)


async def vanishing_wings(ctx):
    """Once during your turn, if this Pokemon is on your Bench, you may
    shuffle it and all attached cards into your deck."""
    if await ctx.ask_yes_no("Shuffle Pidgeot V and all attached cards into your deck?"):
        await ctx.shuffle_into_deck(full_stack(ctx.source), ctx.player_id)


card = PokemonCardDef(
    guid="38a556a8-210f-50df-9cba-7703f3d9df49",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotV.Name",
    display_name="Pidgeot V",
    searchable_by=["Pidgeot V", "Basic", "V", "PidgeotV"],
    subtypes=["Basic", "V"],
    collector_number=137,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=18,
    abilities=[
        Ability(
            title="Vanishing Wings",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may shuffle it and all attached cards into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_on_bench,
            effect=vanishing_wings,
        ),
        Attack(
            title="Flight Surf",
            game_text="If you have a Stadium in play, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 80),
        ),
    ],
)