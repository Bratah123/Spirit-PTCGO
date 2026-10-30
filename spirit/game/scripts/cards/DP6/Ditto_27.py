"""STUB: effect not implemented — do not guess mechanics.
Ditto (DP6 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2b597b57-a05e-5aca-8b16-59935de8a509",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Ditto DNA",
            game_text="As long as Ditto is your Active Pok\u00e9mon, its maximum HP is the same as your opponent's Active Pok\u00e9mon. Ditto can use the attacks of that Pok\u00e9mon as its own. (You still need the necessary Energy to use each attack.) If that Pok\u00e9mon is no longer your opponent's Active Pok\u00e9mon, choose 1 of your opponent's Active Pok\u00e9mon for Ditto to copy.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)