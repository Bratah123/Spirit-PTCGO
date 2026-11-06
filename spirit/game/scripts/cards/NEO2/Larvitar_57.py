from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af9c2566-b7fc-595e-bc86-00ab8dd0f4ea",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar",
    searchable_by=["Larvitar", "Basic", "Larvitar"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=246,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)