"""STUB: effect not implemented — do not guess mechanics.
Mewtwo (XY12 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5308c025-6003-5773-84be-8886e9b419dc",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Barrier",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon. If 1 of your Pok\u00e9mon used Barrier during your last turn, this attack can't be used.",
            cost={PokemonTypes.PSYCHIC: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)