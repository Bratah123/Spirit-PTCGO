"""STUB: effect not implemented — do not guess mechanics.
Florges BREAK (XY8 #104): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be2e5392-8dcd-541f-adf8-153aa68d25bf",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlorgesBREAK.Name",
    display_name="Florges BREAK",
    searchable_by=["Florges BREAK", "BREAK", "FlorgesBREAK"],
    subtypes=["BREAK"],
    collector_number=104,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Floral Breeze",
            game_text="Once during your turn (before your attack), you may heal 30 damage and remove a Special Condition from your Active Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)