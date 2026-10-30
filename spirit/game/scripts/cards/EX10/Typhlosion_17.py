"""STUB: effect not implemented — do not guess mechanics.
Typhlosion (EX10 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.ex import burning_aura
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_per, damage_counters_on


card = PokemonCardDef(
    guid="6535b7a1-23d9-5f73-be30-2379b452753c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Burning Aura",
            game_text="As long as Typhlosion is your Active Pok\u00e9mon, put 1 damage counter on each Active Pok\u00e9mon (both yours and your opponent's) between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            trigger=Triggers.BETWEEN_TURNS,
            effect=burning_aura(1),
        ),
        Attack(
            title="Flickering Flames",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Rage",
            game_text="Does 50 damage plus 10 more damage for each damage counter on Typhlosion.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=damage_per(damage_counters_on('self'), per=10, base=50),
        ),
    ],
)