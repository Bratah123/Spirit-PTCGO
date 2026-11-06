from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="8bbcbd6c-2f27-565e-a950-18d323d01980",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Lunge",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)