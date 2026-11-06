from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card


card = PokemonCardDef(
    guid="5ed830be-ace9-590f-a662-566a498ea470",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBulbasaur.Name",
    display_name="Erika's Bulbasaur",
    searchable_by=["Erika's Bulbasaur", "Basic", "ErikasBulbasaur"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Sleep Seed",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Errand-Running",
            game_text="Flip a coin. If heads, you may search your deck for a Trainer card. Show it to your opponent and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 2},
            effect=flip_or_nothing(then=search_to_hand(
                is_trainer_card, count=1, minimum=0, reveal=True,
                prompt="Choose a Trainer card.",
            )),
        ),
    ],
)
