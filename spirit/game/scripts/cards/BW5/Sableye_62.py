from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="6fff0b86-4073-5055-b04b-c5cd23e14baa",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Junk Hunt",
            game_text="Put 2 Item cards from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=recover_from_discard(is_item_card, count=2, minimum=1,
                                        prompt='Choose 2 Item cards to put into your hand'),
        ),
    ],
)