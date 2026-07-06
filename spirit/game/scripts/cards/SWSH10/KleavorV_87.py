from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77f605f7-0d49-54c0-a30c-86433a18731b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorV.Name",
    display_name="Kleavor V",
    searchable_by=["Kleavor V", "Basic", "V", "KleavorV"],
    subtypes=["Basic", "V"],
    collector_number=87,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=900,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Axe Slash",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)