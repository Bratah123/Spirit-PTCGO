from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d6a83755-2794-5dba-996e-639b2ee4639b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Polteageist.Name",
    display_name="Polteageist",
    searchable_by=["Polteageist", "Stage 1", "Polteageist"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    family_id=854,
    abilities=[
        Attack(
            title="Teatime",
            game_text="Each player draws 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)