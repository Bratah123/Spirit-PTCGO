from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a23f06f3-a96d-5584-9140-96c3cc4b953d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Max Milk",
            game_text="Heal all damage from 1 of your Pok\u00e9mon. Then, discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)