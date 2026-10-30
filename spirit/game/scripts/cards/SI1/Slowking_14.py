from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    count_energy, damage_per, flip_or_nothing,
)
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card


card = PokemonCardDef(
    guid="2bb670f3-22b9-5a57-bf96-c0a73144688c",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=199,
    abilities=[
        Attack(
            title="Revelation",
            game_text="Flip a coin. If heads, search your deck for a Trainer card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=flip_or_nothing(then=search_to_hand(
                is_trainer_card, count=1, minimum=0, reveal=True,
                prompt="Choose a Trainer card.",
            )),
        ),
        Attack(
            title="Psychic",
            game_text="Does 10 damage plus 10 more damage for each Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender", cards=True), 10, base=10),
        ),
    ],
)
