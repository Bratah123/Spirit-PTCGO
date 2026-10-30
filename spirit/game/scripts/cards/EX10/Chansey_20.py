"""STUB: effect not implemented — do not guess mechanics.
Chansey (EX10 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import hyper_healing


async def double_wing_attack(ctx):
    """Does 20 damage to each Defending Pokémon (no printed damage)."""
    await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="4401c08d-1541-526c-b1cd-3ad66e1de0f8",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Hyper Healing",
            game_text="Remove 1 damage counter and all Special Conditions from each of your Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=hyper_healing(1),
        ),
        Attack(
            title="Double Tack",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=double_wing_attack,
        ),
    ],
)