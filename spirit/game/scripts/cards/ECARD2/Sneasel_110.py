from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import rob


card = PokemonCardDef(
    guid="52fdac5b-f47f-50f1-9668-5b9f875597da",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Rob",
            game_text="Look at your opponent's hand. Choose all Technical Machine and Pok\u00e9mon Tool cards there and put them into his or her deck. Your opponent shuffles the deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=rob,
        ),
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)
