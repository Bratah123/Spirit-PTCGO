from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df0e83ae-0bc6-5680-b00b-3b6ec9b00eaa",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RhyperiorV.Name",
    display_name="Rhyperior V",
    searchable_by=["Rhyperior V", "Basic", "V", "RhyperiorV"],
    subtypes=["Basic", "V"],
    collector_number=181,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=464,
    abilities=[
        Attack(
            title="Drill Run",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Rock Artillery",
            game_text="During your next turn, this Pok\u00e9mon can't use Heavy Rock Artillery.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)