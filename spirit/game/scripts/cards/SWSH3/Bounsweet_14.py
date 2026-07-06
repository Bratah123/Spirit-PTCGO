from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd5fc7e6-e8f7-56e6-8922-2fa9fb09bf97",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    display_name="Bounsweet",
    searchable_by=["Bounsweet", "Basic", "Bounsweet"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=761,
    abilities=[
        Attack(
            title="Synthesis",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)