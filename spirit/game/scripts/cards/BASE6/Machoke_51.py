from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_counters_on, damage_per, recoil_attack,
)


card = PokemonCardDef(
    guid="7b52a142-5a5e-51e9-945d-0fc52427b524",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Karate Chop",
            game_text="Does 50 damage minus 10 damage for each damage counter on Machoke.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="-",
            effect=damage_per(damage_counters_on("self"), -10, base=50),
        ),
        Attack(
            title="Submission",
            game_text="Machoke does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=recoil_attack(20),
        ),
    ],
)
