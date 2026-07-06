from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c73632dd-a3fc-55ae-8772-5aca7198a956",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name",
    display_name="Mudsdale",
    searchable_by=["Mudsdale", "Stage 1", "Mudsdale"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    family_id=749,
    abilities=[
        Attack(
            title="Mud Bomb",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Heavy Slam",
            game_text="This attack does 30 less damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)