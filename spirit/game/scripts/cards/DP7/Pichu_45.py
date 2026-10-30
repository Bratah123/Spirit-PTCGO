"""STUB: effect not implemented — do not guess mechanics.
Pichu (DP7 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a6a2a64f-6b1f-5ba7-b371-bbdb2732e625",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Electric Circuit",
            game_text="Search your discard pile for up to 4 Lightning Energy cards, show them to your opponent, and put them into your hand.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)