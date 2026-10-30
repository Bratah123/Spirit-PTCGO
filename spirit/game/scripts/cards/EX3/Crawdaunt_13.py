from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, bonus_if, has_damage


card = PokemonCardDef(
    guid="ca387315-c3ab-5275-b12a-6735e14cefa9",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1", "Crawdaunt"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon has any damage counters on it, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(has_damage(), 30),
        ),
    ],
)