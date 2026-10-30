"""STUB: effect not implemented — do not guess mechanics.
Swablu (EX8 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import fluff_flip_prevent


card = PokemonCardDef(
    guid="7ab816ef-58a4-57a6-b0fa-2c1f1fdd7c88",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    display_name="Swablu",
    searchable_by=["Swablu", "Basic", "Swablu"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=333,
    abilities=[
        Ability(
            title="Fluff",
            game_text="Whenever Swablu would be damaged or affected by an opponent's attack and already has at least 1 damage counter on it, flip a coin. If heads, prevent all effects of that attack, including damage, done to Swablu.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=fluff_flip_prevent(),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)