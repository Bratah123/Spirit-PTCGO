from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3fc8959-c8de-55b3-89e5-9fc25546a119",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosionV.Name",
    display_name="Hisuian Typhlosion V",
    searchable_by=["Hisuian Typhlosion V", "Basic", "V", "HisuianTyphlosionV"],
    subtypes=["Basic", "V"],
    collector_number=53,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=157,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Petrifying Flame",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)