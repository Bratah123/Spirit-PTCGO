from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import flip_reduce_damage_passive


card = PokemonCardDef(
    guid="2cddef95-acb3-5638-8482-2252fcf3e04a",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    display_name="Silcoon",
    searchable_by=["Silcoon", "Stage 1", "Silcoon"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Hard Cocoon",
            game_text="During your opponent's turn, if Silcoon would be damaged by an opponent's attack (after applying Weakness and Resistance), flip a coin. If heads, reduce that damage by 30.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=flip_reduce_damage_passive(30, title="Hard Cocoon"),
        ),
        Attack(
            title="Gooey Thread",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
