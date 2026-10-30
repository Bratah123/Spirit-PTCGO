"""STUB: effect not implemented — do not guess mechanics.
Leafeon LV.X (DP5 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="6360b467-f0e9-5aba-9727-e5bb5822c7c0",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonLVX.Name",
    display_name="Leafeon LV.X",
    searchable_by=["Leafeon LV.X", "Level-Up", "LeafeonLVX"],
    subtypes=["Level-Up"],
    collector_number=99,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Energy Forcing",
            game_text="Once during your turn (before your attack), you may attach an Energy card from your hand to 1 of your Pok\u00e9mon. This power can't be used if Leafeon is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Verdant Dance",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)