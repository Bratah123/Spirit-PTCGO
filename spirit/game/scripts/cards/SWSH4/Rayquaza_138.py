from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="69e23074-b5cb-5986-b844-6de666c4c606",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Amazing Burst",
            game_text="Discard all basic Energy from this Pok\u00e9mon. This attack does 80 damage for each type of basic Energy you discarded in this way.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)