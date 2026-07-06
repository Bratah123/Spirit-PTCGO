from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c049f814-276b-5712-86e2-e33601c1aaca",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic", "Pidove"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=519,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)