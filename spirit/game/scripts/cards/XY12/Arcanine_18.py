"""STUB: effect not implemented — do not guess mechanics.
Arcanine (XY12 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="8de205ce-7f69-5193-abb9-4747b4aed584",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Burning Road",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, you may move any number of Fire Energy attached to your Pok\u00e9mon to this Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Breath",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)