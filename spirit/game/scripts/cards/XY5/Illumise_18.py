from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="91e40882-8c6e-53a0-8e6f-ede7a26b6425",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Attack(
            title="Helping Hand",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card, count=1, distribute=False, target_pred=lambda p: not is_in_active_spot(p), prompt='Choose a basic Energy card to attach.'),
        ),
        Attack(
            title="Twirling Sign",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)