"""STUB: effect not implemented — do not guess mechanics.
Sceptile (EX9 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import swift_attack
from spirit.game.card_effects.ex import green_essence_passive


card = PokemonCardDef(
    guid="53891197-337b-545a-8e84-b6b8c1ece227",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Green Essence",
            game_text="As long as Sceptile is in play, each of your Active Pok\u00e9mon that has Grass Energy attached to it can't be affected by any Special Conditions.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=green_essence_passive(),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=swift_attack(),
        ),
    ],
)