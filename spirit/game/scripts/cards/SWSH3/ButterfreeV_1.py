from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="615c3c80-031e-5c8a-9b68-9a24e4501ea1",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ButterfreeV.Name",
    display_name="Butterfree V",
    searchable_by=["Butterfree V", "Basic", "V", "ButterfreeV"],
    subtypes=["Basic", "V"],
    collector_number=1,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=12,
    abilities=[
        Attack(
            title="Dizzying Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)