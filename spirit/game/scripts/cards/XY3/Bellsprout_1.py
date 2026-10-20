"""STUB: effect not implemented — do not guess mechanics.
Bellsprout (XY3 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def knock_off(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="32783b63-f8ed-58e7-8178-b1ccd10a9c55",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name="Bellsprout",
    searchable_by=["Bellsprout", "Basic", "Bellsprout"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=knock_off,
        ),
    ],
)