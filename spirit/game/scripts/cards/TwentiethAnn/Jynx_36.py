"""STUB: effect not implemented — do not guess mechanics.
Jynx (TwentiethAnn #36): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1460c34-7ece-5391-879f-8dc86a03a634",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="TwentiethAnn",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Ability(
            title="Victory Kiss",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may heal 10 damage from your Active Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)