from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="36e1ec87-a2da-5747-8ca3-fb237186af7f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SWSH4",
    rarity=Rarities.Amazing,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Energy Press",
            game_text="This attack does 30 damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Amazing Bloom",
            game_text="For each of your Benched Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)