"""STUB: effect not implemented — do not guess mechanics.
Crawdaunt (EX8 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import cross_cut_evolved_bonus, dark_protection_passive



card = PokemonCardDef(
    guid="09cecf88-20d6-59d7-a156-ba1a5c27bd6b",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1", "Crawdaunt"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Ability(
            title="Dark Protection",
            game_text="Any damage done to Crawdaunt by your opponent's attacks is reduced by 10 for each Darkness Energy attached to Crawdaunt (after applying Weakness and Resistance). You can't reduce more than 20 damage in this way.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=dark_protection_passive(),
        ),
        Attack(
            title="Bubblebeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=cross_cut_evolved_bonus(),
        ),
    ],
)