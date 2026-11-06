from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card


card = PokemonCardDef(
    guid="8970c1d7-d2f5-5cc7-8f56-511c1cd2d5e3",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Errand-Running",
            game_text="Search your deck for a Trainer card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(is_trainer_card, count=1, minimum=0, reveal=True,
                                   prompt='Choose a Trainer card'),
        ),
        Attack(
            title="Water Splash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)