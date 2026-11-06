from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    condition_attack,
    flip_or_nothing,
    spread_damage,
)


card = PokemonCardDef(
    guid="01bc1c3f-6d35-53d1-8c46-566c0ad3ac7c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasParas.Name",
    display_name="Erika's Paras",
    searchable_by=["Erika's Paras", "Basic", "ErikasParas"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Irongrip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Poison Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned and this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2},
            effect=flip_or_nothing(then=condition_attack(
                SpecialConditions.POISONED,
                also=spread_damage(10),
            )),
        ),
    ],
)
