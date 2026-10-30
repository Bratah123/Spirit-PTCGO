from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    damage_counters_on, damage_per, flip_damage,
)


card = PokemonCardDef(
    guid="a2874007-288d-50d4-8e69-0608270a2bf6",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    display_name="Vigoroth",
    searchable_by=["Vigoroth", "Stage 1", "Vigoroth"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    family_id=287,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
        Attack(
            title="Rage",
            game_text="Does 20 damage plus 10 more damage for each damage counter on Vigoroth.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=20),
        ),
    ],
)
