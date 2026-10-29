from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="8b430d23-c36f-5037-bc0a-4b67f4a5ee40",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=741,
    abilities=[
        Ability(
            title="Vital Dance",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(is_basic_energy_card, count=2, minimum=0, prompt='Choose up to 2 basic Energy cards'),
        ),
        Attack(
            title="Casual Slap",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)