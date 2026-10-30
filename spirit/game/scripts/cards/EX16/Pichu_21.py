"""STUB: effect not implemented — do not guess mechanics.
Pichu (EX16 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition, cry_for_help


card = PokemonCardDef(
    guid="1afbf0dc-2e1e-5f08-a2c7-6fa530b1d7da",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX16",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Pikachu'),
            effect=baby_evolution('Pikachu'),
        ),
        Attack(
            title="Cry for Help",
            game_text="Search your deck for a Lightning Pok\u00e9mon (excluding Pok\u00e9mon-ex), show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=cry_for_help(PokemonTypes.LIGHTNING),
        ),
    ],
)