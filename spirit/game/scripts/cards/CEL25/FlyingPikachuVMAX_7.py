from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import prevent_damage_when


def _max_balloon_shield(calc, carrier):
    if calc.target is not carrier:
        return False
    attacker = calc.attacker
    return attacker is not None and \
        attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value


async def _max_balloon(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, prevent_damage_when(_max_balloon_shield)
    )


card = PokemonCardDef(
    guid="a3f7a335-9942-5930-9395-5f6d4d26754e",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachuVMAX.Name",
    display_name="Flying Pikachu VMAX",
    searchable_by=["Flying Pikachu VMAX", "VMAX", "FlyingPikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=7,
    set_code="CEL25",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Max Balloon",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=_max_balloon,
        ),
    ],
)