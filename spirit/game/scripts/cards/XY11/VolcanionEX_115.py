"""STUB: effect not implemented — do not guess mechanics.
Volcanion-EX (XY11 #115): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="7594e1de-ff5c-5c0d-8948-8a92ca6d2b87",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionEX.Name",
    display_name="Volcanion-EX",
    searchable_by=["Volcanion-EX", "Basic", "EX", "VolcanionEX"],
    subtypes=["Basic", "EX"],
    collector_number=115,
    set_code="XY11",
    rarity=Rarities.RareSecret,
    hp=180,
    elements=[PokemonTypes.FIRE, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Steam Up",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, during this turn, your Basic Fire Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)