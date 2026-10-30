from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import extra_energy_damage, genetic_memory

card = PokemonCardDef(
    guid="21ae8767-3507-5605-9048-29effbbc110b",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdraex.Name",
    display_name="Kingdra ex",
    searchable_by=["Kingdra ex", "Stage 2", "ex", "Kingdraex"],
    subtypes=["Stage 2", "ex"],
    collector_number=92,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Genetic Memory",
            game_text="Use any attack from Kingdra ex's Basic Pok\u00e9mon card or Stage 1 Evolution card. (Kingdra ex doesn't have to pay for that attack's Energy cost.)",
            cost={PokemonTypes.WATER: 1},
            effect=genetic_memory,
        ),
        Attack(
            title="Hydrocannon",
            game_text="Does 50 damage plus 20 more damage for each Water Energy attached to Kingdra ex but not used to pay for this attack's Energy cost. You can't add more than 40 damage in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=extra_energy_damage(20, base=50, energy_type=PokemonTypes.WATER),
        ),
    ],
)