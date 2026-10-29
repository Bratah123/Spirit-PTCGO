from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks
from spirit.game.session.effects import is_basic_pokemon


async def tie_up(ctx):
    """20. If the Defending Pokemon is a Basic Pokemon, it can't attack next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_basic_pokemon(defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="fe4a5a7f-bbfc-5908-942e-ad048720e336",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic", "Piplup"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(
            title="Bubble Hold",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            effect=tie_up,
        ),
    ],
)