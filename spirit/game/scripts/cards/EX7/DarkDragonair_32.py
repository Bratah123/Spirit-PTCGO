"""STUB: effect not implemented — do not guess mechanics.
Dark Dragonair (EX7 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


async def double_wing_attack(ctx):
    """Does 20 damage to each Defending Pokémon (no printed damage)."""
    await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="12840a9d-35c5-5845-8af6-7683ffbd99fd",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDragonair.Name",
    display_name="Dark Dragonair",
    searchable_by=["Dark Dragonair", "Stage 1", "DarkDragonair"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Double Tackle",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=double_wing_attack,
        ),
        Attack(
            title="Crushing Blow",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(1, flip=True),
        ),
    ],
)