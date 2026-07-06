from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ff2cdba-3376-5025-8bf2-cd5086770cb4",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuV.Name",
    display_name="Single Strike Urshifu V",
    searchable_by=["Single Strike Urshifu V", "Basic", "V", "Single Strike", "SingleStrikeUrshifuV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=85,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Laser Focus",
            game_text="Search your deck for up to 2 Fighting Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Impact Blow",
            game_text="During your next turn, this Pok\u00e9mon can't use Impact Blow.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)