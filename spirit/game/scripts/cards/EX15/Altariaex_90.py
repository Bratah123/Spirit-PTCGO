"""STUB: effect not implemented — do not guess mechanics.
Altaria ex δ (EX15 #90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import extra_boost_attach_to_stage2, healing_light_all
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="19da8423-282e-55cc-b700-b0a6f1fd24ec",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altariaex.Name",
    display_name="Altaria ex δ",
    searchable_by=["Altaria ex \u03b4", "Stage 1", "ex", "Altariaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=90,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=334,
    abilities=[
        Ability(
            title="Extra Boost",
            game_text="Once during your turn (before your attack), you may attach a basic Energy card from your hand to 1 of your Stage 2 Pok\u00e9mon-ex. This power can't be used if Altaria ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=extra_boost_attach_to_stage2(),
        ),
        Attack(
            title="Healing Light",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=healing_light_all(1),
        ),
    ],
)