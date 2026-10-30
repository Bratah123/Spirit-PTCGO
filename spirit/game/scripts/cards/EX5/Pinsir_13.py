"""STUB: effect not implemented — do not guess mechanics.
Pinsir (EX5 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


from spirit.game.card_effects.ex import crust_passive

card = PokemonCardDef(
    guid="ac214669-1c58-5690-bb5f-095a94a541a1",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Ability(
            title="Crust",
            game_text="Any damage done to Pinsir by attacks from your opponent's Basic Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=crust_passive(30),
        ),
        Attack(
            title="Sonicboom",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=sonic_boom,
        ),
    ],
)