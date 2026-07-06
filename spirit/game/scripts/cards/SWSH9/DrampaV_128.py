from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62488140-1f03-5ffc-bc97-9992d0a4570c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrampaV.Name",
    display_name="Drampa V",
    searchable_by=["Drampa V", "Basic", "V", "DrampaV"],
    subtypes=["Basic", "V"],
    collector_number=128,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)