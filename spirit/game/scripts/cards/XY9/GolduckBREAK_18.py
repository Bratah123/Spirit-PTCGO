"""STUB: effect not implemented — do not guess mechanics.
Golduck BREAK (XY9 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee6534f9-9946-519d-ad86-4aa20a8280e1",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GolduckBREAK.Name",
    display_name="Golduck BREAK",
    searchable_by=["Golduck BREAK", "BREAK", "GolduckBREAK"],
    subtypes=["BREAK"],
    collector_number=18,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    family_id=54,
    abilities=[
        Ability(
            title="Hyper Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a basic Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)