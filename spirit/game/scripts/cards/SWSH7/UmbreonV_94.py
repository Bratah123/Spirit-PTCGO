from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


async def mean_look(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="b69dc488-99d7-5c97-b620-03a53bd1d211",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonV.Name",
    display_name="Umbreon V",
    searchable_by=["Umbreon V", "Basic", "V", "Single Strike", "UmbreonV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=94,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=197,
    abilities=[
        Attack(
            title="Mean Look",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=mean_look,
        ),
        Attack(
            title="Moonlight Blade",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(has_damage("self"), 80),
        ),
    ],
)