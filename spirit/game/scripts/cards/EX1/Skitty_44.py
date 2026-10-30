from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="0227d650-aeac-5bc9-8419-e8d7a69dfe70",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    display_name="Skitty",
    searchable_by=["Skitty", "Basic", "Skitty"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=300,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for 2 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                is_basic_energy_card, count=2, reveal=True,
                prompt="Choose up to 2 basic Energy cards.",
            ),
        ),
        Attack(
            title="Lullaby",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
