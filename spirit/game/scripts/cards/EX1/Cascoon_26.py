from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import flip_reduce_damage_passive


card = PokemonCardDef(
    guid="ac9fea88-9254-5ae4-a39a-bbdff4864d9c",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    display_name="Cascoon",
    searchable_by=["Cascoon", "Stage 1", "Cascoon"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Hard Cocoon",
            game_text="During your opponent's turn, if Cascoon would be damaged by an opponent's attack (after applying Weakness and Resistance), flip a coin. If heads, reduce that damage by 30.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=flip_reduce_damage_passive(30, title="Hard Cocoon"),
        ),
        Attack(
            title="Poison Thread",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
