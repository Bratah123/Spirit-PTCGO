"""STUB: effect not implemented — do not guess mechanics.
Yveltal-EX (XY1 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def shadow_cyclone(ctx):
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench(), max_count=1)


card = PokemonCardDef(
    guid="70ca16fb-b31d-5913-8a29-a2957bd86b4e",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalEX.Name",
    display_name="Yveltal-EX",
    searchable_by=["Yveltal-EX", "Basic", "EX", "YveltalEX"],
    subtypes=["Basic", "EX"],
    collector_number=79,
    set_code="XY1",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Evil Ball",
            game_text="This attack does 20 more damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Y Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=shadow_cyclone,
        ),
    ],
)