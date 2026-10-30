"""STUB: effect not implemented — do not guess mechanics.
Jynx δ (EX15 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import stages_of_evolution_retreat_discount
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="117d89d0-1a81-586c-8c7b-02693cca9e2f",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx δ",
    searchable_by=["Jynx \u03b4", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Jynx is an Evolved Pok\u00e9mon, you pay Colorless less to retreat your Fire and Psychic Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=stages_of_evolution_retreat_discount(PokemonTypes.FIRE, PokemonTypes.PSYCHIC),
        ),
        Attack(
            title="Fire Punch",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)