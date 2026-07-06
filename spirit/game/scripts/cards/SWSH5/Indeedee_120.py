from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bed6476b-7025-5d9e-9663-dcdf39f99c2b",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name",
    display_name="Indeedee",
    searchable_by=["Indeedee", "Basic", "Indeedee"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hand Kinesis",
            game_text="This attack does 10 damage for each card in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)