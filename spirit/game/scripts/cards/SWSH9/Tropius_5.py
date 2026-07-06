from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d2fa901f-fe1a-5efe-86d2-b4bb082f952f",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Ability(
            title="Curative Bower",
            game_text="All of your Pok\u00e9mon that have Grass Energy attached can't be Confused, and if they are already Confused, they recover from that Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)