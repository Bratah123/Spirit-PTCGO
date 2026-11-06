from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="f942964a-23c8-510e-bae4-0a58d4aabe4b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasClefairy.Name",
    display_name="Erika's Clefairy",
    searchable_by=["Erika's Clefairy", "Basic", "ErikasClefairy"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=35,
    abilities=[
        Attack(
            title="Moonwatching",
            game_text="Search your deck for a basic Energy card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                is_basic_energy_card, count=1, reveal=True,
                prompt="Choose a basic Energy card to put into your hand.",
            ),
        ),
        Attack(
            title="Comet Slap",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)
