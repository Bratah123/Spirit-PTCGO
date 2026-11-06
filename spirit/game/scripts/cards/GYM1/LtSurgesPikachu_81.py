from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy


card = PokemonCardDef(
    guid="4e121c7c-7cd7-5578-905f-74e7f8401ce1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesPikachu.Name",
    display_name="Lt. Surge's Pikachu",
    searchable_by=["Lt. Surge's Pikachu", "Basic", "LtSurgesPikachu"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Charge",
            game_text="Take 1 Lightning Energy card from your discard pile and attach it to Lt. Surge's Pikachu.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(predicate=is_lightning_energy),
        ),
        Attack(
            title="Lightning Tail",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
