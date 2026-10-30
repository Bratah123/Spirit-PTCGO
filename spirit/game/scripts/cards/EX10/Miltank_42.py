"""STUB: effect not implemented — do not guess mechanics.
Miltank (EX10 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import thick_fat_vs_types, healing_milk_flip


card = PokemonCardDef(
    guid="99a9686c-41dd-53c1-98c9-88530324c754",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to Miltank by attacks from Fire Pok\u00e9mon and Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=thick_fat_vs_types(30, PokemonTypes.FIRE, PokemonTypes.WATER),
        ),
        Attack(
            title="Healing Milk",
            game_text="Flip 2 coins. For each heads, remove 2 damage counters from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=healing_milk_flip(2, 2),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)