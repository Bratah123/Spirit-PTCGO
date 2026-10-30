"""STUB: effect not implemented — do not guess mechanics.
Wynaut (EX16 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import baby_evolution_ex7, flail_damage


card = PokemonCardDef(
    guid="cb6f2e76-5015-561f-a54b-3a8eb764b5b2",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wynaut.Name",
    display_name="Wynaut",
    searchable_by=["Wynaut", "Basic", "Wynaut"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=360,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Wobbuffet from your hand onto Wynaut (this counts as evolving Wynaut) and remove all damage counters from Wynaut.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=baby_evolution_ex7('Wobbuffet'),
        ),
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Wynaut.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flail_damage(10),
        ),
    ],
)