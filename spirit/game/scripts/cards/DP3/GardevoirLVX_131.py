"""STUB: effect not implemented — do not guess mechanics.
Gardevoir LV.X (DP3 #131): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="cd22cd11-0690-5974-a263-77ad70017a8e",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirLVX.Name",
    display_name="Gardevoir LV.X",
    searchable_by=["Gardevoir LV.X", "Level-Up", "GardevoirLVX"],
    subtypes=["Level-Up"],
    collector_number=131,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEVELUP,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Teleportation",
            game_text="Once during your turn (before your attack), choose 1 of your Active Pok\u00e9mon or 1 or your Benched Pok\u00e9mon and switch Gardevoir with that Pok\u00e9mon. This power can't be used if Gardevoir is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bring Down",
            game_text="Choose 1 Pok\u00e9mon (yours or your opponent's) with the fewest remaining HP (excluding Gardevoir) and that Pok\u00e9mon is now Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)