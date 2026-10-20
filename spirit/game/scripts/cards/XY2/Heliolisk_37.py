from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_energy_card


card = PokemonCardDef(
    guid="7d2e905a-5f2e-5068-8831-42ea342161cc",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1", "Heliolisk"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Parabolic Charge",
            game_text="Search your deck for up to 2 Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_energy_card, count=2, minimum=0, reveal=True,
                prompt='Choose up to 2 Energy cards'),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)