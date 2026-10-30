"""STUB: effect not implemented — do not guess mechanics.
Smoochum δ (EX15 #64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import alluring_kiss_search, baby_evolution, baby_evolution_condition


card = PokemonCardDef(
    guid="0f0ecad2-9ea7-5175-b4ec-77b3642dfa48",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum δ",
    searchable_by=["Smoochum \u03b4", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=238,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Jynx from your hand onto Smoochum (this counts as evolving Smoochum) and remove all damage counters from Smoochum.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Jynx'),
            effect=baby_evolution('Jynx'),
        ),
        Attack(
            title="Alluring Kiss",
            game_text="Search your deck for a Basic Pok\u00e9mon and basic Energy card, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=alluring_kiss_search(),
        ),
    ],
)