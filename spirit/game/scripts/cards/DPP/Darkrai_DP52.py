"""STUB: effect not implemented — do not guess mechanics.
Darkrai (DPP #DP52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="019e7883-3ffa-5501-bfe6-8bc08c054db1",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Ability(
            title="Darkness Aura",
            game_text="If you have Cresselia in play, each of Darkrai's attack does 20 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)