from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="5fdcc1c4-bb68-5479-8dca-3655cafc2026",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name",
    display_name="Seaking",
    searchable_by=["Seaking", "Stage 1", "Seaking"],
    subtypes=["Stage 1"],
    collector_number=59,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    family_id=118,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage times the number of damage counters on Seaking.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), per=10),
        ),
        Attack(
            title="Undulate",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Seaking.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
