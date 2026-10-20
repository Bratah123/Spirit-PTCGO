from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dd37492e-0ec6-51e2-8a36-a0e17e62531e",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    display_name="Sandile",
    searchable_by=["Sandile", "Basic", "Sandile"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=551,
    abilities=[
        Attack(
            title="Sand Dive",
            game_text="Flip a coin. If heads, prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)