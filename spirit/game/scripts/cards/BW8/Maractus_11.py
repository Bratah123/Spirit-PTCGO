from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d137205d-992e-5ce2-979b-9cd8f8d3e801",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=556,
    abilities=[
        Attack(
            title="Dazzle Dance",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)