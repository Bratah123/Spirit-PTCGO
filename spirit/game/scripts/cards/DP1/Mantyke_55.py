"""STUB: effect not implemented — do not guess mechanics.
Mantyke (DP1 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition, call_for_friends_basic

card = PokemonCardDef(
    guid="7f20dfdc-a87e-524c-a9c5-21cc03d3524c",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantyke.Name",
    display_name="Mantyke",
    searchable_by=["Mantyke", "Basic", "Mantyke"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=458,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Mantine from your hand onto Mantyke (this counts as evolving Mantyke) and remove all damage counters from Mantyke.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=baby_evolution_condition('Mantine'),
            effect=baby_evolution('Mantine'),
        ),
        Attack(
            title="Call for Friends",
            game_text="Search your deck for a Water Basic Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=call_for_friends_basic(),
        ),
    ],
)