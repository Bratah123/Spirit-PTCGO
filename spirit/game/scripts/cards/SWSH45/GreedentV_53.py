from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fce25894-c26a-5c8f-8937-1f63dcb7b102",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentV.Name",
    display_name="Greedent V",
    searchable_by=["Greedent V", "Basic", "V", "GreedentV"],
    subtypes=["Basic", "V"],
    collector_number=53,
    set_code="SWSH45",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=820,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Stumbling Press",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)