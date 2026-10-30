"""STUB: effect not implemented — do not guess mechanics.
Swellow δ (EX15 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import agility_flip_protect, extra_wing_stage2_ex_retreat0
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="b42a6b6d-7449-59ec-8f3b-53a12c43f618",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow δ",
    searchable_by=["Swellow \u03b4", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=277,
    abilities=[
        Ability(
            title="Extra Wing",
            game_text="The Retreat Cost for each of your Stage 2 Pok\u00e9mon-ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=extra_wing_stage2_ex_retreat0(),
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Swellow during your opponent's next turn.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=agility_flip_protect(),
        ),
    ],
)