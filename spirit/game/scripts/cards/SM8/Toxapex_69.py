from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    venom_fever,
)

card = PokemonCardDef(
    guid="c9cc225b-a7b3-5142-bb08-71c2a3d2a917",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxapex.Name",
    display_name="Toxapex",
    searchable_by=["Toxapex", "Stage 1", "Toxapex"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    family_id=747,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Venom Fever",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 50 damage for each damage counter on that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            damage_operator="x",
            effect=venom_fever
        ),
    ],
)