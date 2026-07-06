from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f56edb89-68c2-555a-844a-fb0460efae15",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteV.Name",
    display_name="Dragonite V",
    searchable_by=["Dragonite V", "Basic", "V", "DragoniteV"],
    subtypes=["Basic", "V"],
    collector_number=49,
    set_code="PGO",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=149,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Buster Tail",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)