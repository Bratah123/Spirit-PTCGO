from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, condition_attack
from spirit.game.attributes import SpecialConditions

card = PokemonCardDef(
    guid="20d6c658-057e-5168-812c-7d63b0e60d5a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="DM",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=371,
    abilities=[
        Attack(
            title="Risky Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Dragon Eye",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)