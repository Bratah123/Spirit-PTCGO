"""STUB: effect not implemented — do not guess mechanics.
Azurill (EX11 #20): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition


card = PokemonCardDef(
    guid="293ecac5-6ab1-5fe9-b515-10b7687cd38a",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Marill from your hand onto Azurill (this counts as evolving Azurill) and remove all damage counters from Azurill.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition('Marill'),
            effect=baby_evolution('Marill'),
        ),
        Attack(
            title="Type Match",
            game_text="Choose a basic Energy card in your hand and show it to your opponent. Then, search your deck for a Basic Pok\u00e9mon or Evolution card of that Energy type, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=baby_evolution('Marill'),
        ),
    ],
)