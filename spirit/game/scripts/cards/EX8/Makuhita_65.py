"""STUB: effect not implemented — do not guess mechanics.
Makuhita (EX8 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import thrust_flip_discard_def_energy



card = PokemonCardDef(
    guid="ee77a035-913d-554d-b70b-017607b6e62b",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    display_name="Makuhita",
    searchable_by=["Makuhita", "Basic", "Makuhita"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=296,
    abilities=[
        Attack(
            title="Thrust",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, discard 1 Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=thrust_flip_discard_def_energy(),
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)