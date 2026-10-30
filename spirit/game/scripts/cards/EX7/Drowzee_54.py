from spirit.game.card_effects.ex import soothing_wave, insomnia_passive
"""STUB: effect not implemented — do not guess mechanics.
Drowzee (EX7 #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=insomnia_passive(),
    guid="faabd6bf-5954-5afb-9aa8-971bf3501928",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Ability(
            title="Insomnia",
            game_text="Drowzee can't be Asleep.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Soothing Wave",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=soothing_wave(),
        ),
    ],
)