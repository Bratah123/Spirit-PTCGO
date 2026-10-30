"""STUB: effect not implemented — do not guess mechanics.
Absol (DP3 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf80af19-dcd8-5f96-b2e5-51bf294274b3",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Attack(
            title="Baleful Wind",
            game_text="Choose a card from your opponent's hand without looking and discard it. If you discarded a Trainer, Supporter, or Stadium card, choose 1 more card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Raid",
            game_text="If you played Absol from your hand during this turn, this attack's base damage is 40 instead of 10.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)