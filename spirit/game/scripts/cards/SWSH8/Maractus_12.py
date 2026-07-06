from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a8756632-c300-52e6-90f9-6098398f810a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Ditch and Shake",
            game_text="Discard any number of Pok\u00e9mon Tool cards from your hand. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)