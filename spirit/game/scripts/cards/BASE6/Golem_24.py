from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import selfdestruct_attack


card = PokemonCardDef(
    guid="888010bd-d781-5c92-8d73-7ac612d5f5ae",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name",
    display_name="Golem",
    searchable_by=["Golem", "Stage 2", "Golem"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Avalanche",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 20 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Golem does 100 damage to itself.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=100,
            effect=selfdestruct_attack(bench_damage=20, self_damage=100),
        ),
    ],
)
