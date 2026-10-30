"""STUB: effect not implemented — do not guess mechanics.
Quagsire (EX10 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dense_vs_evolved


async def puncture(ctx):
    """This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="2c4319f4-a81c-5608-9899-89883d96000d",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Dense",
            game_text="Any damage done to Quagsire by attacks from your opponent's Evolved Pok\u00e9mon is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=dense_vs_evolved(20),
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Rock Hurl",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=puncture,
        ),
    ],
)