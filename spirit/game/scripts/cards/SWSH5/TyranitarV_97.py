from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed01b5eb-45b3-5158-b1cf-8a282c8b353d",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarV.Name",
    display_name="Tyranitar V",
    searchable_by=["Tyranitar V", "Basic", "V", "Single Strike", "TyranitarV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=97,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=248,
    abilities=[
        Attack(
            title="Cragalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Single Strike Crush",
            game_text="Discard the top 4 cards of your deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=unimplemented,
        ),
    ],
)