"""STUB: effect not implemented — do not guess mechanics.
Magnemite (EX7 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


card = PokemonCardDef(
    guid="16e3da26-bdd9-5193-943e-616e3871e0f9",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Sonicboom",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=sonic_boom,
        ),
    ],
)