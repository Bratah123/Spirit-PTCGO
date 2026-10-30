"""STUB: effect not implemented — do not guess mechanics.
Larvitar (POP1 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29e0a68b-df13-56f0-b973-54ac7311ffec",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar",
    searchable_by=["Larvitar", "Basic", "Larvitar"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=246,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="If the Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=smokescreen_attack(),
        ),
    ],
)