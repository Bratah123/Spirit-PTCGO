from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1bdf6a75-3be9-5ab4-935a-0c8dbb33dce3",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    display_name="Mienfoo",
    searchable_by=["Mienfoo", "Basic", "Mienfoo"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=619,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)