from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import shuffle_random_from_opponent_hand


card = PokemonCardDef(
    guid="1bc6ec56-047a-577c-a6bb-f727c0309162",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Attack(
            title="Surprise",
            game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shuffle_random_from_opponent_hand(),
        ),
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
