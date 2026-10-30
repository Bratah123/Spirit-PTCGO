"""STUB: effect not implemented — do not guess mechanics.
Meditite (EX14 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters


card = PokemonCardDef(
    guid="9b5c275b-9ac6-5f4e-8b42-e761c73d0331",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    display_name="Meditite",
    searchable_by=["Meditite", "Basic", "Meditite"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=307,
    abilities=[
        Attack(
            title="Kick",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Pure Power",
            game_text="Put 2 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=place_counters(2, 'choose_any_opponent'),
        ),
    ],
)