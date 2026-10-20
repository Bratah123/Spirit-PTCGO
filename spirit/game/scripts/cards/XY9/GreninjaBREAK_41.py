"""STUB: effect not implemented — do not guess mechanics.
Greninja BREAK (XY9 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="524342c2-6ed5-5564-8a1c-99790c2209e4",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaBREAK.Name",
    display_name="Greninja BREAK",
    searchable_by=["Greninja BREAK", "BREAK", "GreninjaBREAK"],
    subtypes=["BREAK"],
    collector_number=41,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Giant Water Shuriken",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may discard a Water Energy card from your hand. If you do, put 6 damage counters on 1 of your opponent's Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)