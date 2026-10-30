"""STUB: effect not implemented — do not guess mechanics.
Suicune (DP3 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import charm_reduce_defender_next


card = PokemonCardDef(
    guid="aebbde38-b4c7-5782-866c-4d7fa1fe5b07",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Aqua Recover",
            game_text="Once during your turn, when you put Suicune from your hand onto your Bench, you may search your discard pile for up to 3 Water Pok\u00e9mon, show them to your opponent, and put them into your hand.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cure Stream",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=charm_reduce_defender_next(20),
        ),
    ],
)