"""STUB: effect not implemented — do not guess mechanics.
Relicanth (EX5 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


from spirit.game.card_effects.ex import deep_sleep_passive

card = PokemonCardDef(
    guid="cf39dd39-77a4-5e37-bb00-2afaa0ec1977",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=369,
    abilities=[
        Ability(
            title="Deep Sleep",
            game_text="As long as Relicanth is your Active Pok\u00e9mon, a player flips 2 coins for each of his or her Pok\u00e9mon that is Asleep between turns. If either coin is tails, that Pok\u00e9mon is still Asleep.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=deep_sleep_passive(),
        ),
        Attack(
            title="Yawn",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)