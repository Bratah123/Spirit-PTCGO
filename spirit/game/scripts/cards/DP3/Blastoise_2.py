"""STUB: effect not implemented — do not guess mechanics.
Blastoise (DP3 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a6303097-4017-5795-81c5-961917eb2b70",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Waterlog",
            game_text="Once during your turn (before your attack), you may attach as many basic Water Energy cards from your hand to any of your Pok\u00e9mon in any way you like. If you do, your turn ends. This power can't be used if Blastoise is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 50 damage plus 20 more damage for each Water Energy attached to Blastoise but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)