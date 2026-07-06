from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="894c5061-8e44-5472-9611-2af49a1aaed7",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic", "Zacian"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=888,
    abilities=[
        Attack(
            title="Metal Armament",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Amazing Sword",
            game_text="If your opponent has any Pok\u00e9mon VMAX in play, this attack does 150 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=150,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)