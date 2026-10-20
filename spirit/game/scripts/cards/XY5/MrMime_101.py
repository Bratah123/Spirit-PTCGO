"""STUB: effect not implemented — do not guess mechanics.
Mr. Mime (XY5 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="74c179dd-4c5e-5664-89e4-af50938fc9dd",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Attack(
            title="Trick",
            game_text="Move a Pok\u00e9mon Tool card attached to 1 of either player's Pok\u00e9mon to another of that player's Pok\u00e9mon that doesn't already have a Pok\u00e9mon Tool attached to it. If there is no Pok\u00e9mon to move the Pok\u00e9mon Tool card to, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)