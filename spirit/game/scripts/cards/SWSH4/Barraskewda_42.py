from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39ae597b-4774-5908-974c-116cdbfa0069",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1", "Barraskewda"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Targeted Skewer",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon for each damage counter on that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)