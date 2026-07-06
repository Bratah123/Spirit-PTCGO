from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4c752968-166d-5825-9c08-acb3f38c199d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DracozoltV.Name",
    display_name="Dracozolt V",
    searchable_by=["Dracozolt V", "Basic", "V", "DracozoltV"],
    subtypes=["Basic", "V"],
    collector_number=58,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=880,
    abilities=[
        Attack(
            title="Primeval Beak",
            game_text="During your opponent's next turn, Energy cards can't be attached from your opponent's hand to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Mountain Swing",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)