from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import attach_from_hand
from spirit.game.card_effects.trainers import is_grass_energy_card


card = PokemonCardDef(
    guid="2ae1ac08-b73b-5193-99c0-df016c22036f",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    display_name="Shroomish",
    searchable_by=["Shroomish", "Basic", "Shroomish"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=285,
    abilities=[
        Attack(
            title="Growth Spurt",
            game_text="Attach a Grass Energy card from your hand to Shroomish.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(
                is_grass_energy_card, target="active",
                prompt="Choose a Grass Energy card to attach.",
            ),
        ),
        Attack(
            title="Poisonpowder",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
